<h1>Multi Landmarks Tracking with OpenCV and Mediapipe</h1>

<h2>Overview</h2>
<p>This Python script utilizes the Mediapipe library to perform multi-landmark tracking in real-time. It incorporates three main components: Pose Estimation, Face Detection, and Hand Tracking. The script captures video from the webcam, overlays detected landmarks on the face, hands, and human pose, and displays the result in a resizable window.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#understanding-the-script">Understanding the Script</a>
        <ul>
            <li><a href="#components">Components</a></li>
            <li><a href="#functions">Functions</a></li>
            <li><a href="#propagating-poses">Propagating Poses</a></li>
        </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.x</li>
    <li>OpenCV (<code>pip install opencv-python</code>)</li>
    <li>Mediapipe (<code>pip install mediapipe</code>)</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/Mayur-ingole/Multi-Landmark-Tracking.git
cd Multi-Landmarks-Tracking
</code></pre>

<ol start="2">
    <li>Install the required dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="3">
    <li>Run the script:</li>
</ol>

<pre><code>python Multi_Landmarks_Tracking.py
Press 'q' to exit the application.
</code></pre>

<h1>Features</h1>
<ul>
    <li><strong>Pose Estimation:</strong> Tracks the human body pose.</li>
    <li><strong>Face Detection:</strong> Detects and tracks faces in the video stream.</li>
    <li><strong>Hand Tracking:</strong> Tracks hand landmarks and connections.</li>
</ul>

<h1>Understanding the Script</h1>

<h2>Components</h2>
<ul>
    <li><strong>Pose Estimation (mp_pose):</strong> Utilizes the Mediapipe Pose model to estimate human body pose, including landmark locations for various body parts.</li>
    <li><strong>Face Detection (mp_face):</strong> Employs the Mediapipe Face Detection model to detect and track faces in the video stream. It extracts bounding box coordinates for each detected face.</li>
    <li><strong>Hand Tracking (mp_hands):</strong> Uses the Mediapipe Hands model to track hand landmarks and connections. It provides coordinates for each hand landmark and visualizes connections between them.</li>
</ul>

<h2>Functions</h2>
<ul>
    <li><strong>estimate_pose(frame):</strong> Estimates the pose landmarks in a single frame using the Mediapipe Pose model.</li>
    <li><strong>estimate_face(frame):</strong> Estimates the face landmarks in a single frame using the Mediapipe Face Detection model.</li>
    <li><strong>estimate_hands(frame):</strong> Estimates the hand landmarks in a single frame using the Mediapipe Hands model.</li>
    <li><strong>draw_face_landmarks(frame, landmarks):</strong> Draws bounding boxes around detected faces on the frame.</li>
    <li><strong>draw_hand_landmarks(frame, landmarks):</strong> Draws hand landmarks and connections on the frame using Mediapipe drawing utilities.</li>
    <li><strong>draw_landmarks(frame, landmarks):</strong> Draws pose landmarks on the frame using Mediapipe drawing utilities.</li>
</ul>

<h2>Propagating Poses</h2>
<ul>
    <li><strong>propagate_pose(prev_pose, current_pose):</strong> Propagates poses from the previous frame to the current frame. If the previous pose is not available, it returns the current pose; otherwise, it averages the previous and current poses.</li>
    <li><strong>propagate_poses(frames):</strong> Propagates poses across frames. It estimates poses for each frame, propagates them based on the previous frame's pose, and visualizes face and hand landmarks.</li>
</ul>

<h1>Contributing</h1>
<p>Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.</p>

<h1>License</h1>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

</body>
</html>
