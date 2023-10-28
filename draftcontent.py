from dataclasses import dataclass,field
from enum import Enum 
from typing import List,Any,Dict,Optional
from draft.util import generate_id,get_system
import platform
from pathlib import Path 
from PIL import Image  
from copy import deepcopy


class RatioType(Enum):
    ORIGINAL = "original" # 原始比例

class ColorSpace(Enum):
    DEFAULT = -1 #empty project 
    SDR = 0 # use this one
    HDR_HLG = 1 # maybe 1, special monitor support
    HDR_PQ = 2 # 2，special monitor support

class TrackType(Enum):
    VIDEO = "video"
    AUDIO = "audio"

@dataclass
class CanvasConfig:
    height: int = field(default=1080)
    ratio: RatioType = field(default=RatioType.ORIGINAL) 
    width: int = field(default=1920)

@dataclass
class Config:
    adjust_max_index: int = field(default=1) 
    attachment_info: list = field(default_factory=list)
    combination_max_index: int = field(default=1)
    export_range: Optional[str] = field(default=None)
    extract_audio_last_index: int = field(default=1)
    lyrics_recognition_id: str = field(default="")
    lyrics_sync: bool = field(default=True)
    lyrics_taskinfo: list = field(default_factory=list)
    maintrack_adsorb: bool = field(default=True)
    material_save_mode: int = field(default=0)
    original_sound_last_index: int = field(default=1)
    record_audio_last_index: int = field(default=1)
    sticker_max_index: int = field(default=1)
    subtitle_recognition_id: str = field(default="")
    subtitle_sync: bool = field(default=True)
    subtitle_taskinfo: list = field(default_factory=list)
    system_font_list: list = field(default_factory=list)
    video_mute: bool = field(default=False)
    zoom_info_params: Optional[str] = field(default=None)

@dataclass
class KeyFrames:
    adjusts: List[Any] = field(default_factory=list)
    audios: List[Any] = field(default_factory=list)
    effects: List[Any] = field(default_factory=list)
    filters: List[Any] = field(default_factory=list)
    handwrites: List[Any] = field(default_factory=list)
    stickers: List[Any] = field(default_factory=list)
    texts: List[Any] = field(default_factory=list)
    videos: List[Any] = field(default_factory=list)

@dataclass
class Platform:
    app_id: int = field(default=3704)
    app_source: str = field(default="lv")
    app_version: str = field(default="4.6.1")
    device_id: str = field(default="0aa41cb15b0a6068e4dd4c1388c7fdfb")
    hard_disk_id: str = field(default="3a0aa421529f1838aff80c80410d602a")
    mac_address: str = field(default="522c331216c24ff306ee05239b2ab7c7")
    os: str = field(default_factory=get_system)
    os_version: str = field(default_factory=platform.version)

@dataclass
class Canvas:
    album_image: str = field(default="")
    blur:int = field(default=0)
    color:str = field(default="")
    id:str = field(default_factory=generate_id) #track.segments[0].extra_material_refs append
    image:str = field(default="")
    image_id:str = field(default="")
    image_name:str = field(default="")
    source_platform:int = field(default=0)
    team_id:str = field(default="")
    type:str = field(default="canvas_color")

@dataclass
class SoundChannelMapping:
    audio_channel_mapping: int = field(default=0)
    id: str = field(default_factory=generate_id) #track.segments[0].extra_material_refs append
    is_config_open: bool = field(default=False)
    type:str = field(default="")
@dataclass
class Speed:
    curve_speed: Optional[str] = field(default=None)
    id: str = field(default_factory=generate_id) #track.segments[0].extra_material_refs append
    mode: int = field(default=0)
    speed: float = field(default=1.0)
    type:str = field(default="speed")

