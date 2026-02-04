import streamlit as st
import base64
from pathlib import Path

def global_music():
    if "music_initialized" not in st.session_state:
        st.session_state.music_initialized = True

        songs = [
            "assets/songs/Dandelions.m4a",
            "assets/songs/Lifetime.mp3",
            "assets/songs/Lucky.mp3",
            "assets/songs/Partilhar.m4a"
        ]

        playlist = []
        for song in songs:
            with open(song, "rb") as f:
                playlist.append(
                    "data:audio/mp3;base64," +
                    base64.b64encode(f.read()).decode()
                )

        html = f"""
        <audio id="player"></audio>

        <script>
        if (!window.weddingPlayer) {{
            window.weddingPlayer = document.getElementById("player");
            window.weddingPlaylist = {playlist};
            window.weddingIndex = 0;

            function playMusic() {{
                weddingPlayer.src = weddingPlaylist[weddingIndex];
                weddingPlayer.volume = 0.4;
                weddingPlayer.play();
            }}

            weddingPlayer.onended = function() {{
                weddingIndex = (weddingIndex + 1) % weddingPlaylist.length;
                playMusic();
            }}

            window.toggleWeddingMusic = function() {{
                if (weddingPlayer.paused) {{
                    playMusic();
                }} else {{
                    weddingPlayer.pause();
                }}
            }}
        }}
        </script>

        <div style="text-align:center; margin-top:20px;">
            <button onclick="toggleWeddingMusic()"
            style="
                background: transparent;
                border: none;
                font-family: 'Cormorant Garamond';
                font-size: 14px;
                letter-spacing: 0.3em;
                cursor: pointer;
            ">
                🎵 Música
            </button>
        </div>
        """

        st.components.v1.html(html, height=100)