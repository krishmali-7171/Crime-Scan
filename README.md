# 🕵️‍♂️ Crime Scan – Face Recognition Criminal Detection System

**Crime Scan** is an AI-powered web application designed to detect and recognize faces by comparing them with a known criminal database using machine learning.  
This project was developed as a showcase of face recognition technology integrated with a web-based UI using Flask.

---

## 🔍 Features

- 📸 Upload or scan face images
- 🔐 Matches face against a criminal dataset
- 🎯 Displays matched identity if found
- 💾 Encodes and stores known faces using `pickle`
- 🧠 Powered by `face_recognition`, `OpenCV`, and `Flask`

---

## 🧰 Tech Stack

- Python 3  
- Flask – Backend  
- OpenCV – Image Processing  
- face_recognition – Face Encoding and Matching  
- HTML/CSS – Frontend

---

## 🚀 How It Works

1. Store known criminal faces in the `/dataset` folder  
2. Run `dataset_encode.py` to encode and save faces into `encodings.pickle`  
3. User uploads a face image via the web UI  
4. The app compares it with stored encodings using `face_recognition.compare_faces()`  
5. Outputs match result on the screen

---

## 📁 Project Structure
