import cv2 # Import OpenCV
from ultralytics import YOLO

model = YOLO("yolo11n.pt") # Load a small pretrained YOLO model

camera = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION) # Save access to default camera (MacBook webcam)

if not camera.isOpened():
    print("Camtry could not open the camera.")
    exit()

while True:
    success, frame = camera.read() # read() returns bool success and one frame

    # If camera disconnects or OpenCV can't retrieve frame
    if not success:
        break

    results = model(frame) # Send cam frame to neural network and ask what objects are seen

    annotated_frame = results[0].plot() # Take YOLO's detections and draw the bounding boxes and labels

    cv2.imshow("Camtry", annotated_frame) # imshow() -> creates a window and shows image

    # OpenCV wait 1 ms for keyboard input
    # If user presses q then quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release() # Done using camera
cv2.destroyAllWindows() # Close OpenCV window