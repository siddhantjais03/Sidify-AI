from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr
import threading
import webbrowser   # ✅ added
import SPOTIFY_3


class Music:
    def __init__(self):
        self.window = Tk()
        self.window.title("VOICE EMOTION MUSIC")
        self.window.state("zoomed")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        try:
            img = Image.open("images.jpeg")
            img = img.resize((width, height))
            self.bg = ImageTk.PhotoImage(img)
            Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.window.configure(bg="#222")

        frame = Frame(self.window, bg=self.window["bg"])
        frame.place(relx=0.5, rely=0.55, anchor="center")

        def btn(text, color, cmd, col):
            b = Label(frame, text=text, font=("Arial", 14, "bold"),
                      bg=color, fg="white", width=15, height=2, cursor="hand2")
            b.grid(row=0, column=col, padx=0, pady=0)
            b.bind("<Button-1>", lambda e: cmd())

        btn("Start Face", "#4CAF50", self.open_face, 0)
        btn("Speak 🎤", "#2196F3", self.start_thread, 1)
        btn("Dashboard", "#9C27B0", self.open_dash, 2)
        btn("Exit", "#f44336", self.window.quit, 3)

        self.label = Label(self.window, text="Ready...",
                           font=("Arial", 22, "bold"), bg="#222", fg="white")
        self.label.place(relx=0.5, rely=0.7, anchor="center")

        self.window.mainloop()

    def safe(self, msg):
        self.window.after(0, lambda: self.label.config(text=msg))

    def start_thread(self):
        threading.Thread(target=self.speak, daemon=True).start()

    # 🔥 FIXED SPEAK FUNCTION
    def speak(self):
        try:
            self.safe("Listening...")

            r = sr.Recognizer()

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)

            self.safe("Recognizing...")

            text = r.recognize_google(audio, language="en-IN").lower()

            print("You said:", text)

            if any(word in text for word in ["happy", "joy", "good", "great", "excited"]):
                emo = "happy"
            elif any(word in text for word in ["sad", "depressed", "cry", "alone"]):
                emo = "sad"
            elif any(word in text for word in ["angry", "mad", "frustrated"]):
                emo = "angry"
            else:
                emo = "neutral"

            self.safe(f"Emotion: {emo}")

            self.window.after(1000, lambda: self.open_music(emo))

        except sr.WaitTimeoutError:
            self.safe("No voice detected ❌")

        except sr.UnknownValueError:
            self.safe("Not understood ❌")

        except sr.RequestError:
            self.safe("Internet error ❌")

        except Exception as e:
            self.safe("Voice Error ❌")
            print(e)

            # ---------------- EMOTION DETECTION ----------------
            if "happy" in text:
                emo = "happy"
                link = "https://open.spotify.com/playlist/4IRfmPFaasC3otx3LDoSVr"

            elif "sad" in text:
                emo = "sad"
                link = "https://open.spotify.com/playlist/5iRglGOpok1GkpIH4XmP2k"

            elif "angry" in text:
                emo = "angry"
                link = "https://open.spotify.com/playlist/5qpcTVfuET01SiK1qbFp3U"

            elif "neutral" in text or "normal" in text:
                emo = "neutral"
                link = "https://open.spotify.com/playlist/0XLkFWhpn9GO2F2yFUgyxY"

            else:
                emo = "neutral"
                link = "https://open.spotify.com/playlist/0XLkFWhpn9GO2F2yFUgyxY"

            self.safe(f"Emotion: {emo}")

            # 🔥 OPEN SPOTIFY
            webbrowser.open(link)

            # 🔥 OPEN YOUR NEXT PAGE (same as before)
            self.window.after(1500, lambda: self.open_music(emo))

        except Exception as e:
            self.safe("Voice Error ❌")
            print(e)

    def open_music(self, emo):
        self.window.destroy()
        SPOTIFY_3.SongUI(emo)

    def open_face(self):
        self.window.destroy()
        from SPOTIFY_2 import Face
        Face()

    def open_dash(self):
        self.window.destroy()
        from SPOTIFY_4 import Dash
        Dash()


if __name__ == "__main__":
    Music()