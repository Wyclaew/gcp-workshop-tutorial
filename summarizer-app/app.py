import os
import re
from flask import Flask, render_template, request, redirect
import vertexai
from vertexai.generative_models import GenerativeModel
from youtube_transcript_api import YouTubeTranscriptApi
from pytubefix import YouTube

app = Flask(__name__)

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("PROJECT_ID") or os.environ.get("DEVSHELL_PROJECT_ID")
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)
model = GenerativeModel("gemini-2.5-flash")

def extract_video_id(url):
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_video_metadata(url):
    """Videonun başlık ve açıklamasını çeker."""
    try:
        yt = YouTube(url)
        return {
            "title": yt.title,
            "description": yt.description[:1000] # İlk 1000 karakter yeterli
        }
    except Exception as e:
        print(f"Metadata hatası: {str(e)}")
        return None

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['tr', 'en'])
        return " ".join([t['text'] for t in transcript_list])
    except:
        return None

def generate(youtube_link, additional_prompt):
    if not additional_prompt:
        additional_prompt = "Lütfen videoyu özetle."
    
    video_id = extract_video_id(youtube_link)
    metadata = get_video_metadata(youtube_link)
    transcript = get_transcript(video_id) if video_id else None
    
    # Gemini'ye gönderilecek veri havuzu
    prompt = f"YouTube Video Analizi:\n"
    prompt += f"Link: {youtube_link}\n"
    
    if metadata:
        prompt += f"Video Başlığı: {metadata['title']}\n"
        prompt += f"Video Açıklaması: {metadata['description']}\n"
    
    if transcript:
        prompt += f"Videonun Altyazıları: {transcript}\n"
    
    prompt += f"\nTalimat: {additional_prompt}\n"
    prompt += "Önemli: Eğer videonun içeriği hakkında bilgin yoksa uydurma. Sadece sana verdiğim başlık, açıklama ve altyazı bilgilerini kullanarak özet çıkar."

    response = model.generate_content(prompt)
    return response.text

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["GET", "POST"])
def summarize():
    if request.method == "POST":
        youtube_link = request.form["youtube_link"]
        additional_prompt = request.form["additional_prompt"]
        try:
            summary = generate(youtube_link, additional_prompt)
            return summary
        except Exception as e:
            return f"Hata: {str(e)}", 500
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    app.run(debug=False, port=port, host="0.0.0.0")
