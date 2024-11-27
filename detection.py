from ultralytics import YOLO
import cv2

class YoloDetection:
    def __init__(self, model_name = "exp_yolo.pt"):
        # Download weights from https://github.com/ultralytics/ultralytics and change the path
        self.model = YOLO(f"./models/{model_name}")
        self.classNames = ["PMF 1", "PMN 2", "F1", "RGD 5", "RKG 3", "TM 62", "OZM 72", "MON 50"]

    def predict_and_detect(self, img, conf=0.5, rectangle_thickness=2, text_thickness=2):
        results = self.model.predict(img, conf=conf)
        for result in results:
            for box in result.boxes:
                cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                              (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), rectangle_thickness)
                cv2.putText(img, f"{self.classNames[int(box.cls[0])]}",
                            (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), text_thickness)
        return img, results

    def detect_from_image(self, image):
        result_img, _ = self.predict_and_detect(image, conf=0.5)
        return result_img

def gen_frames(detector: YoloDetection):
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (512, 512))
        if frame is None:
            break
        frame = detector.detect_from_image(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')