@dataclass
class Crop:
    lower_left_x:int = field(default=0)
    lower_left_y:int = field(default=1)
    lower_right_x:int = field(default=1)
    lower_right_y:int = field(default=1)
    upper_left_x:int = field(default=0)
    upper_left_y:int = field(default=0)
    upper_right_x:int = field(default=1)
    upper_right_y:int = field(default=0)

@dataclass
class Matting:
    flag:int = field(default=0)
    has_use_quick_brush:bool = field(default=False)
    has_use_quick_eraser:bool = field(default=False)
    interactiveTime:List = field(default_factory=list)
    path:str = field(default="")
    strokes:List = field(default_factory=list)

@dataclass
class VideoAlgorithm: 
    algorithms: List[Any] = field(default_factory=list)
    deflicker: Optional[str] = field(default=None)
    motion_blur_config: Optional[str] = field(default=None)
    noise_reduction: Optional[str] = field(default=None)
    path: str = field(default="")
    quality_enhance: Optional[str] = field(default=None)
    time_range: Optional[str] = field(default=None)

@dataclass
class Video:
    aigc_type:str = field(default="none")
    audio_fade: Optional[str] = field(default=None)
    cartoon_path: str = field(default="")
    category_id: str = field(default="")
    category_name: str = field(default="local")
    check_flag: int = field(default=63487)
    crop:Crop = field(default_factory=Crop)
    crop_ratio:str = field(default="free")
    crop_scale:float = field(default=1.0)
    duration:int = field(default=10800000000)
    extra_type_option:int = field(default=0)
    formula_id: str = field(default="")
    freeze: Optional[str] = field(default=None)
    gameplay: Optional[str] = field(default=None)
    has_audio: bool = field(default=False)
    height:int = field(default=1080)
    id: str = field(default_factory=generate_id) #track.segments[].material_id append
    intensifies_audio_path: str = field(default="")
    intensifies_path:str = field(default="")
    is_ai_generate_content: bool = field(default=False)
    is_unified_beauty_mode: bool = field(default=False)
    local_id:str = field(default="")
    local_material_id:str = field(default="")
    material_id:str = field(default="")
    material_name:str = field(default="") # image name
    material_url:str = field(default="")
    matting:Matting = field(default_factory=Matting)
    media_path:str = field(default="")
    object_locked: Optional[str] = field(default=None)
    origin_material_id: str = field(default="")
    path:str = field(default="") #image path
    picture_from: str = field(default="none")
    picture_set_category_id:str = field(default="")
    picture_set_category_name:str = field(default="")
    request_id: str = field(default="")
    reverse_intensifies_path:str = field(default="")
    reverse_path:str = field(default="")
    smart_motion: Optional[str] = field(default=None)
    source: int = field(default=0)
    source_platform: int = field(default=0)
    stable: Optional[str] = field(default=None)
    team_id: str = field(default="")
    type: str = field(default="photo")
    video_algorithm:VideoAlgorithm = field(default_factory=VideoAlgorithm)
    width:int = field(default=1440)

@dataclass
class VocalSeparation:
    choice: int = field(default=0)
    id: str = field(default_factory=generate_id) #track.segments[0].extra_material_refs append
    production_path: str = field(default="")
    time_range: Optional[str] = field(default=None)
    type:str = field(default="vocal_separation")

@dataclass
class Audio:
    app_id:int = 0
    category_id:str = ""
    category_name:str = "local"
    check_flag:int = 1
    duration:int = 0 #duration
    effect_id:str =  ""  
    formula_id:str = ""
    id:str = field(default_factory=generate_id) #segments[].material_id
    intensifies_path:str = ""  
    local_material_id:str = field(default_factory=generate_id) #meta_info.draft_materials.value][0].id
    music_id:str = field(default_factory=generate_id) 
    name:str = "" #name  
    path:str = "" #D:/JianyingPro Drafts/temp/speaker_test_sound.mp3  
    query:str = ""  
    request_id:str = ""
    resource_id:str = ""
    search_id:str = "" 
    source_platform:int = 0  
    team_id:str = ""
    text_id:str = ""
    tone_category_id:str = ""
    tone_category_name:str = ""
    tone_effect_id:str = ""
    tone_effect_name:str = ""  
    tone_speaker:str = ""
    tone_type:str = "" 
    type:str = "extract_music"
    video_id:str = ""
    wave_points:list = field(default_factory=list)

