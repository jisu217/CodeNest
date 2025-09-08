# 기본 import
import cv2
from ultralytics import YOLO
import numpy as np

# YOLOv8 모델 로드 (사전 훈련된 모델)
model = YOLO('yolov8n.pt')  # nano 버전 (가장 빠름)


# 이미지에서 객체 탐지
def detect_objects_image(image_path):

    image = cv2.imread(image_path)

    results = model(image)

    annotated_image = results[0].plot()

    for result in results:
        boxes = result.boxes
        if boxes is not None:
            for box in boxes:
                # 바운딩 박스 좌표
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                # 신뢰도
                confidence = box.conf[0].cpu().numpy()

                class_id = int(box.cls[0].cpu().numpy())

                class_name = model.names[class_id]

                print(f"탐지된 객체: {class_name}, 신뢰도: {confidence:.2f}")

    # 결과 이미지 저장
    cv2.imwrite('result.jpg', annotated_image)
    return annotated_image


# 사용 예시
result_image = detect_objects_image('practice.jpg')