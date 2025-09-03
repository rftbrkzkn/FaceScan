# Face Access System (LBPH)

This project is a simple **face recognition access system** using OpenCV’s LBPH Face Recognizer.  
It detects faces from a camera, recognizes known people, and logs access to an SQLite database.

## Features
- Modular structure (Camera, Detection, Recognition, Database, Utils)
- LBPH for fast CPU-based face recognition
- SQLite logging of recognized people
- Dataset-based training (`DataSet/Name/1.png`, `2.png`, ...)

## Project Structure
```
FaceAccessSystem/
│── main.py
├── Camera/
├── Detection/
├── Recognition/
├── DataBase/
├── Utils/
└── DataSet/
```

## Requirements
```
pip install opencv-contrib-python
```

##  Run
```
python main.py
```

Press `q` to quit.