def create_melody_percents():
    return [0]

@dataclass
class AiBeats:
    beat_speed_infos:list = field(default_factory=list)
    beats_path:str = ""
    beats_url:str = ""
    melody_path:str = ""
    melody_percents:list = field(default_factory=create_melody_percents)
    melody_url:str = ""

@dataclass
class Beat:
    ai_beats:AiBeats = field(default_factory=AiBeats)
    enable_ai_beats:bool = field(default=False)
    gear:int = 404
    gear_count:int = 0
    id:str = field(default_factory=generate_id) #segments[].extra_material_refs append
    mode:int = 404
    type:str = "beats"
    user_beats:list = field(default_factory=list)
    user_delete_ai_beats:Optional[str] = field(default=None)

@dataclass
class Materials:
    audio_balances: List[Any] = field(default_factory=list)
    audio_effects: List[Any] = field(default_factory=list)
    audio_fades: List[Any] = field(default_factory=list)
    audios: List[Audio]= field(default_factory=list)
    beats:List[Beat] = field(default_factory=list)
    canvases: List[Canvas] = field(default_factory=list)
    chromas:List[Any] = field(default_factory=list)
    color_curves: List[Any] = field(default_factory=list)
    digital_humans: List[Any] = field(default_factory=list)
    drafts: List[Any] = field(default_factory=list)
    effects: List[Any] = field(default_factory=list)
    flowers: List[Any] = field(default_factory=list)
    green_screens: List[Any] = field(default_factory=list)
    handwrites: List[Any] = field(default_factory=list)
    hsl:List[Any] = field(default_factory=list)
    images: List[Any] = field(default_factory=list)
    log_color_wheels: List[Any] = field(default_factory=list)
    loudnesses: List[Any] = field(default_factory=list)
    manual_deformations: List[Any] = field(default_factory=list)
    masks: List[Any] = field(default_factory=list)
    material_animations: List[Any] = field(default_factory=list)
    material_colors: List[Any] = field(default_factory=list)
    placeholders: List[Any] = field(default_factory=list)
    plugin_effects: List[Any] = field(default_factory=list)
    primary_color_wheels: List[Any] = field(default_factory=list)
    realtime_denoises: List[Any] = field(default_factory=list)
    shapes: List[Any] = field(default_factory=list)
    smart_crops: List[Any] = field(default_factory=list)
    sound_channel_mappings: List[SoundChannelMapping] = field(default_factory=list)
    speeds:List[Speed] = field(default_factory=list)
    stickers: List[Any] = field(default_factory=list)
    tail_leaders: List[Any] = field(default_factory=list)
    text_templates: List[Any] = field(default_factory=list)
    texts: List[Any] = field(default_factory=list)
    transitions: List[Any] = field(default_factory=list)
    video_effects: List[Any] = field(default_factory=list)
    video_trackings: List[Any] = field(default_factory=list)
    videos: List[Video] = field(default_factory=list)
    vocal_separations: List[VocalSeparation] = field(default_factory=list)

@dataclass
class Flip:
    horizontal: bool = field(default=False)
    vertical: bool = field(default=False)

@dataclass
class Scale:
    x:int = field(default=1)
    y:int = field(default=1)

@dataclass
class Transform:
    x:float = field(default=0)
    y:float = field(default=0)

@dataclass 
class Clip:
    alpha:str = field(default=1)
    flip:Flip = field(default_factory=Flip)
    rotation:int = field(default=0)
    scale:Scale = field(default_factory=Scale)
    transform:Transform = field(default_factory=Transform)

