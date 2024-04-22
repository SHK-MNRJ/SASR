from deepface import DeepFace
import cv2

def emotionDetection():
    #print("Hello from, face detection module")
    video = cv2.VideoCapture(0)  # Use 0 for webcam, or provide the path to the video file

    while True:
        ret, frame = video.read()  # Read the next frame
        if not ret:
            break  # Break the loop if there are no more frames

        # Perform face recognition on the current frame using DeepFace
        result = DeepFace.analyze(frame, actions=['emotion'])
        
        #print(result)
        # Extract the face landmarks and draw bounding boxes on the frame
        emotion=(result[0])['dominant_emotion']
        print(emotion)
        return emotion
        break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Press 'q' to exit
    video.release()
    cv2.destroyAllWindows()
