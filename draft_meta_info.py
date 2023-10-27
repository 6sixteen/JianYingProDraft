from dataclasses import dataclass,field
from typing import List,Any,Optional
from draft.util import generate_id,get_time,get_time_ms

@dataclass
class DraftEnterPriseInfo:
    draft_enterprise_extra: str = field(default="")
    draft_enterprise_id: str = field(default="")
    draft_enterprise_name: str = field(default="")
    enterprise_material: List[Any] = field(default_factory=list)

@dataclass
class DraftMaterial:
    type:int = field(default=0)
    value:list = field(default_factory=list)

def create_draft_materials():
    draft_materials = []
    draft_material_0 = DraftMaterial(type=0)
    draft_material_1 = DraftMaterial(type=1)
    draft_material_2 = DraftMaterial(type=2)
    draft_material_3 = DraftMaterial(type=3)
    draft_material_6 = DraftMaterial(type=6)
    draft_materials.append(draft_material_0)
    draft_materials.append(draft_material_1)
    draft_materials.append(draft_material_2)
    draft_materials.append(draft_material_3)
    draft_materials.append(draft_material_6)
    return draft_materials

@dataclass
class TimeRange:
    duration:int = -1
    start:int = -1

#photo
@dataclass
class DraftMaterialType0:
    create_time:float = field(default_factory=get_time)
    duration:int = 5000000 #
    extra_info:str = "" #file name
    file_path:str = "" #
    height:int =0 #h
    id:str = field(default_factory=generate_id)
    import_time:float = field(default_factory=get_time)
    import_time_ms:float = field(default_factory=get_time_ms)
    item_source:int = 1
    md5:str = ""
    metetype:str = "photo"
    roughcut_time_range:TimeRange = field(default_factory=TimeRange)
    sub_time_range:TimeRange = field(default_factory=TimeRange)
    type:int = 0
    width:int = 0 #w

@dataclass
class DraftMetaInfo:
    draft_cloud_capcut_purchase_info:str = field(default="")
    draft_cloud_last_action_download: bool = field(default=False)
    draft_cloud_materials: List[Any] = field(default_factory=list)
    draft_cloud_purchase_info: str = field(default="")
    draft_cloud_template_id: str = field(default="")
    draft_cloud_tutorial_info: str = field(default="")
    draft_cloud_videocut_purchase_info: str = field(default="")
    draft_cover: str = field(default="draft_cover.jpg")
    draft_deeplink_url: str = field(default="")
    draft_enterprise_info: DraftEnterPriseInfo = field(default_factory=DraftEnterPriseInfo)
    draft_fold_path: str ="" # 草稿文件夹路径 D:/JianyingPro Drafts/10月25日
    draft_id: str = field(default_factory=generate_id) 
    draft_is_article_video_draft: bool = field(default=False)
    draft_is_from_deeplink: str = field(default="false")
    draft_materials: List[DraftMaterial] = field(default_factory=create_draft_materials)
    draft_materials_copied_info: List[Any] = field(default_factory=list)
    draft_name: str ="" #project name 
    draft_new_version: str = field(default="")
    draft_removable_storage_device: str ="" # D: 盘符
    draft_root_path: str  ="" #root path "D:\\JianyingPro Drafts"
    draft_segment_extra_info: List[Any] = field(default_factory=list)
    draft_timeline_materials_size_: int = 7592
    tm_draft_cloud_completed: str = ""
    tm_draft_cloud_modified: int = 0
    tm_draft_create: int = 1698228018949678
    tm_draft_modified: int = 1698228045497140
    tm_draft_removed: int = 0
    tm_duration: int = 0
