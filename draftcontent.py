from dataclasses import dataclass,field
from enum import Enum 
from typing import List,Any,Dict 
from draft.util import generate_id
class RatioType(Enum):
    ORIGINAL = "original" # 原始比例

class ColorSpace(Enum):
    DEFAULT = -1 #empty project 
    SDR = 0 # use this one
    HDR_HLG = 1 # maybe 1, special monitor support
    HDR_PQ = 2 # 2，special monitor support

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
    export_range: list = field(default_factory=list)
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
    zoom_info_params: dict = field(default_factory=dict)

@dataclass
class KeyFrames:
    adjusts: List[Any] = field(default_factory=list)
    audio: List[Any] = field(default_factory=list)
    effects: List[Any] = field(default_factory=list)
    filters: List[Any] = field(default_factory=list)
    handwrites: List[Any] = field(default_factory=list)
    stickers: List[Any] = field(default_factory=list)
    texts: List[Any] = field(default_factory=list)
    videos: List[Any] = field(default_factory=list)

@dataclass
class DraftContent:
    canvas_config: CanvasConfig = field(default_factory=CanvasConfig)
    color_space: ColorSpace = field(default=ColorSpace.SDR)
    config: Config = field(default_factory=Config)
    cover: str = field(default="")
    create_time: int = field(default=0)
    duration: int = field(default=0) # /1000000 -> second
    extra_info: str = field(default="")
    fps: int = field(default=30) 
    free_render_index_mode_on: bool = field(default=False)
    id: str = field(default_factory=generate_id) # project id
    keyframe_graph_list: list = field(default_factory=list)
