import cv2
import serial
import time
import mediapipe as mp  

try:
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    time.sleep(2)
    print("ESP32 Connected Successfully!")
except Exception as e:
    print("Error: Could not connect to ESP32. Check the port or close Serial Monitor.")

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

print("Starting Camera... Show your hand!")

while cap.isOpened():
    success, img = cap.read()
    if not success: 
        continue

    img = cv2.flip(img, 1) 
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
           
            tip = hand_lms.landmark[8].y
            mcp = hand_lms.landmark[6].y

            if tip < mcp:
                print("Status: OPEN -> LED ON")
                try:
                    ser.write(b'0')
                except:
                    pass
            else:
                print("Status: CLOSED -> LED OFF")
                try:
                    ser.write(b'1')
                except:
                    pass

            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
    
    cv2.imshow("HAND-CONTROLE-LED", img)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

