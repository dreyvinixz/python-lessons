import youtube_dl

video_url = 'https://youtu.be/fFPHaHmt8I0?si=ZUn5nku3aBNBsxXE'

ydl_opts = {
    'format': 'best',
    'outtmpl': '%(title)s.%(ext)s',  # O vídeo será salvo com o título original
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download concluído!")
