import cv2
import face_recognition

# 웹캠 장치 인덱스(0부터 시작)
WEBCAM_DEVICE_INDEX = 0

# 웹캠 연결
webcam = cv2.VideoCapture(WEBCAM_DEVICE_INDEX)

while True:
    # 이미지 읽기
    _, frame = webcam.read()
    
    # 얼굴 위치 검출
    face_locations = face_recognition.face_locations(frame)
    
    # 얼굴이 찾아지지 않으면 원본 영상을 그대로 출력합니다.
    if len(face_locations) == 0:
        cv2.imshow("Webcam", frame)
    else:
        # 얼굴 위치를 그려줍니다.
        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), -1)
        # for top, right, bottom, left in face_locations:
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        
        # 얼굴 위치가 검출된 이미지 미리보기
        cv2.imshow('Webcam', frame)
        
        # q 키가 입력되면 종료합니다.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 웹캠 연결 해제
webcam.release()

# 미리보기 창 종료
cv2.destroyAllWindows()