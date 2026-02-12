import streamlit as st
from pytubefix import YouTube
import os
import streamlit as st
from pytubefix import YouTube
import os

st.title("유튜브 오디오 다운로드 (MP3)")
video_url = st.text_input("유튜브 영상의 URL을 입력하세요:")

if st.button("다운로드"):
    try:
        yt = YouTube(video_url)
        st.write(f"{yt.title} 영상 찾는 중...")
        audio_stream = yt.streams.filter(only_audio=True).first()
        output_path = "downloads"
        os.makedirs(output_path, exist_ok=True)
        audio_file = audio_stream.download(output_path)
        base, ext = os.path.splitext(audio_file)
        mp3_file = base + ".mp3"
        os.rename(audio_file, mp3_file)
        with open(mp3_file, "rb") as f:
            st.download_button(
                label="MP3 파일 다운로드",
                data=f,
                file_name=os.path.basename(mp3_file),
                mime="audio/mp3"
            )
        st.success("다운로드 완료!")
    except Exception as e: 