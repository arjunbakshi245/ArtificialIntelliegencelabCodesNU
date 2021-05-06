import time
class Game:
    def __init__(self):
        self.start_game()

    def start_game(self):
        self.current_state = [['.', '.', '.'],
                              ['.', '.', '.'],
                              ['.', '.', '.']]

        # X start
        self.player_turn = 'X'

    #Print the matrix
    def display(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True

    def is_end(self):
        # Verticals
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                    self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

    # Horizontals
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

    # Diagonals
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
                self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
                self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

    # GameOver
        for i in range(0, 3):
            for j in range(0, 3):
            # There's an empty field, we continue the game
                if (self.current_state[i][j] == '.'):
                    return None
    #tie
        return '.'
#===========================  min - max and prune variations========================================

    def max(self):
    # less than -1
        maxv = -2
        px = None
        py = None
        result = self.is_end()    
    # -1 - loss
    # 0  - a tie
    # 1  - win
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                # maxv Update 
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                # Reset
                    self.current_state[i][j] = '.'
        return (maxv, px, py)

    
    def min(self):    
    # -1 - win
    # 0  - a tie
    # 1  - loss

    # More than 1
        minv = 2
        qx = None
        qy = None
        result = self.is_end()
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'
        return (minv, qx, qy)
    
    def max_prune(self, alpha, beta):
            maxv = -2
            px = None
            py = None
            result = self.is_end()
            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'O'
                        (m, min_i, in_j) = self.min_prune(alpha, beta)
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        self.current_state[i][j] = '.'
                    #prune updates
                        if maxv >= beta:
                            return (maxv, px, py)
                        if maxv > alpha:
                            alpha = maxv
            return (maxv, px, py)

    def min_prune(self, alpha, beta):
            minv = 2
            qx = None
            qy = None
            result = self.is_end()
            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)
            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'X'
                        (m, max_i, max_j) = self.max_prune(alpha, beta)
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        self.current_state[i][j] = '.'
                        if minv <= alpha:
                            return (minv, qx, qy)
                        if minv < beta:
                            beta = minv
            return (minv, qx, qy)

    def play(self):
        while True:
            self.display()
            self.result = self.is_end()
        # Display
            if self.result != None:
                if self.result == 'X':
                    print('X wins')
                elif self.result == 'O':
                    print('O wins')
                elif self.result == '.':
                    print("No winner")
                self.start_game()
                return
        # X plays
            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Time without pruning: {}s'.format(round(end - start, 10)))
                    print('Prefered move: ',(qx, qy))
                    startprune = time.time()
                    (mprune, qxprune, qyprune) = self.min_prune(-2,2)
                    endprune = time.time()
                    print('Time after pruning: {}s'.format(round(endprune - startprune, 10)))
                    print('Move after pruning: ',(qxprune, qyprune))
                    px = int(input('Move X coordinate: '))
                    py = int(input('Move Y coordinate: '))
                    (qx, qy) = (px, py)
                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid')

        # O plays
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

#Call
g=Game()
g.play()

#==========References================#
#https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/