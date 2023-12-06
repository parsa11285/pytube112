#from pytube import YouTube

#def download_video(url, path):
    #yt = YouTube(url)
    #yt.streams.first().download(path)

# استفاده از تابع
#download_video('لینک ویدیوی یوتیوب', 'مسیر ذخیره‌سازی')
def download_video(url, path):
    """Downloads a video from the given URL and saves it to the specified path."""

    # Creates a YouTube object from the provided URL
    yt = YouTube(url)

    # Downloads the first available video stream and saves it to the specified path
    yt.streams.first().download(path)