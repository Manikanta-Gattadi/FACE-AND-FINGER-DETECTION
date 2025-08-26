import cv2
import mediapipe as mp

# Initialize Face Detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Video Capture
cap = cv2.VideoCapture(0)

# Full screen window
cv2.namedWindow("Face + Hand Gesture Recognition", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Face + Hand Gesture Recognition", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Finger tips landmark IDs
tip_ids = [4, 8, 12, 16, 20]
finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]

while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect Faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 0), 1)

    # Process Hands
    result = hands.process(img_rgb)
    total_fingers = 0
    hand_info = []  # Store hand labels, counts, and finger names for display

    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_index, hand_landmarks in enumerate(result.multi_hand_landmarks):
            lm_list = []
            h, w, c = frame.shape
            for id, lm in enumerate(hand_landmarks.landmark):
                lm_list.append((int(lm.x * w), int(lm.y * h)))

            # Get hand label (Left/Right)
            hand_label = result.multi_handedness[hand_index].classification[0].label

            fingers = []
            up_fingers = []

            # Thumb detection logic
            if hand_label == "Right":
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                    fingers.append(1)
                    up_fingers.append(finger_names[0])
                else:
                    fingers.append(0)
            else:  # Left Hand
                if lm_list[tip_ids[0]][0] < lm_list[tip_ids[0] - 1][0]:
                    fingers.append(1)
                    up_fingers.append(finger_names[0])
                else:
                    fingers.append(0)

            # Other fingers (Index, Middle, Ring, Pinky)
            for id in range(1, 5):
                if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id] - 2][1]:
                    fingers.append(1)
                    up_fingers.append(finger_names[id])
                else:
                    fingers.append(0)

            hand_fingers = fingers.count(1)
            total_fingers += hand_fingers

            # Store hand info
            hand_info.append((hand_label, hand_fingers, up_fingers))

            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display info on top-left corner
    cv2.putText(frame, f'Total Fingers: {total_fingers}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    y_offset = 70
    for hand_label, count, up_fingers in hand_info:
        cv2.putText(frame, f'{hand_label} Hand: {count}', (10, y_offset),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
        y_offset += 25
        
        finger_string = ", ".join(up_fingers)
        if finger_string:
            # Change font scale to 0.5 and color to red (0, 0, 255)
            cv2.putText(frame, f'Fingers Up: {finger_string}', (30, y_offset),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            y_offset += 25
        
        y_offset += 5 # Add some extra space between hands

    cv2.imshow("Face + Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
