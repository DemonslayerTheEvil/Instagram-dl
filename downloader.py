import yt_dlp
import os

def download_video(url: str, cookies_file: str):
    # Configure yt-dlp options, including the use of cookies
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'cookiefile': cookies_file  # Path to the cookies file
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info_dict)
            file_name = file_name.rsplit(".", 1)[0] + ".mp3"
        return file_name
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # YouTube video URL
    video_url = input("Enter the YouTube video URL: ")

    # Path to your YouTube cookies.txt file
    cookies_file = "cookies.txt"  # Replace with your cookies file path

    # Download video
    output_file = download_video(video_url, cookies_file)

    if output_file:
        print(f"Downloaded: {output_file}")
    else:
        print("Download failed.")
