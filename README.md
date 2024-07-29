
# Tennis Analysis
Analysis of Tennis players in a video to measure their speed, ball shot speed and number of shots. This project will detect players and the tennis ball using YOLO and CNNs to extract court key points. 
The project includes the training of 2 YOLO models and CNN Resnet50
+ YOLOv8 for detection of the players
+ Fine-tuning YOLOv5 for detection of the tennis ball
+ Resnet50 for marking key points on the courts

## Demo Result


## Training & Validation Data
Images from various tennis matches obtained via RoboFlow include multiple tennis surfaces to ensure performance across all surfaces. The training data includes:
+ 2 Hardcourt types
+ Clay
+ Grass
+ Labels/Bounding Boxes

## Example of Training Data
{INSERT IMAGES}

## Requirements
* python3.8
* ultralytics
* pytroch
* pandas
* numpy 
* opencv
