# librosa，擅长音频信号处理，内部用numpy存储数据，读写文件依赖soundfile模块（不支持mp3）。
# pydub，底层基于ffmpeg读写文件，代码简洁，支持切割、格式转换、音量、ID3等常用功能，门槛低。


from pydub import AudioSegment  
from pathlib import Path

def get_mp3_duration(file_path):  
    audio = AudioSegment.from_file(file_path, format="mp3")  
    duration = audio.duration_seconds  
    return duration 

temp_path = Path(__file__).resolve().parent / "temp"
file_path = temp_path / "speaker_test_sound.mp3"
print(file_path)
duration = get_mp3_duration(str(file_path))
print("Duration:", duration, "seconds")