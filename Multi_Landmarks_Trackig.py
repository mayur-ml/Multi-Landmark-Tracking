import cv2
import mediapipe as mp

# Initialize Mediapipe Pose, Face, and Hands models
mp_pose = mp.solutions.pose
mp_face = mp.solutions.face_detection
mp_hands = mp.solutions.hands

pose = mp_pose.Pose()
face = mp_face.FaceDetection(min_detection_confidence=0.5)
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Create a drawing utility
mp_drawing = mp.solutions.drawing_utils

# Function to estimate pose in a single frame
def estimate_pose(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_frame)
    landmarks = results.pose_landmarks
    return landmarks

# Function to estimate face landmarks in a single frame
def estimate_face(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face.process(rgb_frame)
    landmarks = results.detections
    return landmarks

# Function to estimate hand landmarks in a single frame
def estimate_hands(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    landmarks = results.multi_hand_landmarks
    return landmarks

# Function to draw face landmarks on the frame
def draw_face_landmarks(frame, landmarks):
    if landmarks:
        for detection in landmarks:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)

# Function to draw hand landmarks on the frame
def draw_hand_landmarks(frame, landmarks):
    if landmarks:
        for hand_landmarks in landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

# Function to draw pose landmarks on the frame
def draw_landmarks(frame, landmarks):
    if landmarks:
        mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS)

# Function to propagate poses from the previous frame to the current frame
def propagate_pose(prev_pose, current_pose):
    if prev_pose is None:
        return current_pose
    else:
        return (prev_pose + current_pose) / 2.0

# Function to propagate poses across frames
def propagate_poses(frames):
    all_poses = []
    for frame in frames:
        current_pose = estimate_pose(frame)
        current_face = estimate_face(frame)
        current_hands = estimate_hands(frame)

        if not all_poses:
            all_poses.append(current_pose)
        else:
            propagated_pose = propagate_pose(all_poses[-1], current_pose)
            all_poses.append(propagated_pose)

        draw_face_landmarks(frame, current_face)
        draw_hand_landmarks(frame, current_hands)

    return all_poses

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_pose = estimate_pose(frame)
    current_face = estimate_face(frame)
    current_hands = estimate_hands(frame)

    draw_landmarks(frame, current_pose)
    draw_face_landmarks(frame, current_face)
    draw_hand_landmarks(frame, current_hands)

    # Display the frame with a larger window size
    cv2.imshow('Multi-Landmark Tracking', cv2.resize(frame, (1024, 720)))


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
