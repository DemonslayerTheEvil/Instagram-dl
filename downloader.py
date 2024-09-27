from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_song():
    data = request.json
    video_url = data.get('url')
    
    if not video_url:
        return jsonify({"error": "Please provide a YouTube URL."}), 400

    # Set up yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            file_name = ydl.prepare_filename(info_dict)
            file_name = file_name.rsplit(".", 1)[0] + ".mp3"
        
        # Send response with download link or success message
        return jsonify({"message": "Download successful", "file": file_name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
