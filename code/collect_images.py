from os import path, makedirs
from cv2 import VideoCapture, putText, imshow, waitKey, imwrite, destroyAllWindows, FONT_HERSHEY_SIMPLEX, LINE_AA

number_of_classes = 1 # Number of hand signs (seals)
dataset_size = 100 # Number of photos for each class
data_directory = '../data/'
camera_index = 0
hand_seals = {0: 'Saru (monkey)', 1: 'Tatsu (dragon)', 2: 'Ne (rat)', 3: 'Tori (bird)',
              4: 'Mi (snake)', 5: 'Ushi (ox)', 6: 'Inu (dog)', 7: 'Uma (horse)',
              8: 'Tora (tiger)', 9: 'I (boar)', 10: 'Hitsuji (ram)', 11: 'U (hare)'}

# Check if the data directory exists
if not path.exists(data_directory):
    makedirs(data_directory)

video_cap = VideoCapture(camera_index)
for n in range(number_of_classes):
    if not path.exists(path.join(data_directory, str(n))):
        makedirs(path.join(data_directory, str(n)))

    print(f'Collecting data for class {n} - {hand_seals[n]}')

    while True:
        ret, frame = video_cap.read()
        putText(frame, 'Press SPACE to start', (100, 50), FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, LINE_AA)
        imshow('frame', frame)
        if waitKey(25) == ord(' '):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = video_cap.read()
        imshow('frame', frame)
        waitKey(25)
        imwrite(path.join(data_directory, str(n), '{}.jpg'.format(counter)), frame)
        counter += 1

video_cap.release()
destroyAllWindows()
print("The capture process is finished")
