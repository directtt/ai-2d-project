# tractor-ai-2d-project
Python reinforcement learning 2D project for my AI classes that uses search algorithms, machine learning, neural networks and genetic algorithm.

## General idea
General idea of classes was to implement throughout semester end-to-end AI project that consist of:
- Implementation of a two-dimensional discrete environment (aka lattice) for an autonomous agent using knowledge representation techniques presented in lectures
- Application of informed state space search strategies to solve the problem of scheduling agent movement in the environment
- Application of selected machine learning methods to solve problems that the agent must face in the surrounding environment

We have chosen smart tractor as a main topic of our project. The task of the smart tractor is to cultivate the field. The tractor, moving around the field, checks the soil and crop condition and makes decisions on the application of crop irrigation, fertilizer application, collecting crops etc.

## Algorithms use case 
- Searching Algorithms: BFS & A* for tractor shortest path to crops finding
- Machine Learning: XGBoost for crops watering decision (binary classification)
- Neural Networks: CNN for image classification of real crops images to crops on the board
- Genetic Algorithm: intial arrangement of the crops on the board

## Libraries 
- [pygame](https://github.com/pygame/) for agent and enviroment representation
- BFS & A* were implemented from scratch
- [XGBoost](https://github.com/dmlc/xgboost) for classification
- [tensorflow](https://github.com/tensorflow/tensorflow) for CNN
- Genetic algorithm was implemented from scratch
- Some auxiliary Data Science libraries such as [pandas](https://github.com/pandas-dev/pandas), [numpy](https://github.com/numpy/numpy) or [scikit-learn](https://github.com/scikit-learn/scikit-learn)

## Preview 
![test](https://im.ezgif.com/tmp/ezgif-1-d4a04fd200.gif)
