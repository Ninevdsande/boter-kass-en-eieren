import random
 
from bke import MLAgent, is_winner, opponent, RandomAgent, train_and_plot, save, train, load, start, EvaluationAgent
 
 
class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward

class MyRandomAgent(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    return random.randint(1,500)

def plot():
  random.seed(1)
   
  my_agent = MyAgent(alpha=0.8, epsilon=0.2)
  random_agent = RandomAgent()
   
  train_and_plot(
      agent=my_agent,
      validation_agent=random_agent,
      iterations=50,
      trainings=100,
      validations=1000)

def trainOnly():
  my_agent = MyAgent()
  
  train(my_agent, 3000)
  save(my_agent, 'MyAgent_3000')

def slimmetegenst():
  my_agent = load('MyAgent_3000')
  my_agent.learning = False
  start(player_x=my_agent)

def dommetegenst():
  my_random_agent = MyRandomAgent()
  start(player_o=my_random_agent)
  

print("1: Tegen een ander persoon spelen ")
print("2: Tegen een domme tegenstander spelen")
print("3: De tegenstander trainen")
print("4: Tegen een slimme tegenstander spelen")
print("5: Je programma kan de validatie grafiek plotten")

i = input()

if i == "5":
  plot()

if i == "3":
  trainOnly()

if i == "4":
  slimmetegenst()

if i == "2":
  dommetegenst()

