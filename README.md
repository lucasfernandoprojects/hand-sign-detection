# Hands Seals Detection

In this repository, you will find an AI project that aims to detect Naruto's hands seals in real time, as you can see in the GIF below:

![A man doing hand gestures in front of a webcam.](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/giphy.gif)

## Introduction

Since I discovered the world of computer vision, I’ve been fascinated by how it works and the cool projects you can build with it. If you’ve ever watched Naruto, you probably remember the hands seals, right? It's a concept of controlling the five elements using hands gestures, as you can see in the image below:

![Kakashi Hatake performing hand gestures and creating a chidori - lightning sword](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/kakashi-performing-chidori.gif)

During my AI studies, I thought: what if I could create a computer vision system that recognizes these hands seals in real-time? Well, that’s exactly what I did, and this repository contains all coding I created to reach this goal.

## Context

To create this project, I had to study a specific subject inside Computer Vision called Object Recognition. This is a technology that enables computers to identify and label objects within images or videos. It works similarly to how humans recognize and name things they see. In order to create an object recognition system, you'll generally follow five steps:

1. Image input: You need data to train the model, so you’ll probably use a camera or another device to capture the images and videos you need for the dataset;
2. Preprocessing: In this step, the developer cleans up the dataset to improve its quality and reduce the chances of poor model performance;
3. Feature extraction: This goal is reached by the artificial intelligence algorithm. It identifies important parts of the image, such as shapes and textures, that help the model analyze the data;
4. Comparison: This step is also performed by the AI. At this step, the model compares the features it identified previously to a database of known objects to find matches;
5. Prediction: Finally, the computer labels the objects it recognized in the image, often drawing boxes around them to highlight their locations.

This structured process allows the application to accurately recognize and provide useful information about objects captured in the images. That’s why this technique is crucial for various tools like self-driving cars, facial recognition for security systems, and inspecting products on an assembly line.

## Set up

After defining the problem and desired outcome, the first step to develop the AI model was data collection. Think of data as the fuel for artificial intelligence; you can't do anything without the appropriate data.

I needed photos of hands seals to train the model. Originally, there are 12 distinct hands seals in the Naruto universe, and these were exactly what the system needed to learn to identify.

![Naruto performing the twelve basic hands seals](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/all-basic-hands-seals.jpg)

I wrote a Python script that accessed my webcam and took 100 photos of each hand seal. The program repeated this process 12 times, each time capturing a different hand seal. In the end, I had a database of 1,200 images. This task were performed by the script _collect_images.py_

Next, I needed to label the data. When working with object recognition, you must tell the model where the object is located in each image. For this task, I used a special software called [CVAT](https://www.cvat.ai/).

I uploaded the images to CVAT, labeled them according to the hand seal it represented, and then exported the annotations into the YOLO format.

![CVAT tasks.](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/cvat-tasks.jpg)
![CVAT annotation of the first photo of the eighth class.](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/cvat-annotation-class-7.jpg)

If you open one of these annotation files, you’ll see five numbers arranged in one line. The first value represents the class (the hand seal). The second and third numbers are the coordinates of the bounding box center, while the fourth and fifth values represent the width and height of the box.

![Annotation of the photo 6 class 0.](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/photos-readme/annotation-of-img-6-class-0.jpg)

With the data labeled, I was ready to train the model. This was the most time-consuming part of the project. I tried several approaches to find the best solution.

After days of trial and error, I decided to use [YOLO](https://docs.ultralytics.com/) (You Only Look Once), a real-time object detection algorithm. YOLO is built on a deep CNN architecture and is known for its high accuracy and reliability. Applying YOLO to my dataset solved the hand seal detection problem effectively. The files _train-yolo-model.py_ and _config.yaml_ were used to accomplished this goal.

Once the model was trained, I downloaded it and wrote a Python script to use the AI with my webcam in real-time, displaying the predictions on the screen. To do it, run the Python script _predict.py_

A detailed tutorial about this project was posted on [YouTube](https://www.youtube.com/watch?v=mIE9g0209xk&t=6s). Hope you find it helpful :)
