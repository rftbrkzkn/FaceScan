import cv2
import os
import numpy as np

class FastRecognizer:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.label_map = {}

    def train(self, dataset_path):
        faces, labels = [], []
        label_id = 0
        for person in os.listdir(dataset_path):
            person_path = os.path.join(dataset_path, person)
            self.label_map[label_id] = person
            for file in os.listdir(person_path):
                img_path = os.path.join(person_path, file)
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if img is None:
                    print(f"[WARNING] Could not read {img_path}, skipping...")
                    continue
                img = cv2.resize(img, (200, 200))
                faces.append(img)
                labels.append(label_id)
            label_id += 1
        if len(faces) == 0:
            raise ValueError("No valid images found in dataset!")
        self.recognizer.train(faces, np.array(labels))

    def predict(self, face_crop):
        label, confidence = self.recognizer.predict(face_crop)
        return self.label_map.get(label, "Unknown"), confidence
