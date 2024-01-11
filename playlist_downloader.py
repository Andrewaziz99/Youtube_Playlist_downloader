import os
from pytube import Playlist, YouTube

print('\nYoutube Playlist Downloader. script by ©Andrew Aziz\n')
print('--------------------------------------------------------\n')


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    playlist_name = playlist.title
    os.makedirs(playlist_name, exist_ok=True)  # Create folder for downloads

    for video_url in playlist.video_urls:
        try:
            yt = YouTube(video_url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            print(f"Downloading {yt.title} in {stream.resolution}")
            stream.download(output_path=playlist_name)
        except Exception as e:
            print(f"Error downloading {yt.title}: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_playlist(playlist_url)
