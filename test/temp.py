data = {  
    "app_id": 0,  
    "category_id": "",  
    "category_name": "local",  
    "check_flag": 1,  
    "duration": 6633333,  
    "effect_id": "",  
    "formula_id": "",  
    "id": "4EEEC111-7888-4c31-995E-EDB6EDA77ED7",  
    "intensifies_path": "",  
    "local_material_id": "cb968058-2da8-4065-90d9-a9e5583ea5df",  
    "music_id": "16cf50bd-f366-4d0d-b2a0-9f53ca936ef8",  
    "name": "speaker_test_sound.mp3",  
    "path": "D:/JianyingPro Drafts/temp/speaker_test_sound.mp3",  
    "query": "",  
    "request_id": "",  
    "resource_id": "",  
    "search_id": "",  
    "source_platform": 0,  
    "team_id": "",  
    "text_id": "",  
    "tone_category_id": "",  
    "tone_category_name": "",  
    "tone_effect_id": "",  
    "tone_effect_name": "",  
    "tone_speaker": "",  
    "tone_type": "",  
    "type": "extract_music",  
    "video_id": "",  
    "wave_points": []  
}  
  
new_data = {k: v for k, v in data.items() if isinstance(v, (int, str, list))}  
print(new_data)