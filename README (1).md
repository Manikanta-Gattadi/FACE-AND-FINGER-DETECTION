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

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/c38820d4-f8c5-4df3-9ce3-d4ccf3b39bca" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/002e5f46-bbce-4951-b82e-8e352031db40" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/5d2cceb8-f2b1-4aa9-b166-640ea404371a" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/06f10b86-9ad0-45a6-a36b-09248a97499e" />

## Controls
- Press `q` to exit the application.

## Future Improvements
- Add gesture-based controls (e.g., volume control).
- Integrate sign language recognition.
- Optimize detection for low-light conditions.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
