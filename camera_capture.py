import cv2

def capture_image():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open camera")
        return

    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_waste.jpg", frame)
        print("Image captured and saved.")
    else:
        print("Failed to capture image.")

    cap.release()
    cv2.destroyAllWindows()

capture_image()
