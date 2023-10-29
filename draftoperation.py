from copy import deepcopy
from pathlib import Path 
from draft.util import generate_id,judge_image_path,get_mp3_duration
from draftcontent import *
import json 
from dataclasses import asdict 

ttf_dir = Path(__file__).resolve().parent / "ttf"

class DraftOperation:

    @classmethod
    def assign(source_draft_content:DraftContent,target_draft_content:DraftContent):
        """
        This function assigns a source draft content to a target draft content.
        Args:
            source_draft_content (DraftContent): The source draft content.
            target_draft_content (DraftContent): The target draft content.
        """
        # todo implement
    @classmethod
    def __get_track_duration(self,track: Track):
        """
        Get the total duration of a track.

        Args:
            track (Track): The track object.

        Returns:
            int: The total duration of the track.
        """
        # Get the segments of the track
        segments = track.segments

        # If there are no segments, return 0
        if len(segments) == 0:
            return 0

        # Get the last segment
        last_segment = segments[-1]

        # Calculate the total duration
        total_duration = (last_segment.target_timerange.duration 
                        + last_segment.target_timerange.start)

        return total_duration
    @classmethod
    def __update_duration(self,draft_content: DraftContent):
        """
        This function updates the duration of a DraftContent object based on the duration
        of its tracks. If the new duration is greater than the old duration, it updates
        the DraftContent's duration.
        
        Args:
        draft_content (DraftContent): The DraftContent object to update.
        """
        # Get the old duration
        old_duration = draft_content.duration
        
        # Initialize new_duration to 0
        new_duration = 0
        
        # Iterate over each track in the draft content
        for track in draft_content.tracks:
            # Get the duration of the track
            temp_duration = self.__get_track_duration(track)
            # If the track's duration is greater than the old duration,
            # update new_duration
            if temp_duration > old_duration:
                new_duration = temp_duration
        # If new_duration is greater than old_duration, update the DraftContent's duration
        if new_duration > old_duration:
            draft_content.duration = new_duration
    
    @classmethod
    def __get__track_index(self,tracks:List[Track],type:TrackType):
        index = -1
        for i,track in enumerate(tracks):
            if track.type == type:
                return i
        if index == -1:
            raise IndexError(f"no {type.value} track")
    
    @classmethod
    def write2json(self,draft_content:DraftContent,json_path:Path,encoding:str="utf-8"):
        class EnumEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj, Enum):
                    return obj.value
                if isinstance(obj,Path):
                    return str(obj)
                return super().default(obj)
        data = asdict(draft_content)
    # 将字典转换为 JSON 格式  
        json_data = json.dumps(data,cls=EnumEncoder,indent=2) 
        # 将 JSON 数据写入文件  
        with open(json_path, "w",encoding=encoding) as f:  
            f.write(json_data)

    @classmethod
    def add_image2track(self,draft_content:DraftContent, image_path:Path,duration:int=5000000):
        """
        Add an image to a track.
        Args:
            image_path (Path): The path to the image file.
            track_index (int): The index of the track to add the image to.
        Raises:
            FileNotFoundError: If the image_path is not a valid image file or if the image file does not exist.
        """

        image_name = image_path.name
        if not judge_image_path(image_path):
            raise FileNotFoundError("This path is not an image file")
        if not image_path.exists():
            raise FileNotFoundError("no image")
        img = Image.open(image_path) 
        w, h = img.size  

        #deepcopy for error
        copy_draft = deepcopy(draft_content)
        #materials.canvas
        canvases = copy_draft.materials.canvases
        canvas = Canvas()
        canvases.append(canvas)  

        sound_channel_mappings = copy_draft.materials.sound_channel_mappings
        sound_channel_mapping = SoundChannelMapping() 
        sound_channel_mappings.append(sound_channel_mapping)

        speeds = copy_draft.materials.speeds
        speed = Speed()
        speeds.append(speed)

        videos = copy_draft.materials.videos
        video = Video(material_name=image_name,path=str(image_path),type='photo',height=h,width=w) 
        videos.append(video)

        vocal_separations = copy_draft.materials.vocal_separations
        vocal_separation = VocalSeparation() 
        vocal_separations.append(vocal_separation)

        #track 
        tracks = copy_draft.tracks
        if len(tracks) == 0:
            #init track or add new track
            track = Track()
            tracks.append(track)
        
        video_track_index = self.__get__track_index(tracks,TrackType.AUDIO)
        video_track:Track = tracks[video_track_index]
        #Each Image for Each Segment
        segments = video_track.segments
        segment = Segment()
        if len(segments) == 0:
            source_timerange = TimeRange(start=0,duration=duration)
            target_timerange = TimeRange(start=0,duration=duration)
            segment.source_timerange = source_timerange
            segment.target_timerange = target_timerange
        else:
            total_duration = self.__get_track_duration(track)
            source_timerange = TimeRange(start=0,duration=duration)
            target_timerange = TimeRange(start=total_duration,duration=duration)
            segment.source_timerange = source_timerange
            segment.target_timerange = target_timerange

        segment.extra_material_refs.append(speed.id)
        segment.extra_material_refs.append(canvas.id)
        segment.extra_material_refs.append(sound_channel_mapping.id)
        segment.extra_material_refs.append(vocal_separation.id)  
        segment.material_id = video.id
        segments.append(segment)

        self.__update_duration(draft_content=copy_draft)

        return copy_draft
        
    @classmethod
    def add_audio2track(self,draft_content:DraftContent,audio_path:Path,audio_local_material_id:str):

        copy_draft_content = deepcopy(draft_content)
        materials = copy_draft_content.materials
        audios = materials.audios
        audio_name = audio_path.name
        audio_duration = get_mp3_duration(audio_path)
        audio = Audio(name = audio_name,
                      path = audio_path,
                      duration=audio_duration,
                      local_material_id=audio_local_material_id) #segments[].material_id
        audios.append(audio)

        beats = materials.beats
        beat = Beat()
        beats.append(beat)

        sound_channel_mappings = materials.sound_channel_mappings
        sound_channel_mapping = SoundChannelMapping()
        sound_channel_mappings.append(sound_channel_mapping)

        speeds = materials.speeds
        speed = Speed()
        speeds.append(speed)

        vocal_separations = materials.vocal_separations
        vocal_separation = VocalSeparation()
        vocal_separations.append(vocal_separation)

        tracks = copy_draft_content.tracks
        if len(tracks) == 0:
            video_track = Track()
            audio_track = Track(type=TrackType.AUDIO)
            tracks.append(video_track)
            tracks.append(audio_track)
        
        #find video track 
        audio_track_index = self.__get__track_index(tracks,TrackType.AUDIO)
        audio_track:Track = tracks[audio_track_index]
        segments = audio_track.segments
        segment = Segment(clip=None,
                          enable_adjust=False,
                          enable_lut=False,
                          uniform_scale=None,
                          hdr_settings=None)
        
        if len(segments) == 0:
            source_timerange = TimeRange(start=0,duration=audio_duration)
            target_timerange = TimeRange(start=0,duration=audio_duration)
            segment.source_timerange = source_timerange
            segment.target_timerange = target_timerange
        else:
            total_duration = self.__get_track_duration(audio_track)
            source_timerange = TimeRange(start=0,duration=audio_duration)
            target_timerange = TimeRange(start=total_duration,duration=audio_duration)
            segment.source_timerange = source_timerange
            segment.target_timerange = target_timerange

        extra_material_refs = segment.extra_material_refs
        extra_material_refs.append(speed.id)
        extra_material_refs.append(beat.id)
        extra_material_refs.append(sound_channel_mapping.id)
        extra_material_refs.append(vocal_separation.id)  
        segment.material_id = audio.id
        segments.append(segment)

        #update duration
        self.__update_duration(draft_content=copy_draft_content)

        return copy_draft_content
    
    @classmethod
    def add_text2track(self,draft_content:DraftContent,text_content:str,text_duration:int,text_color:str="#FFFFFF",text_size:float=15,ttf:str="zh-hans.ttf"):

        copy_draft_content = deepcopy(draft_content)
        materials = copy_draft_content.materials
        material_animations = materials.material_animations
        material_animation = MaterialAnimation() #append
        material_animations.append(material_animation)
        texts = materials.texts
        ttf_path = ttf_dir / ttf
        text_content_obj = TextContent(content=text_content,color=text_color,size=text_size,ttf_path=str(ttf_path))
        text = Text(content=text_content_obj.text,
                    font_path=ttf_path)
        texts.append(text)
        tracks = copy_draft_content.tracks
        if len(tracks) == 0:
            video_track = Track()
            text_track = Track(type=TrackType.TEXT)
            tracks.append(video_track)
            tracks.append(text_track)
        text_track_index = self.__get__track_index(tracks,TrackType.TEXT)
        text_track:Track = tracks[text_track_index]
        segments = text_track.segments
        segment = Segment(clip=Clip(),
                          enable_adjust=False,
                          enable_lut=False,
                          hdr_settings=None)
        segment.source_timerange = None
        start_duration = self.__get_track_duration(text_track)
        target_timerange = TimeRange(start=start_duration,duration=text_duration)
        segment.target_timerange = target_timerange
        extra_material_refs = segment.extra_material_refs
        extra_material_refs.append(material_animation.id)
        segment.material_id = text.id
        segments.append(segment)

        #update duration
        self.__update_duration(draft_content=copy_draft_content)

        return copy_draft_content