
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

![synframe158_jpg rf 673671e1058d073a21d2e6c6147d5679](https://github.com/user-attachments/assets/40187de9-ca7e-4a10-93e3-f4394c9e135a)


![fed59_jpg rf 1638258685d0cf43ca8e55bc7a3f017a](https://github.com/user-attachments/assets/18bca86f-ea6a-4a5f-a1fa-37c44a5e3b72)


![clay412_jpg rf aacb7c5d89b372b3ca686dd69abca001](https://github.com/user-attachments/assets/c744429e-648f-448a-83e6-05f056b5f42f)
