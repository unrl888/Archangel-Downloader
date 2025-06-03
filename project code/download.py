import yt_dlp
import json
import os


def read_config(path='C:/downloader/config/config.json'):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data
    
    
def download(url, download_path, quality):
    options = {
        'format': quality,
        'outtmpl': download_path + r'/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',  
        'quiet': True, 
        'no_warnings': True,  
        'postprocessor_args': ['-loglevel', 'error'],
    }
    
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
    except Exception as e:
        pass
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        

def main(url):
    data = read_config()
    download_path = data.get('download_path')
    quality = data.get('quality')
    download(url, download_path, quality)
