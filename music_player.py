import streamlit as st
import os
import random
from pydub import AudioSegment

def load_audio_files(allmode):
    audio_files = {}
    for file in os.listdir("music_folder"):
        if file.endswith(".wav"):
            if allmode == "Study" and file.startswith("st_"):
                article_id = file.split(".")[0]
                audio_files[article_id] = file
            elif allmode == "Relaxing" and file.startswith("re_"):
                article_id = file.split(".")[0]
                audio_files[article_id] = file
    return audio_files

def play_audio(file):
    audio_bytes = open("music_folder/" + file, "rb").read()
    st.audio(audio_bytes, format="audio/wav")

def main():
    st.title("Music Player🎸🎷")

    # Retrieve query parameters
    article_id = st.query_params.get("article_id", [None])[0]

    # Memilih mode
    allmode = st.selectbox("Mode", ("Study", "Relaxing"))

    # memuat file berdasarkan pilihan
    audio_files = load_audio_files(allmode)

    # mode Loop atau shuffle
    mode = st.radio("Playback Mode", ("Loop", "Shuffle"), key="mode")

    # Peraliahan antara mode study dan relaxing
    st_audio_files = {k: v for k, v in audio_files.items() if v.startswith("st_")}
    re_audio_files = {k: v for k, v in audio_files.items() if v.startswith("re_")}

    # Find matching audio file based on query parameter "article_id"
    current_file = None
    if article_id:
        if allmode == "Study" and article_id in st_audio_files:
            current_file = st_audio_files[article_id]
        elif allmode == "Relaxing" and article_id in re_audio_files:
            current_file = re_audio_files[article_id]

    # shuffle audio
    if mode == "Shuffle":
        if allmode == "Study":
            audio_files = list(st_audio_files.values())
            random.shuffle(audio_files)
        elif allmode == "Relaxing":
            audio_files = list(re_audio_files.values())
            random.shuffle(audio_files)
    else:
        if allmode == "Study":
            audio_files = list(st_audio_files.values())
        elif allmode == "Relaxing":
            audio_files = list(re_audio_files.values())

    # menampilakn file audio
    if len(audio_files) > 0:
        for i, file in enumerate(audio_files):
            if st.button(f"Play {file}", key=file):
               
                play_audio(file)
    else:
        st.warning("No audio files available.")\

    # menampilkan peringatan jika file yang di minta tidak ada
    if not current_file and article_id:
        st.waarning(f"Warning: Audio file for article ID '{article_id}' not found.")

if __name__ == "__main__":
    main()