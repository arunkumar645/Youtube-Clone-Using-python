
from fastapi import FastAPI,Form
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp.YoutubeDL

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)



import os
import yt_dlp # type: ignore

cur_dir = os.getcwd()






@app.post("/download")
def download_video(link: str = Form(...)):
    youtube_dl_options = {
        "format": "best",
        "outtmpl": os.path.join(cur_dir, f"video-{link[-11:]}.mp4")
    }
    with yt_dlp.YoutubeDL(youtube_dl_options) as ydl:
        ydl.download([link])
    return {"message": "Download started"}

