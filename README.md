# 2020-Game-Play
Authors: Tanmay Prakash, Maxwell Hampel, Ryan Butler and Shreyas Srinivasan

'''
This repository consists of a model agent for the old time classic game Street Figher 2. 
We use the Champions Deluxe Edition source code via the Dopamine Framework and the Gym Retro emulator to train our agent.
The basic principle implemented is Reinforcement Learning via pixel-based analysis.
Warning: It is advised to design a state-vector map, but an older game can still have a proper agent using pixel analysis. 

The repository is made of three major parts: The Data Generator, the Environment and Data Checker, and the Model.
The Data Generator consists of the batch-wise output of the game's metadata at 30 frames per second.
The Environment and Data Checkers ensure that all the correct packages and correct package versions are in place to generate the model. 
The Model comprises of calls to the Gym_retro.py file and also has code that enables a visual display of your agent training. 

Please refer to this video for more detail on the code and the game:
https://youtu.be/FdtwKXfOmLA
  
To get the training started:
  Please select the Game_Play_Testing.ipynb file to gain access to the notebook. 
   Just run cell by cell from top to bottom in the notebook..
  
Want to know more about the items used in this project?
  1) https://openai.com/blog/gym-retro/ 
  2) https://opensource.google/projects/dopamine
  3) https://medium.com/@SmartLabAI/reinforcement-learning-algorithms-an-intuitive-overview-904e2dff5bbc
  '''
  

