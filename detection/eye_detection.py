import cv2
import os
import time

from alerts.alert_system import play_alarm


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASCADE_PATH = os.path.join(BASE_DIR, "haarcascade_eye.xml")

eye_cascade = cv2.CascadeClassifier(CASCADE_PATH)

if eye_cascade.empty():
    raise RuntimeError(f"Could not load Haar Cascade: {CASCADE_PATH}")


start_time = None
alert_triggered = False

FIXATION_THRESHOLD = 3  # seconds


def process_frame(frame):

    global start_time, alert_triggered

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in eyes:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    if len(eyes) >= 2:

        if start_time is None:
            start_time = time.time()

        else:
            duration = time.time() - start_time

            cv2.putText(
                frame,
                f"Gaze Time: {duration:.1f}s",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2
            )

            if duration > FIXATION_THRESHOLD and not alert_triggered:

                cv2.putText(
                    frame,
                    "Eyes fixed too long!",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                play_alarm()
                alert_triggered = True

    else:
        start_time = None
        alert_triggered = False

    return frame