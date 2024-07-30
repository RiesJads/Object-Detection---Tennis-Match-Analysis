from ultralytics import YOLO 

model = YOLO('TB-Models/last.pt')

result = model.track('Input/input_video.mp4',conf=0.1, save=True)