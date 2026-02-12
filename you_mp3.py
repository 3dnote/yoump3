import streamlit as st
from pytube import YouTube
import os

st.title("유튜브 오디오 다운로드 (MP3)")
video_url = st.text_input("유튜브 영상의 URL을 입력하세요:")

if st.button("다운로드"):
    if not video_url.strip():
        st.warning("유튜브 URL을 입력하세요.")
    else:
        try:
            yt = YouTube(video_url)
            st.write(f"{yt.title} 영상 찾는 중...")
            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream is None:
                st.error("오디오 스트림을 찾을 수 없습니다. 유효한 유튜브 링크인지 확인하세요.")
            else:
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
            st.error(f"다운로드 오류: {e}\n\n유튜브 다운로드가 클라우드 환경에서 차단될 수 있습니다. 로컬 PC에서 실행해보세요.")