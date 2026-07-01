import cv2
import mediapipe as mp

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open Camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:

    success, frame = cap.read()

    if not success:
        break

    # Flip for mirror view
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process Pose
    results = pose.process(rgb)

    if results.pose_landmarks:

        # Draw skeleton
        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        landmarks = results.pose_landmarks.landmark

        nose = landmarks[mp_pose.PoseLandmark.NOSE]

        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        # Default
        feedback = "Good Posture"
        color = (0, 255, 0)

        shoulder_diff = abs(left_shoulder.y - right_shoulder.y)
        shoulder_center_y = (left_shoulder.y + right_shoulder.y) / 2
        shoulder_center_x = (left_shoulder.x + right_shoulder.x) / 2

        # Head down
        if nose.y > shoulder_center_y - 0.15:
            feedback = "Raise Your Head"
            color = (0, 0, 255)

        # Lean left
        elif nose.x < shoulder_center_x - 0.10:
            feedback = "Leaning Left"
            color = (0, 0, 255)

        # Lean right
        elif nose.x > shoulder_center_x + 0.10:
            feedback = "Leaning Right"
            color = (0, 0, 255)

        # Shoulder tilt
        elif shoulder_diff > 0.05:
            feedback = "Sit Straight"
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

    cv2.imshow("PresentIQ AI - Posture Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
pose.close()
cv2.destroyAllWindows()