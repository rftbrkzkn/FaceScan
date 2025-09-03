from Camera.camera_manager import CameraManager
from Detection.face_detector import FaceDetector
from Recognition.fast_recognizer import FastRecognizer
from DataBase.database_manager import DatabaseManager
from Utils.logger_util import Logger
import cv2
import os

def main():
    cam = CameraManager()
    detector = FaceDetector()
    recognizer = FastRecognizer()
    db = DatabaseManager()

    dataset_path = "DataSet"
    if os.path.exists(dataset_path):
        recognizer.train(dataset_path)
        Logger.log("Recognizer trained with dataset.")
    else:
        Logger.log("Dataset not found. Please create DataSet folder.", "error")
        return

    Logger.log("Face Access System (LBPH) started.")

    while True:
        frame = cam.get_frame()
        if frame is None:
            continue

        frame = cv2.resize(frame, (640, 480))
        faces = detector.detect_faces(frame)

        for (x, y, w, h) in faces:
            gray_face = cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2GRAY)
            gray_face = cv2.resize(gray_face, (200, 200))

            name, conf = recognizer.predict(gray_face)

            if conf > 80:
                name = "Unknown"

            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, f"{name} ({conf:.1f})", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            if name != "Unknown":
                db.add_log(name)
                Logger.log(f"{name} logged in with confidence {conf:.2f}")

        cv2.imshow("Access Control (LBPH)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
