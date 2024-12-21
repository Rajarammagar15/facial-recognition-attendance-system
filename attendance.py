# attendance.py
import os
import cv2
import pandas as pd
from datetime import datetime
from deepface import DeepFace
import logging
from contextlib import redirect_stdout
import io

ATTENDANCE_FILE = "attendance.csv"
MODEL_DIR = "./models"
DB_PATH = "face_database"
os.environ["DEEPFACE_HOME"] = MODEL_DIR


def initialize_attendance_file():
    if not os.path.exists(ATTENDANCE_FILE):
        df = pd.DataFrame(columns=["Name", "Date", "Time"])
        df.to_csv(ATTENDANCE_FILE, index=False)


def mark_attendance(name):
    df = pd.read_csv(ATTENDANCE_FILE)
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    if not ((df["Name"] == name) & (df["Date"] == date)).any():
        new_entry = pd.DataFrame([[name, date, time]], columns=["Name", "Date", "Time"])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(ATTENDANCE_FILE, index=False)
        print(f"Attendance marked for {name} at {time}")
    else:
        print(f"{name} is already marked for today.")


def recognize_faces():
    initialize_attendance_file()
    cap = cv2.VideoCapture(0)
    print("Starting face recognition. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        try:
            with io.StringIO() as buf, redirect_stdout(buf):
                results = DeepFace.find(img_path=frame, db_path=DB_PATH, enforce_detection=False)

            if isinstance(results, list) and len(results) > 0 and not results[0].empty:
                df = results[0]
                name = df["identity"].iloc[0].split(os.path.sep)[-2]
                mark_attendance(name)
                cv2.putText(frame, name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                print("No match found.")
        except Exception as e:
            print(f"Error: {e}")

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
