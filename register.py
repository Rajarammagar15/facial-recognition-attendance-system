# register.py
import os
import cv2

DB_PATH = "face_database"


def register_user():
    cap = cv2.VideoCapture(0)
    user_name = input("Enter your name: ").strip()
    user_dir = os.path.join(DB_PATH, user_name.replace(" ", "_"))
    os.makedirs(user_dir, exist_ok=True)

    print(f"Starting registration for {user_name}. Capturing 50 images.")

    image_count = 0
    while image_count < 50:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow(f"Registration - Capturing Image {image_count + 1}/50", frame)

        # Automatically capture and save images
        image_path = os.path.join(user_dir, f"{user_name}_{image_count}.jpg")
        cv2.imwrite(image_path, frame)
        print(f"Image {image_count + 1} saved to {image_path}")
        image_count += 1

        # Show frame for a brief moment to simulate capturing interval
        cv2.waitKey(50)  # Wait for 100 milliseconds between captures

    cap.release()
    cv2.destroyAllWindows()
    print(f"Registration complete. {image_count} images saved for {user_name}.")
