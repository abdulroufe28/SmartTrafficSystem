import cv2
from ultralytics import YOLO
import time

# LIVE VEHICLE COUNT
live_vehicle_count = 0

# TRAFFIC DATA
traffic_density = "LOW"
signal_time = 10
emergency_status = "NORMAL"

# LOAD YOLO MODEL
model = YOLO("yolov8n.pt")

# VIDEO PATH
video_path = r"backend\datasets\traffic_sample.mp4"

# OPEN VIDEO
video = cv2.VideoCapture(video_path)


def generate_frames():

    global live_vehicle_count
    global traffic_density
    global signal_time
    global emergency_status

    frame_skip = 0

    while True:

        success, frame = video.read()

        if not success:

            video.set(cv2.CAP_PROP_POS_FRAMES, 0)

            continue

        # SKIP FRAMES FOR PERFORMANCE
        frame_skip += 1

        if frame_skip % 2 != 0:
            continue

        # YOLO DETECTION
        results = model(frame)

        vehicle_count = 0

        annotated_frame = frame.copy()

        for box in results[0].boxes:

            cls = int(box.cls[0])

            confidence = float(box.conf[0])

            class_name = model.names[cls]

            # VEHICLE FILTER
            if class_name in ["car", "bus", "truck", "motorcycle"]:

                display_name = class_name

                box_color = (0, 255, 0)

                # AMBULANCE SIMULATION
                if class_name == "bus" and confidence > 0.50:

                    display_name = "ambulance"

                    box_color = (0, 0, 255)

                    emergency_status = "ACTIVE"

                    signal_time = 5

                vehicle_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # DRAW BOX
                cv2.rectangle(
                    annotated_frame,
                    (x1, y1),
                    (x2, y2),
                    box_color,
                    2
                )

                # LABEL
                cv2.putText(
                    annotated_frame,
                    f"{display_name} {confidence:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    box_color,
                    2
                )

        # UPDATE LIVE COUNT
        live_vehicle_count = vehicle_count

        # TRAFFIC DENSITY LOGIC
        if vehicle_count <= 5:

            traffic_density = "LOW"

            signal_time = 10

        elif vehicle_count <= 15:

            traffic_density = "MEDIUM"

            signal_time = 20

        else:

            traffic_density = "HIGH"

            signal_time = 20

        # EMERGENCY LOGIC
        if vehicle_count > 15:

            emergency_status = "ACTIVE"

        else:

            emergency_status = "NORMAL"

        # SHOW VEHICLE COUNT
        cv2.putText(
            annotated_frame,
            f"Vehicles: {vehicle_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        # SHOW TRAFFIC DENSITY
        cv2.putText(
            annotated_frame,
            f"Density: {traffic_density}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            3
        )

        # SHOW SIGNAL TIME
        cv2.putText(
            annotated_frame,
            f"Signal Time: {signal_time}s",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 255),
            3
        )

        # SHOW EMERGENCY STATUS
        cv2.putText(
            annotated_frame,
            f"Emergency: {emergency_status}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            3
        )

        # CONVERT FRAME
        ret, buffer = cv2.imencode(
            '.jpg',
            annotated_frame
        )

        frame_bytes = buffer.tobytes()

        # STREAM FRAME
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame_bytes +
            b'\r\n'
        )


# SIGNAL PAGE VIDEO
def generate_slow_frames():

    slow_video = cv2.VideoCapture(
        r"backend\datasets\traffic_sample.mp4"
    )

    while True:

        success, frame = slow_video.read()

        if not success:

            slow_video.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )

            continue

        # SLOW DOWN VIDEO
        time.sleep(0.08)

        frame = cv2.resize(
            frame,
            (1000, 500)
        )

        ret, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        frame_bytes = buffer.tobytes()

        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' +
            frame_bytes +
            b'\r\n'
        )