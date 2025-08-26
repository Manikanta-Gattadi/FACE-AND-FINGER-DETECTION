# Face and Finger Detection using OpenCV & MediaPipe

## Project Overview
This project implements **real-time face detection and finger counting** using **OpenCV** for face recognition and **Google's MediaPipe** for hand landmark detection.  
The application captures video from the webcam, detects faces, identifies left/right hands, and counts the number of fingers raised for each hand.  

## Features
- Face Detection using Haar Cascade Classifier.
- Hand Gesture Recognition using MediaPipe Hands solution.
- Finger Counting Logic for both Left and Right hands.
- Real-time Video Stream with detection overlays.
- Displays:
  - Total Fingers Raised
  - Left/Right Hand Labels
  - Specific Fingers Raised

## Technologies Used
- Python 3
- OpenCV
- MediaPipe

## Project Structure
```
├── face and finger detection.py    # Main Python script
```

## How It Works
1. Capture video using OpenCV.
2. Detect faces with Haar Cascade Classifier.
3. Detect hands & landmarks using MediaPipe.
4. Apply logic to count raised fingers:
   - Thumb detection is based on X-coordinates (left/right hand orientation).
   - Other fingers are based on Y-coordinate comparison.
5. Display results on the live feed.

## Installation and Setup
1. Clone the Repository
   ```bash
   git clone https://github.com/your-username/face-finger-detection.git
   cd face-finger-detection
   ```
2. Install Dependencies
   ```bash
   pip install opencv-python mediapipe
   ```
3. Run the Application
   ```bash
   python "face and finger detection.py"
   ```

## Output Example
The program displays:
- A rectangle around the face.
- Hand landmarks connected with lines.
- Finger count and names displayed on the top-left corner.

<img width="1106" height="636" alt="Image" src="https://github.com/user-attachments/assets/a02c86ca-c28c-40b8-829e-ad4b9bb1f876" />

<img width="1114" height="616" alt="Image" src="https://github.com/user-attachments/assets/52b07e78-5f08-483a-adf8-bab59d242021" />

<img width="1110" height="617" alt="Image" src="https://github.com/user-attachments/assets/ea8c500c-5d67-4718-914d-90ab4c75321d" />

<img width="1114" height="627" alt="Image" src="https://github.com/user-attachments/assets/6e1fc79f-ad48-4cc1-a0a1-9168bc1955fc" />

## Controls
- Press `q` to exit the application.

## Future Improvements
- Add gesture-based controls (e.g., volume control).
- Integrate sign language recognition.
- Optimize detection for low-light conditions.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
