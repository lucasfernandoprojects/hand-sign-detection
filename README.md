# Hands Seals Detection

In this repository, you will find an AI project that aims to detect Naruto's hands seals in real time, as you can see in the GIF below:

![A man doing hand gestures in front of a webcam.](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/gifs/giphy.gif)

## Introduction

Since I discovered the world of computer vision, I’ve been fascinated by how it works and the cool projects you can build with it. If you’ve ever watched Naruto, you probably remember the hands seals, right? It's a concept of controlling the five elements using hands gestures, as you can see in the image below:

![Kakashi Hatake performing hand gestures and creating a chidori - lightning sword](https://github.com/lucasfernandoprojects/hand-sign-detection/blob/main/gifs/kakashi-performing-chidori.gif)

During my AI studies, I thought, what if I could create a computer vision system that recognizes these hands seals in real-time? Well, that’s exactly what I did, and this repository contains all coding I created to reach this goal.

## Context

To create this project, I got studying a specific subject inside Computer Vision called Object Recognition. This is a technology that enables computers to identify and label objects within images or videos. It works similarly to how humans recognize and name things they see. In order to create an object recognition system, you'll generally follow five steps:

1. Image input: You need data to train the model, so you’ll probably use a camera or another device to capture the images and videos you need for the dataset;
2. Preprocessing: In this step, the developer cleans up the dataset to improve its quality and reduce the chances of poor model performance;
3. Feature extraction: This goal is reached by the artificial intelligence algorithm. It identifies important parts of the image, such as shapes and textures, that help the model analyze the data;
4. Compasiron: This step is also performed by the AI. At this step, the model compares the features it identified previously to a database of known objects to find matches;
5. Prediction: Finally, the computer labels the objects it recognized in the image, often drawing boxes around them to highlight their locations.

This structured process allows the application to accurately recognize and provide useful information about objects captured in the images. That’s why this technique is crucial for various tools like self-driving cars, facial recognition for security systems, and inspecting products on an assembly line.

## Set up

After defining the problem and desired outcome, the first step to develop the AI model was data collection. Think of data as the fuel for artificial intelligence; you can't do anything without the appropriate data.

I needed photos of hands seals to train the model. Originally, there are 12 distinct hands seals in the Naruto universe, and these were exactly what the system needed to learn to identify.

![Naruto performing the twelve basic hands seals]()

A detailed tutorial about this project was posted on [YouTube](https://www.youtube.com/watch?v=mIE9g0209xk&t=6s).
