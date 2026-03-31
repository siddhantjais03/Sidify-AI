from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

class Dash:
    def __init__(self):
        self.window = Tk()
        self.window.state("zoomed")
        self.window.title("Emotion Dashboard")

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        # Background
        try:
            img = Image.open("images.jpeg")
            img = img.resize((width, height))
            self.bg = ImageTk.PhotoImage(img)
            Label(self.window, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.window.configure(bg="#ffffff")

        # Title
        Label(
            self.window,
            text="Emotion Dashboard",
            font=("Arial", 30, "bold"),
            bg=self.window["bg"],
            fg="black"
        ).place(relx=0.5, rely=0.15, anchor="center")

        # Center Frame
        frame = Frame(self.window, bg=self.window["bg"])
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Buttons
        Button(frame, text="Daily", command=self.daily,
               width=20, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10, pady=10)

        Button(frame, text="Weekly", command=self.weekly,
               width=20, bg="#4CAF50", fg="white").grid(row=0, column=1, padx=10, pady=10)

        Button(frame, text="Monthly", command=self.monthly,
               width=20, bg="#4CAF50", fg="white").grid(row=1, column=0, padx=10, pady=10)

        Button(frame, text="Yearly", command=self.yearly,
               width=20, bg="#4CAF50", fg="white").grid(row=1, column=1, padx=10, pady=10)

        Button(frame, text="Export Excel", command=self.export_excel,
               width=20, bg="#2196F3", fg="white").grid(row=2, column=0, padx=10, pady=15)

        Button(frame, text="Export PDF", command=self.export_pdf,
               width=20, bg="#9C27B0", fg="white").grid(row=2, column=1, padx=10, pady=15)

        Button(frame, text="Back", command=self.back,
               width=20, bg="#f44336", fg="white").grid(row=3, column=0, columnspan=2, pady=20)

        self.window.mainloop()

    # ---------------- DB CONNECT ----------------
    def get_connection(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="sa123",
            database="emotion_music"
        )

    # ---------------- GRAPH ----------------
    def plot(self, query, title):
        try:
            conn = self.get_connection()
            df = pd.read_sql(query, conn)
            conn.close()

            if df.empty:
                print("No data found ❌")
                return

            plt.figure()
            plt.bar(df['emotion'], df['count'])
            plt.title(title)
            plt.xlabel("Emotion")
            plt.ylabel("Count")
            plt.show()

        except Exception as e:
            print("Graph Error:", e)

    # ---------------- BUTTON FUNCTIONS ----------------
    def daily(self):
        self.plot("""
            SELECT emotion, COUNT(*) as count
            FROM history
            WHERE DATE(timestamp) = CURDATE()
            GROUP BY emotion
        """, "Daily Emotion")

    def weekly(self):
        self.plot("""
            SELECT emotion, COUNT(*) as count
            FROM history
            WHERE timestamp >= CURDATE() - INTERVAL 7 DAY
            GROUP BY emotion
        """, "Weekly Emotion")

    def monthly(self):
        self.plot("""
            SELECT emotion, COUNT(*) as count
            FROM history
            WHERE YEAR(timestamp) = YEAR(CURDATE())
            AND MONTH(timestamp) = MONTH(CURDATE())
            GROUP BY emotion
        """, "Monthly Emotion")

    def yearly(self):
        self.plot("""
            SELECT emotion, COUNT(*) as count
            FROM history
            WHERE YEAR(timestamp) = YEAR(CURDATE())
            GROUP BY emotion
        """, "Yearly Emotion")

    # ---------------- EXPORT EXCEL ----------------
    def export_excel(self):
        try:
            conn = self.get_connection()
            df = pd.read_sql("SELECT * FROM history", conn)
            conn.close()

            if df.empty:
                print("No data ❌")
                return

            file = "emotion_report.xlsx"
            df.to_excel(file, index=False)
            print("Excel Exported ✅")
            os.startfile(file)

        except Exception as e:
            print("Excel Error:", e)

    # ---------------- EXPORT PDF ----------------
    def export_pdf(self):
        try:
            conn = self.get_connection()
            df = pd.read_sql("SELECT * FROM history", conn)
            conn.close()

            if df.empty:
                print("No data ❌")
                return

            from reportlab.platypus import SimpleDocTemplate, Table

            file = "emotion_report.pdf"
            data = [df.columns.tolist()] + df.values.tolist()

            pdf = SimpleDocTemplate(file)
            table = Table(data)
            pdf.build([table])

            print("PDF Exported ✅")
            os.startfile(file)

        except Exception as e:
            print("PDF Error:", e)

    # ---------------- BACK ----------------
    def back(self):
        self.window.destroy()
        # from SPOTIFY_1 import Music
        # Music()

# ---------------- MAIN ----------------
if __name__ == "__main__":
    Dash()