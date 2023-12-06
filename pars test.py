def download_video(url, path): 
    try: 
        proxy = 'http://username:password@proxyserver:port'
        os.environ['http_proxy'] = proxy 
        os.environ['https_proxy'] = proxy 
        yt = YouTube(url) 
        stream = yt.streams.get_highest_resolution() 
        stream.download(path) 
        print(f"Video downloaded successfully") 
    except Exception as e: 
        print(f"An error occurred: {e}") 
youtube_downloader.py

