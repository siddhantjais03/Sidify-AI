import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tkinter import *
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
import threading
import time
import SPOTIFY_3 as Music3


class Face:
    def __init__(self):
        self.window = Tk()
        self.window.title("FACE DETECTION")
        self.window.state("zoomed")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        # ---------------- BACKGROUND ----------------
        try:
            img = Image.open("images.jpeg")
            img = img.resize((width, height))
            self.bg = ImageTk.PhotoImage(img)

            Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.window.configure(bg="#121212")

        # ---------------- TITLE ----------------
        self.label_text = Label(
            self.window,
            text="Detecting Emotion...",
            font=("Arial", 22, "bold"),
            bg="#000000",
            fg="white"
        )
        self.label_text.place(relx=0.5, rely=0.1, anchor="center")

        # ---------------- CAMERA ----------------
        self.canvas = Label(self.window, bd=0)
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.cap = cv2.VideoCapture(0)

        if not self.cap.isOpened():
            self.label_text.config(text="Camera not found ❌")
            return

        self.running = True

        # camera preview
        threading.Thread(target=self.show_camera, daemon=True).start()

        # auto detect
        threading.Thread(target=self.detect_emotion, daemon=True).start()

        self.window.mainloop()

    # ---------------- CAMERA PREVIEW ----------------
    def show_camera(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.canvas.config(image=img)
            self.canvas.image = img

    # ---------------- DETECTION ----------------
    def detect_emotion(self):
        time.sleep(4)

        ret, frame = self.cap.read()

        if not ret:
            emotion = "neutral"
        else:
            try:
                result = DeepFace.analyze(
                    frame,
                    actions=['emotion'],
                    enforce_detection=False
                )
                emotion = result[0]['dominant_emotion']
            except:
                emotion = "neutral"

        self.running = False
        self.cap.release()

        self.window.after(0, lambda: self.open_music(emotion))

    # ---------------- NEXT SCREEN ----------------
    def open_music(self, emotion):
        self.window.destroy()
        Music3.SongUI(emotion)


if __name__ == "__main__":
    Face()