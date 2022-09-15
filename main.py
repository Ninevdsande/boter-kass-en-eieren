from bke import EvaluationAgent, is_winner, opponent, start

class MijnSpeler(EvaluationAgent):
  def evaluate(self, board, my_symbol, opponent_symbol):
    getal = 1
    
    if board[4] == my_symbol:
      getal = getal + 5
    return getal
    if is_winner(board, my_symbol):
            reward = 1
    elif is_winner(board, opponent[my_symbol]):
            reward = -1
    else:
            reward = 0
    return reward()
    

mijn_speler = MijnSpeler()
start(player_o=mijn_speler)