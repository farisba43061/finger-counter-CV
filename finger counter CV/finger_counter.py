import cv2
import mediapipe as mp

# Open the computer camera
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open the camera.")
    exit()

# MediaPipe utilities
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Create the hand detector
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Fingertip landmark IDs
tip_ids = [4, 8, 12, 16, 20]

print("Finger Counter Started")
print("Press Q or ESC to quit")

while True:

    success, frame = camera.read()

    if not success:
        break

    # Flip the image like a mirror
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb)

    fingers = []

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            # Draw the hand skeleton
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand.landmark

            # Thumb
            if landmarks[4].x < landmarks[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other four fingers
            for tip in tip_ids[1:]:

                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

    finger_count = fingers.count(1)

    # Display the finger count
    cv2.putText(
        frame,
        f"Fingers: {finger_count}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Finger Counter", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:
        break

camera.release()
cv2.destroyAllWindows()
hands.close()