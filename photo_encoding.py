import face_recognition
import os
import numpy as np

base_dir = 'known_faces'

def encode_and_save_face(image_path, encoding_path):
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    
    if face_encodings:
        np.save(encoding_path, face_encodings[0])
        print(f"Кодировка сохранена для {image_path}")
    else:
        print(f"Лицо не найдено на изображении {image_path}")

for group_name in os.listdir(base_dir):
    group_path = os.path.join(base_dir, group_name)
    if os.path.isdir(group_path):
        for student_name in os.listdir(group_path):
            student_path = os.path.join(group_path, student_name)
            if os.path.isdir(student_path):
                for filename in os.listdir(student_path):
                    if filename.endswith('.jpg') or filename.endswith('.png'):
                        image_path = os.path.join(student_path, filename)
                        encoding_path = os.path.join(student_path, f"{student_name}_encoding.npy")
                        encode_and_save_face(image_path, encoding_path)
