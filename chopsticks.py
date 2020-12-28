"""A chopstick's game"""
import random

#maps user input to dictionary key
x_moves = {'L': 'x_left', 'R': 'x_right'}
o_moves = {'L': 'o_left', 'R': 'o_right'}


class game:
    """A class representing a chopstick's game"""
    
    def __init__(self) -> None:
        """Initialize the game such that each player starts with one finger on 
        each hand"""
        self.x_left = 1
        self.x_right = 1
        self.o_left = 1
        self.o_right = 1  
        
    def show_board(self) -> None:
        """Show the current state of the game"""
        if human == 'x':
            print('o' * self.o_left + '      ' + 'o' * self.o_right + '\n' +
                  'x' * self.x_left + '      ' + 'x' * self.x_right )
            
        else:
            print('x' * self.x_left + '      ' + 'x' * self.x_right + '\n' +
                  'o' * self.o_left + '      ' + 'o' * self.o_right )     
            
    
    def track_vars(self) -> tuple:
        """Track the number of fingers on each hand"""
        return (self.x_left, self.x_right, self.o_left, self.o_right)
    
    def set_vars(self, x_left: int, x_right: int, o_left: int, 
                 o_right: int) -> None:
        
        """Set the number of fingers on each hand"""
        self.x_left = x_left
        self.x_right = x_right
        self.o_left = o_left
        self.o_right = o_right
                    
    def get_enemy(self, player: str) -> str:
        """Return player's opponent"""
        if player == 'x':
            return 'o'
        return 'x'
    
    def get_winner(self) -> str:
        """Get the winner of the game"""
        if self.x_left == 0 and self.x_right == 0:
            return 'o'
        
        if self.o_left == 0 and self.o_right == 0:
            return 'x'
        
        return None
    
    def remove_duplicate_mutations(self, lst: list) -> list:
        """Return a list of non-symmetric mutations the current 
        player can perform"""
        removed = []
        for item in lst:
            if (item[1], item[0]) not in removed:
                removed.append(item)
        return removed
    
    def remove_duplicate_attacks(self, player: str, lst: list) -> list:
        """Return a list of non-symmetric attacks the current 
        player can perform"""        
        removed = []
        states = []
        enemy = g.get_enemy(player)
        saved_vars = self.track_vars()
        
        for move in lst:
            self.attack(move[0], move[1])
            if enemy == 'x':
                left = self.x_left
                right = self.x_right
            else:
                left = self.o_left
                right = self.o_right            
            state = (left, right)
            if state not in states:
                states.append(state)
                removed.append(move)
            self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])
        return removed
                
         
    def mutate(self, player: str, left: int, right: int) -> None:
        """Distribute player's fingers between their two hands so that the 
        sum of fingers between their two hands is unchanged."""
        if left >= 5 or right >=5:
            return 'invalid mutation'
        
        if player == 'x':
            if self.x_left + self.x_right != left + right:
                return 'invalid mutation'
            
            if (self.x_left, self.x_right) in [(right, left), (left, right)]:     
                return 'invalid mutation'           

            self.x_left = left
            self.x_right = right
            
        else:
            if self.o_left + self.o_right != left + right:
                return 'invalid mutation'
            
            if (self.o_left, self.o_right) in [(right, left), (left, right)]:
                return 'invalid mutation' 
   
            self.o_left = left
            self.o_right = right        
            
    def available_mutations(self, player: str) -> list:
        """Return a list of all available mutations player can make."""
    
        if player == 'x':
            total_sticks = self.x_left + self.x_right
            left = self.x_left
            right = self.x_right            
            
            
        if player == 'o':
            total_sticks = self.o_left + self.o_right   
            left = self.o_left
            right = self.o_right   
        combos = [(x, total_sticks - x) for x in range(total_sticks + 1)]
        legal_combos = []
        
        for item in combos:
            if self.mutate(player, item[0], item[1]) == None:             
                legal_combos.append(item)
                if player == 'x':
                    self.x_left = left
                    self.x_right = right
                else:
                    self.o_left = left
                    self.o_right = right
        
        return legal_combos
    
    
    def available_attacks(self, player: str) -> list:
        """Return a list of all available attacks a player can make."""
        attacks = []
        if player == 'x':
            for item1 in ['x_left', 'x_right']:
                for item2 in ['o_left', 'o_right']:
                    if self.dict_hand(item1) > 0 and self.dict_hand(item2) > 0:
                        attacks.append((item1, item2))
                        
        else:
            for item1 in ['o_left', 'o_right']:
                for item2 in ['x_left', 'x_right'] :
                    if self.dict_hand(item1) > 0 and self.dict_hand(item2) > 0:
                        attacks.append((item1, item2))           
            
        return attacks
    
        
               
    def set_x_left(self, num: int) -> None:
        """Setter"""
        self.x_left = num if num < 5 else 0
        
    def set_x_right(self, num: int) -> None:
        """Setter"""
        self.x_right = num if num < 5 else 0
        
    def set_o_left(self, num: int) -> None:
        """Setter"""
        self.o_left = num if num < 5 else 0
        
    def set_o_right(self, num: int) -> None:
        """Setter"""
        self.o_right = num if num < 5 else 0
     
    def dict_func(self, hand: str) -> callable:     
        """ Return hand's setter method"""
        self.func= {'x_left': self.set_x_left, 'x_right': self.set_x_right,
             'o_left': self.set_o_left, 'o_right': self.set_o_right}
        
        return self.func[hand]
    
    def dict_hand(self, hand: str) -> int:
        """Return the number of finger's on hand"""
        self.hands = {'x_left': self.x_left, 'x_right': self.x_right,
             'o_left': self.o_left, 'o_right': self.o_right}     
        
        return self.hands[hand]
        
   
        
    def attack(self, from_hand: str, to_hand: str) -> None:
        """Perform an attack from from_hand to to_hand"""
        setter = self.dict_func(to_hand)      
        from_ = self.dict_hand(from_hand) 
        to = self.dict_hand(to_hand)
      
        setter(from_ + to)
        
    def is_over(self) -> bool:
        """Return True if the game is over, else False"""
        if self.x_left == 0 and self.x_right == 0:
            return True
        
        if self.o_left == 0 and self.o_right == 0:
            return True
        
        return False
    
    def determine(self, player: str, depth: int) -> tuple:
        """Return the best move for player given the current depth of search"""
        moves = []
        score = self.get_score(player, -1000, 1000, depth)
        available_moves = self.available_attacks(player) + self.available_mutations(player)
        for move in available_moves:
            saved_vars = self.track_vars()
            
            if isinstance(move[0], str):
                self.attack(move[0], move[1])
                if self.is_over():
                    self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])                    
                    return move
                
            else:
                self.mutate(player, move[0], move[1])
            value = self.get_score(self.get_enemy(player), -1000, 1000, depth - 1)  
            self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])

            if value == score:
                moves.append(move)
                #return move
        return random.choice(moves)
            
              
    def get_score(self, player: str, alpha: int, beta: int, depth: int) -> int:
        """Return the current position's evaluation via a minimax search at 
        depth depth. Positive score's indicate a win for x, negative score's 
        indicate a win for o and 0 indicates a tie."""
          
        if self.is_over():
            if self.get_winner() == 'x':
                return 10
            else:
                return -10
            
        if depth == 0:
            return 0        
        
        attacks = self.remove_duplicate_attacks(player, self.available_attacks(player))
        mutations = self.remove_duplicate_mutations(self.available_mutations(player))
        available_moves = attacks + mutations
        
        for move in available_moves:
            saved_vars = self.track_vars()
        
            if isinstance(move[0], str):
                self.attack(move[0], move[1])
                
            else:
                self.mutate(player, move[0], move[1])
                
            
    
            value = self.get_score(self.get_enemy(player), alpha, beta, depth - 1)
            if value == 10 and player == 'x':
                self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])                  
                return 10
            
            if value == -10 and player == 'o':
                self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])                    
                return -10
            
            self.set_vars(saved_vars[0], saved_vars[1], saved_vars[2], saved_vars[3])    
            
            if player == 'x':
                if value > alpha:
                    alpha = value
                if alpha >= beta:
                    return alpha
                
            else:
                if value < beta:
                    beta = value
                if beta <= alpha:
                    return beta
                
        if player == 'x':
            return alpha
        else:
            return beta
   
        
        
            
        
