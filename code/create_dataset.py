from os import listdir, path
from mediapipe import solutions
from cv2 import imread, cvtColor, COLOR_BGR2RGB
from matplotlib.pyplot import figure, imshow, show

mp_hands = solutions.hands
mp_drawing = solutions.drawing_utils
mp_drawing_styles = solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)
data_directory = '../data'

for dir in listdir(data_directory):
    for image_path in listdir(path.join(data_directory, dir))[:1]:
        img = imread(path.join(data_directory, dir, image_path))
        img_rgb = cvtColor(img, COLOR_BGR2RGB)
        
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img_rgb,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )

        figure()
        imshow(img_rgb)

show()