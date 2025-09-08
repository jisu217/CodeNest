# YOLO 웹캠 실시간 탐지 연습용 - 로컬 비디오 파일 사용

import cv2
from ultralytics import YOLO
import time
import os


# =============================================
# 2. 샘플 동영상 자동 다운로드 함수
# =============================================
def get_local_video_file():

    print("=== 로컬 비디오 파일 선택 ===")
    print("비디오 파일 경로를 입력하세요.")
    print("예시: C:/Videos/sample.mp4 또는 ./my_video.mp4")
    print("지원 형식: .mp4, .avi, .mov, .mkv, .wmv")

    while True:
        video_path = input("\n비디오 파일 경로: ").strip()

        # 따옴표 제거 (드래그&드롭 시 생기는 따옴표)
        video_path = video_path.strip('"').strip("'")

        if not video_path:
            print("경로를 입력해주세요!")
            continue

        if not os.path.exists(video_path):
            print(f"파일을 찾을 수 없습니다: {video_path}")
            print("다시 입력해주세요.")
            continue

        video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']
        if not any(video_path.lower().endswith(ext) for ext in video_extensions):
            print("지원하지 않는 파일 형식입니다.")
            print(f"지원 형식: {', '.join(video_extensions)}")
            continue

        test_cap = cv2.VideoCapture(video_path)
        if not test_cap.isOpened():
            print("비디오 파일을 열 수 없습니다. 파일이 손상되었거나 지원하지 않는 형식일 수 있습니다.")
            test_cap.release()
            continue

        fps = test_cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(test_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(test_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(test_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration = frame_count / fps if fps > 0 else 0

        print(f"\n✓ 비디오 파일 정보:")
        print(f"  - 해상도: {width}x{height}")
        print(f"  - FPS: {fps:.1f}")
        print(f"  - 총 프레임: {frame_count}")
        print(f"  - 길이: {duration:.1f}초")

        test_cap.release()
        return video_path


# =============================================
# 3. 개선된 실시간 탐지 코드
# =============================================

class RealTimeYOLO:
    def __init__(self, model_name='yolov8n.pt', confidence_threshold=0.5):
        """
        실시간 YOLO 탐지 클래스

        Args:
            model_name: 사용할 YOLO 모델 ('yolov8n.pt', 'yolov8s.pt', etc.)
            confidence_threshold: 탐지 신뢰도 임계값
        """
        self.model = YOLO(model_name)
        self.confidence_threshold = confidence_threshold
        self.fps_counter = 0
        self.start_time = time.time()

    def calculate_fps(self):
        """실제 FPS 계산"""
        self.fps_counter += 1
        elapsed_time = time.time() - self.start_time

        if elapsed_time >= 1.0:  # 1초마다 FPS 업데이트
            fps = self.fps_counter / elapsed_time
            self.fps_counter = 0
            self.start_time = time.time()
            return fps
        return None

    def detect_webcam(self, camera_index=0):
        cap = cv2.VideoCapture(camera_index)

        # 웹캠 설정 최적화
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)

        if not cap.isOpened():
            print("웹캠을 열 수 없습니다!")
            return

        print("웹캠 실시간 탐지 시작 (종료: 'q' 키)")
        current_fps = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                print("프레임을 읽을 수 없습니다!")
                break

            # YOLO 탐지 실행
            results = self.model(frame, conf=self.confidence_threshold, verbose=False)

            # 결과 시각화
            annotated_frame = results[0].plot()

            # FPS 계산 및 표시
            fps = self.calculate_fps()
            if fps is not None:
                current_fps = fps

            cv2.putText(annotated_frame, f'FPS: {current_fps:.1f}',
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

            # 탐지된 객체 수 표시
            num_detections = len(results[0].boxes) if results[0].boxes is not None else 0
            cv2.putText(annotated_frame, f'Objects: {num_detections}',
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

            # 화면 표시
            cv2.imshow('YOLO Real-time Detection', annotated_frame)

            # 종료 조건
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def detect_video_file(self, video_path, save_output=False, output_path=None):
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"비디오 파일을 열 수 없습니다: {video_path}")
            return

        # 비디오 정보
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        original_fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        print(f"비디오 파일 탐지 시작: {video_path}")
        print(f"총 프레임: {total_frames}, 원본 FPS: {original_fps:.1f}")
        print("종료: 'q' 키, 일시정지: 스페이스바")

        # 결과 영상 저장 설정
        out = None
        if save_output:
            if output_path is None:
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                output_path = f"yolo_result_{base_name}_{int(time.time())}.mp4"

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, original_fps, (width, height))
            print(f"결과 영상 저장 경로: {output_path}")

        frame_count = 0
        paused = False
        current_fps = 0

        while True:
            if not paused:
                ret, frame = cap.read()
                if not ret:
                    print("비디오 끝에 도달했습니다!")
                    break

                frame_count += 1

                # YOLO 탐지 실행
                results = self.model(frame, conf=self.confidence_threshold, verbose=False)

                # 결과 시각화
                annotated_frame = results[0].plot()

                # 정보 표시
                fps = self.calculate_fps()
                if fps is not None:
                    current_fps = fps

                # 상태 정보 오버레이
                info_text = [
                    f'FPS: {current_fps:.1f}',
                    f'Frame: {frame_count}/{total_frames}',
                    f'Progress: {frame_count / total_frames * 100:.1f}%'
                ]

                for i, text in enumerate(info_text):
                    cv2.putText(annotated_frame, text, (10, 30 + i * 25),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # 탐지된 객체 정보
                if results[0].boxes is not None:
                    for j, box in enumerate(results[0].boxes):
                        class_name = self.model.names[int(box.cls[0])]
                        confidence = float(box.conf[0])
                        cv2.putText(annotated_frame, f'{class_name}: {confidence:.2f}',
                                    (10, 120 + j * 20), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 255, 0), 1)

                # 결과 영상 저장
                if save_output and out is not None:
                    out.write(annotated_frame)

            # 화면 표시
            cv2.imshow('YOLO Video Detection', annotated_frame)

            # 키 입력 처리
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord(' '):  # 스페이스바로 일시정지/재생
                paused = not paused
                print("일시정지" if paused else "재생")

        cap.release()
        if out is not None:
            out.release()
            print(f"✓ 결과 영상 저장 완료: {output_path}")
        cv2.destroyAllWindows()

        return output_path if save_output else None


# =============================================
# 4. 다양한 탐지 모드 함수
# =============================================

def detection_with_tracking():
    """객체 탐지 + 추적"""
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    track_history = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model.track(frame, persist=True, verbose=False)

        if results[0].boxes is not None and results[0].boxes.id is not None:
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()

            for box, track_id in zip(boxes, track_ids):
                x, y, w, h = box
                center = (int(x), int(y))

                if track_id not in track_history:
                    track_history[track_id] = []
                track_history[track_id].append(center)

                if len(track_history[track_id]) > 30:
                    track_history[track_id].pop(0)

        annotated_frame = results[0].plot()

        for track_id, points in track_history.items():
            if len(points) > 1:
                for i in range(1, len(points)):
                    cv2.line(annotated_frame, points[i - 1], points[i],
                             (0, 255, 255), 2)

        cv2.imshow('YOLO Detection + Tracking', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def batch_process_videos(input_folder, output_folder=None):
    """폴더 내 모든 비디오 파일을 일괄 처리"""

    if output_folder is None:
        output_folder = os.path.join(input_folder, "yolo_results")

    os.makedirs(output_folder, exist_ok=True)

    # 지원하는 비디오 형식
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']

    # 비디오 파일 찾기
    video_files = []
    for file in os.listdir(input_folder):
        if any(file.lower().endswith(ext) for ext in video_extensions):
            video_files.append(file)

    if not video_files:
        print(f"폴더에서 비디오 파일을 찾을 수 없습니다: {input_folder}")
        return

    print(f"총 {len(video_files)}개의 비디오 파일을 처리합니다.")

    # YOLO 모델 초기화
    model = YOLO('yolov8n.pt')

    for i, filename in enumerate(video_files, 1):
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_folder, f"yolo_{base_name}.mp4")

        print(f"\n[{i}/{len(video_files)}] 처리 중: {filename}")

        try:
            # 비디오 처리
            cap = cv2.VideoCapture(input_path)
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            # 출력 비디오 설정
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

            frame_count = 0
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # YOLO 탐지
                results = model(frame, verbose=False)
                annotated_frame = results[0].plot()

                # 진행률 표시
                frame_count += 1
                if frame_count % 30 == 0:  # 30프레임마다 출력
                    progress = (frame_count / total_frames) * 100
                    print(f"  진행률: {progress:.1f}% ({frame_count}/{total_frames})")

                out.write(annotated_frame)

            cap.release()
            out.release()
            print(f"✓ 완료: {output_path}")

        except Exception as e:
            print(f"✗ 실패: {filename} - {e}")

    print(f"\n일괄 처리 완료! 결과 폴더: {output_folder}")


def save_detection_report(video_path, output_dir=None):
    """탐지 결과를 CSV 리포트로 저장"""

    if output_dir is None:
        output_dir = os.path.dirname(video_path)

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    report_path = os.path.join(output_dir, f"detection_report_{base_name}.csv")

    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(video_path)

    # CSV 파일 생성
    import csv
    with open(report_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['frame_number', 'timestamp', 'object_class', 'confidence', 'x1', 'y1', 'x2', 'y2']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        frame_number = 0
        fps = cap.get(cv2.CAP_PROP_FPS)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_number += 1
            timestamp = frame_number / fps

            # YOLO 탐지
            results = model(frame, verbose=False)

            if results[0].boxes is not None:
                for box in results[0].boxes:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    confidence = float(box.conf[0])
                    class_name = model.names[int(box.cls[0])]

                    writer.writerow({
                        'frame_number': frame_number,
                        'timestamp': f"{timestamp:.2f}",
                        'object_class': class_name,
                        'confidence': f"{confidence:.3f}",
                        'x1': f"{x1:.1f}",
                        'y1': f"{y1:.1f}",
                        'x2': f"{x2:.1f}",
                        'y2': f"{y2:.1f}"
                    })

            if frame_number % 100 == 0:
                print(f"리포트 생성 중... 프레임: {frame_number}")

    cap.release()
    print(f"✓ 탐지 리포트 저장 완료: {report_path}")
    return report_path
    """특정 객체 개수 세기"""
    model = YOLO('yolov8n.pt')
    cap = cv2.VideoCapture(0)

    # 관심 있는 클래스들
    target_classes = ['person', 'car', 'bicycle', 'motorbike']

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)
        annotated_frame = results[0].plot()

        # 클래스별 개수 계산
        if results[0].boxes is not None:
            class_counts = {}
            for box in results[0].boxes:
                class_name = model.names[int(box.cls[0])]
                if class_name in target_classes:
                    class_counts[class_name] = class_counts.get(class_name, 0) + 1

            # 개수 정보 표시
            y_offset = 30
            for class_name, count in class_counts.items():
                text = f'{class_name}: {count}'
                cv2.putText(annotated_frame, text, (10, y_offset),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                y_offset += 30

        cv2.imshow('YOLO Object Counting', annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


# =============================================
# 5. 사용 예시 및 실행 코드
# =============================================

if __name__ == "__main__":
    # YOLO 탐지기 초기화
    detector = RealTimeYOLO(model_name='yolov8n.pt', confidence_threshold=0.3)

    print("\n=== 사용 가능한 모드 ===")
    print("1. 웹캠 실시간 탐지")
    print("2. 로컬 비디오 파일 탐지 (화면 보기만)")
    print("3. 로컬 비디오 파일 탐지 + 결과 영상 저장")
    print("4. 폴더 내 모든 비디오 일괄 처리")
    print("5. 탐지 결과 CSV 리포트 생성")
    print("6. 객체 추적 모드 (웹캠)")
    print("7. 객체 개수 세기 모드 (웹캠)")

    mode = input("\n모드를 선택하세요 (1-7): ")

    if mode == '1':
        # 웹캠 실시간 탐지
        detector.detect_webcam()

    elif mode == '2':
        # 로컬 비디오 파일 탐지 (저장 안함)
        video_path = get_local_video_file()
        if video_path:
            print(f"\n비디오 분석을 시작합니다: {os.path.basename(video_path)}")
            print("조작법:")
            print("  - 'q': 종료")
            print("  - 스페이스바: 일시정지/재생")
            input("엔터를 눌러 시작하세요...")
            detector.detect_video_file(video_path, save_output=False)

    elif mode == '3':
        # 로컬 비디오 파일 탐지 + 결과 저장
        video_path = get_local_video_file()
        if video_path:
            # 저장 경로 설정
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            default_output = f"yolo_result_{base_name}_{int(time.time())}.mp4"

            print(f"\n기본 저장 경로: {default_output}")
            custom_path = input("다른 경로를 원하면 입력하세요 (엔터: 기본값 사용): ").strip()
            output_path = custom_path if custom_path else default_output

            print(f"\n비디오 분석 및 저장을 시작합니다: {os.path.basename(video_path)}")
            print(f"결과 저장 경로: {output_path}")
            print("조작법:")
            print("  - 'q': 종료")
            print("  - 스페이스바: 일시정지/재생")
            input("엔터를 눌러 시작하세요...")

            saved_path = detector.detect_video_file(video_path, save_output=True, output_path=output_path)
            if saved_path:
                print(f"\n🎉 분석 완료! 결과 영상이 저장되었습니다:")
                print(f"📁 {os.path.abspath(saved_path)}")

    elif mode == '4':
        # 폴더 내 모든 비디오 일괄 처리
        folder_path = input("비디오 파일들이 있는 폴더 경로를 입력하세요: ").strip().strip('"').strip("'")

        if os.path.exists(folder_path):
            output_folder = input("결과 저장 폴더 (엔터: 자동 생성): ").strip()
            output_folder = output_folder if output_folder else None

            print(f"\n폴더 내 모든 비디오 파일을 처리합니다...")
            print("이 작업은 시간이 오래 걸릴 수 있습니다.")
            confirm = input("계속하시겠습니까? (y/N): ")

            if confirm.lower() == 'y':
                batch_process_videos(folder_path, output_folder)
        else:
            print("존재하지 않는 폴더입니다!")

    elif mode == '5':
        # 탐지 결과 CSV 리포트 생성
        video_path = get_local_video_file()
        if video_path:
            print(f"\n탐지 결과 리포트를 생성합니다: {os.path.basename(video_path)}")
            print("이 작업은 시간이 걸릴 수 있습니다...")

            report_path = save_detection_report(video_path)
            print(f"\n📊 리포트 생성 완료!")
            print(f"📁 {os.path.abspath(report_path)}")

    elif mode == '6':
        # 객체 추적 모드
        print("웹캠을 사용한 객체 추적을 시작합니다...")
        detection_with_tracking()

    elif mode == '7':
        # 객체 개수 세기 모드
        print("웹캠을 사용한 객체 개수 세기를 시작합니다...")
        detection_with_counting()

    else:
        print("잘못된 선택입니다!")
