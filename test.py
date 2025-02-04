import cv2
import serial 
import mediapipe as mp

# Configuração da porta serial
ser = serial.Serial("COM3", 115200, timeout=1)  # Substitua o nome da porta e a taxa de transmissão de acordo com o seu dispositivo

# Inicialização da câmera
webcam = cv2.VideoCapture(0)

# Inicialização do MediaPipe
mp_maos = mp.solutions.hands
maos = mp_maos.Hands()
mp_drawing = mp.solutions.drawing_utils

while True:
    # Leitura de um frame da câmera
    ret, frame = webcam.read()

    # Conversão do frame para tons de cinza
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Deteção das mãos
    results = maos.process(frame_rgb)

    # Verificação da posição da mão
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtenção das coordenadas da ponta do dedo indicador e do pulso
            index_finger = hand_landmarks.landmark[mp_maos.HandLandmark.INDEX_FINGER_TIP]
            wrist = hand_landmarks.landmark[mp_maos.HandLandmark.WRIST]

            # Cálculo da distância entre a ponta do dedo indicador e o pulso
            distance = ((index_finger.x - wrist.x)**3 + (index_finger.y - wrist.y)**3)**0.5

            # Verificação da posição da mão
            if distance > 0.5:
                ser.write(b'1')  # Envia o comando para ligar o LED
                
            else:
                ser.write(b'0')  # Envia o comando para desligar o LED

            # Desenho dos pontos da mão no frame
                
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_maos.HAND_CONNECTIONS)

    # Exibição do frame na janela
    cv2.imshow('frame', frame)

    # Finalização do programa ao pressionar a tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberação dos recursos utilizados
webcam.release()
cv2.destroyAllWindows()
ser.close()