@dataclass
class HdrSettings:
    intensity:int = field(default=1)
    mode:int = field(default=1)
    nits:int = field(default=1000)

@dataclass
class ResponsiveLayout:
    enable:bool = field(default=False)
    horizontal_pos_layout:int = field(default=0)
    size_layout:int = field(default=0)
    target_follow:str = field(default="")
    vertical_pos_layout:int = field(default=0)

@dataclass
class TimeRange:
    start:int = field(default=0)
    duration:int = field(default=0)

@dataclass
class UniformScale:
    on:bool = field(default=True)
    value:int = field(default=1)

@dataclass
class Segment:
    cartoon:bool = field(default=False)
    clip:Clip = field(default_factory=Clip)
    common_keyframes:List = field(default_factory=list)
    enable_adjust:bool = field(default=True)
    enable_color_curves:bool = field(default=True)
    enable_color_wheels:bool = field(default=True)
    enable_lut:bool = field(default=True)
    enable_smart_color_adjust:bool = field(default=False)
    extra_material_refs:List[str] = field(default_factory=list)
    group_id:str = field(default="")
    hdr_settings:HdrSettings = field(default_factory=HdrSettings)
    id:str = field(default_factory=generate_id)
    intensifies_audio:bool = field(default=False)
    is_placeholder:bool = field(default=False)
    is_tone_modify:bool = field(default=False)
    keyframe_refs:List[str] = field(default_factory=list)
    last_nonzero_volume:int = field(default=1)
    material_id:str = field(default="") # materials.videos[0].id
    render_index:int = field(default=0)
    responsive_layout: ResponsiveLayout = field(default_factory=ResponsiveLayout)
    reverse:bool = field(default=False)
    source_timerange:TimeRange = field(default_factory=TimeRange)
    speed:float = field(default=1)
    target_timerange:TimeRange = field(default_factory=TimeRange)
    template_id:str = field(default="")
    template_scene:str = field(default="default")
    track_attribute:int = field(default=0)
    track_render_index:int = field(default=0)
    uniform_scale:UniformScale = field(default_factory=UniformScale)
    visible:bool = field(default=True)
    volume:int = field(default=1)


@dataclass
class Track:
    attribute:int = field(default=0)
    flag:int = field(default=0)
    id:str = field(default_factory=generate_id)
    is_default_name:bool = field(default=True)
    name:str = field(default="")
    segments:List[Segment] = field(default_factory=list)
    type:TrackType = field(default=TrackType.VIDEO)


@dataclass
class DraftContent:
    canvas_config: CanvasConfig = field(default_factory=CanvasConfig)
    color_space: ColorSpace = field(default=ColorSpace.SDR)
    config: Config = field(default_factory=Config)
    cover: Optional[str] = field(default=None)
    create_time: int = field(default=0)
    duration: int = field(default=0) # /1000000 -> second
    extra_info: Optional[str] = field(default=None)
    fps: int = field(default=30) 
    free_render_index_mode_on: bool = field(default=False)
    group_container: Optional[str] = field(default=None)
    id: str = field(default_factory=generate_id) # project id
    keyframe_graph_list: list = field(default_factory=list)
    keyframes: KeyFrames = field(default_factory=KeyFrames)
    last_modified_platform:Platform = field(default_factory=Platform)
    materials: Materials = field(default_factory=Materials)
    mutable_config: Optional[str] = field(default=None)
    name: str = field(default="")
    new_version: str = field(default="83.0.0")
    platform: Platform = field(default_factory=Platform)
    relationships: list = field(default_factory=list)
    render_index_track_mode_on: bool = field(default=False)
    retouch_cover: Optional[str] = field(default=None)
    source: str = field(default="default")
    static_cover_image_path: str = field(default="")
    tracks: List[Track] = field(default_factory=list)
    update_time:int = field(default=0)
    version:int = field(default=360000)


   