if __name__ == '__main__':        
    g = game()
    human = None
    move = None
    
    while human not in ('x', 'o'):
        human = input('x goes first. Type "x" or "o" to choose your player:  ')
    computer = g.get_enemy(human)
    current_player = human if human == 'x' else computer
    #Adjust depth to change difficulty
    depth = 20
    
    while not g.is_over():        
        if current_player == human:
            g.show_board()
            
            if g.available_mutations(current_player) != []:
                while move not in ('m', 'a'):
                    move = input('Enter "m" for mutate or "a" for attack:  ')
                    if move not in ('m', 'a'):
                        print('Invalid move, try again.')
            else:
                move = 'a'
                print('You can only attack')
                    
            if move == 'a':                 
                count = 0
                while move not in g.available_attacks(current_player):
                    if count == 0:
                        move = input('Enter your move as "LL", "LR", "RL", '
                                     'or "RR": ')
                    else:
                        move = input('Invalid move, try again. Enter your move'
                                     ' as "LL", "LR", "RL", or "RR": ')
                    
                    if move not in ['LL', 'LR', 'RR', 'RL']:
                        continue
                    
                    if current_player == 'x':
                        move = (x_moves[move[0]], o_moves[move[1]])
                    else:
                        move = (o_moves[move[0]], x_moves[move[1]])
                        
                    count += 1
                    
                g.attack(move[0], move[1])
                
                        
            else:
                count = 0
                while move not in g.available_mutations(current_player):
                    if count == 0:
                        move = input('Enter your mutation as a two digit number.' 
                                     ' Ex: 13 for 1 on left hand 3 on right: ')
                    
                    else:
                        move = input('Invalid mutation. Enter your mutation as'
                                     ' a two digit number. Ex: 13 for 1 on left'
                                     ' hand 3 on right: ')                        
                    try:    
                        move = (int(move[0]), int(move[1]))
                    except:
                        continue
                        
                    count += 1
                    
                g.mutate(current_player, move[0], move[1]) 
                
            current_player = computer
        
        if not g.is_over():
            if current_player == computer:  
                g.show_board()                
                print(g.get_score(computer, -1000, 1000, depth))
                computer_move = g.determine(computer, depth)
                print(computer_move)
             
                if isinstance(computer_move[0], int):
                    g.mutate(computer, computer_move[0], computer_move[1])
                    
                else:
                    g.attack(computer_move[0], computer_move[1])
                    
                current_player = human
            
    g.show_board()
    print('winner is ', g.get_winner() + '!')
    
