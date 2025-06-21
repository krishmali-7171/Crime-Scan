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
## 📎 GitHub Repository

🔗 [https://github.com/krishmali-7171/Crime-Scan](https://github.com/krishmali-7171/Crime-Scan)

---

## 📅 Project Info

- **Project Name**: Crime Scan  
- **Developer**: Krish Mali  
- **Tech Focus**: Face Recognition, Flask, Web Security  
- **Duration**: June 2025  
- **Hosted**: Localhost (Can be deployed on Render or Railway)

---

## 🙌 Acknowledgements

Special thanks to:
- 🧠 [`face_recognition`](https://github.com/ageitgey/face_recognition) – For the core face matching logic  
- 💡 The open-source Python community  
- 🔬 Tutorials by *Murtaza’s Workshop* and other helpful content creators  
- 👨‍🏫 My mentors at [Prodigy InfoTech](https://prodigyinfotech.dev/) for fueling my learning path

---

## 👋 Connect With Me

- 🔗 [LinkedIn – Krish Mali](https://linkedin.com/in/krishmali)  
- 💻 [GitHub – krishmali-7171](https://github.com/krishmali-7171)  

---

> 🔐 **Note**: This project is for educational purposes and not intended for use in actual law enforcement or surveillance systems.
