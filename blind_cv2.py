import cv2

# 영상 파일을 읽어옵니다.
video = cv2.VideoCapture("video.mp4")

# 영상에서 프레임 단위로 읽어옵니다.
while True:
    success, frame = video.read()

    # 영상이 끝나면 종료합니다.
    if not success:
        break

    # 얼굴 인식기를 생성합니다.
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # 이미지에서 얼굴을 찾습니다.
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5)

    # 얼굴이 찾아지지 않으면 원본 영상을 그대로 출력합니다.
    if len(faces) == 0:
        cv2.imshow("Frame", frame)
    else:
        # 얼굴이 찾아지면 얼굴 영역을 차단한 새로운 이미지를 생성합니다.
        face_mask = frame.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(face_mask, (x, y), (x+w, y+h), (0, 0, 0), -1)

        # 차단된 이미지를 출력합니다.
        cv2.imshow("Frame", face_mask)

    # 키 입력이 있을 때까지 기다립니다.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 영상 재생을 종료합니다.