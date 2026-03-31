import tkinter as tk
from PIL import Image, ImageTk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import mysql.connector
import webbrowser
import time

# ================== DATABASE FUNCTION ==================
def save_to_db(emotion):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sa123",
            database="emotion_music"
        )
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO history (emotion, song_name, artist, timestamp)
        VALUES (%s, %s, %s, NOW())
        """, (emotion, "Auto Song", "Spotify"))

        conn.commit()
        conn.close()

        print("✅ Saved to DB:", emotion)

    except Exception as e:
        print("DB Error:", e)


# ================== SPOTIFY AUTH ==================
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state"
))

# ================== PLAYLIST ==================
EMOTION_PLAYLISTS = {
    "happy": "spotify:playlist:4IRfmPFaasC3otx3LDoSVr",
    "sad": "spotify:playlist:5iRglGOpok1GkpIH4XmP2k",
    "angry": "spotify:playlist:5qpcTVfuET01SiK1qbFp3U",
    "neutral": "spotify:playlist:0XLkFWhpn9GO2F2yFUgyxY"
}


# ================== MAIN CLASS ==================
class SongUI:
    def __init__(self, emotion):

        # 🔥 NORMALIZE EMOTION
        emotion = str(emotion).lower().strip()

        if "happy" in emotion:
            self.emotion = "happy"
        elif "sad" in emotion:
            self.emotion = "sad"
        elif "angry" in emotion:
            self.emotion = "angry"
        else:
            self.emotion = "neutral"

        print("🎯 Final Emotion:", self.emotion)

        self.window = tk.Tk()
        self.window.title("Music Player")
        self.window.state("zoomed")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        # Background
        try:
            img = Image.open("images.jpeg")
            img = img.resize((width, height))
            self.bg = ImageTk.PhotoImage(img)
            tk.Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.window.configure(bg="#ffffff")

        # Title
        tk.Label(
            self.window,
            text=f"{self.emotion.upper()} PLAYLIST",
            font=("Arial", 32, "bold"),
            bg=self.window["bg"],
            fg="black"
        ).place(relx=0.5, rely=0.35, anchor="center")

        # Play Button
        tk.Button(
            self.window,
            text="▶ Play Music",
            font=("Arial", 16, "bold"),
            bg="#1DB954",
            fg="white",
            width=20,
            height=2,
            bd=0,
            cursor="hand2",
            command=self.play_music
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Back Button
        tk.Button(
            self.window,
            text="Back",
            font=("Arial", 12, "bold"),
            bg="#f44336",
            fg="white",
            bd=0,
            cursor="hand2",
            command=self.back
        ).place(relx=0.5, rely=0.6, anchor="center")

        # 🔥 AUTO PLAY (DELAYED)
        self.window.after(1500, self.play_music)

        self.window.mainloop()

    # ================== PLAY FUNCTION ==================
    def play_music(self):
        try:
            print("🎯 Playing Emotion:", self.emotion)

            # 🔥 SAVE TO DB
            save_to_db(self.emotion)

            # 🔥 1. OPEN SPOTIFY UI
            playlist_id = EMOTION_PLAYLISTS[self.emotion].split(":")[-1]
            webbrowser.open(f"https://open.spotify.com/playlist/{playlist_id}")

            time.sleep(3)  # ⏳ important delay

            # 🔥 2. GET DEVICES
            devices = sp.devices()['devices']
            print("📱 Devices:", devices)

            if not devices:
                print("❌ Open Spotify app and play once manually")
                return

            device_id = devices[0]['id']

            # 🔥 3. FORCE DEVICE ACTIVE
            sp.transfer_playback(device_id, force_play=True)

            time.sleep(1)

            # 🔥 4. PLAY MUSIC
            sp.start_playback(
                device_id=device_id,
                context_uri=EMOTION_PLAYLISTS[self.emotion]
            )

            print("✅ Spotify Open + Auto Play Working")

        except Exception as e:
            print("❌ ERROR:", e)

    # ================== BACK ==================
    def back(self):
        self.window.destroy()
        from SPOTIFY_1 import Music
        Music()