# import cv2
import tensorflow as tf
# import numpy as np
import keras
from keras.models import load_model
print(tf.__version__)
print(keras.__version__)
model = load_model("models/best_suspicious.keras")
print("_----------------------------------------")
# def preprocess_frame(frame):
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
#
#     resized_frame = cv2.resize(frame, (64, 64))
#
#     normalized_frame = resized_frame/255
#
#     return normalized_frame
#
# wave = ".\person01_handwaving_d1_uncomp.avi"
# clap = ".\person01_handclapping_d1_uncomp.avi"
# # run = ".\Dataset\person15_running_d1_uncomp.avi"
# # box = ".\Dataset\person15_boxing_d1_uncomp.avi"
#
# cap = cv2.VideoCapture('./person01_handclapping_d2_uncomp.avi')
#
# # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 120)
# # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 160)
#
# frames_list = []
# frame_cnt = 0
#
# while True:
#     # Read a frame from the video source
#     ret, frame = cap.read()
#
#     img = frame.copy()
#
#     if not ret:
#         break
#
#     preprocessed_frame = preprocess_frame(img)
#     frames_list.append(preprocessed_frame)
#
#     if len(frames_list) > 30:
#         frames_list.pop(0)
#
#     if len(frames_list) == 30:
#         input_data = np.stack(frames_list, axis=0)
#         input_data = np.expand_dims(input_data, axis=0)
#         # predictions = model.predict(input_data)
#
#         # if np.max(predictions) < 0.7:
#         #     print(predictions)
#         #     print('unknown')
#         # else:
#         #     result = 'wave' if np.argmax(predictions) == 1 else 'clap'
#         #     print(predictions)
#         #     print(result)
#
#     # Show the frame
#     cv2.imshow('Real-Time Application', frame)
#
#     # Exit the loop if the 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     frame_cnt += 1
#
# # Release the video capture and close any open windows
# cap.release()
# cv2.destroyAllWindows()
