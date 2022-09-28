import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

def train():
  random.seed(1)
   
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)
  
print("1: Tegen een ander persoon spelen ")
print("2: Tegen een domme tegenstander spelen")
print("3: De tegenstander trainen")
print("4: Tegen een slimme tegenstander spelen")
print("5: Je programma kan de validatie grafiek plotten")

i = input()

if i == "5":
  train()

if i == "b":
  # doe dat andere
  aap = ""


