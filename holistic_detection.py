import cv2
import mediapipe as mp

# Initialize MediaPipe Holistic
mp_holistic = mp.solutions.holistic
mp_draw = mp.solutions.drawing_utils

holistic = mp_holistic.Holistic(
    static_image_mode=False,
    model_complexity=0,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera could not be opened!")
    exit()

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to read frame")
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    print("Before process")
    results = holistic.process(rgb)
    print("After process")

    # Draw Pose
    if results.pose_landmarks:
        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS
        )

    # Draw Left Hand
    if results.left_hand_landmarks:
        mp_draw.draw_landmarks(
            frame,
            results.left_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS
        )

    # Draw Right Hand
    if results.right_hand_landmarks:
        mp_draw.draw_landmarks(
            frame,
            results.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS
        )

    # Draw Face Mesh
    if results.face_landmarks:
        mp_draw.draw_landmarks(
            frame,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS
        )

    feedback = "Person Not Detected"
    color = (0, 0, 255)

    if results.pose_landmarks:

        landmarks = results.pose_landmarks.landmark

        left_shoulder = landmarks[mp_holistic.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_holistic.PoseLandmark.RIGHT_SHOULDER]
        nose = landmarks[mp_holistic.PoseLandmark.NOSE]

        shoulder_diff = abs(left_shoulder.y - right_shoulder.y)

        feedback = "Good Posture"
        color = (0, 255, 0)

        if shoulder_diff > 0.03:
            feedback = "Sit Straight"
            color = (0, 0, 255)

        elif nose.y > 0.55:
            feedback = "Raise Your Head"
            color = (0, 0, 255)

    cv2.putText(
        frame,
        feedback,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        2
    )
    print("Showing Camera")
    cv2.imshow("PresentIQ AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
holistic.close()
cv2.destroyAllWindows()