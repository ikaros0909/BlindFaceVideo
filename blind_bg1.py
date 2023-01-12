# Step 1: import necessary libraries
import cv2
import numpy as np

# Step 2: Load the background removal model
model = cv2.dnn.readNetFromDeepLabv3('path/to/model')

# Step 3: Open the webcam
cap = cv2.VideoCapture(0) # 0 means the default camera

while True:
    # Step 4: Capture the frame from the webcam
    ret, frame = cap.read()

    # Step 5: Run the frame through the background removal model
    blob = cv2.dnn.blobFromImage(frame, size=(1024, 1024), ddepth=cv2.CV_32F)
    model.setInput(blob)
    output = model.forward()

    # Step 6: Extract the object from the output
    object_mask = output[0, 0, :, :]
    object_mask = cv2.resize(object_mask, (frame.shape[1], frame.shape[0]))
    object_mask = np.array(object_mask > 0.5, dtype=np.uint8)

    # Step 7: Replace the background with the desired image
    background = cv2.imread('img/yonsei.jpg')
    background = cv2.resize(background, (frame.shape[1], frame.shape[0]))
    object_mask_3_channels = cv2.merge([object_mask, object_mask, object_mask])
    background = background * object_mask_3_channels + frame * (1 - object_mask_3_channels)

    # Step 8: Show the final output
    cv2.imshow('Output', background)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
