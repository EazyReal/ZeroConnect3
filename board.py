import numpy as np

class Env(object):
    #connect3 environment
    #0 = no play
    #1 = black
    #-1 = white
    def __init__(self, n = 3):
        #params
        self.n = n
        self.n2 = n*n
        self.winn = self.n
        #board related
        self.board = np.zeros((n,n)).astype(int)
        self.stones = 0
    def __str__(self):
        return str(self.board)
    def reset(self):
        self.board = np.zeros((self.n,self.n)).astype(int)
        self.stones = 0

    def player_to_move(self):
        return 1 if (self.stones%2 == 0) else -1

    def is_full(self):
        return self.n2 == self.stones

    def status(self):
        res = self.check()
        if res != 0:
            return res
        else:
            return 0 if self.is_full() else -2 #-2 means not ended

    def valid_mask(self):
        return np.where(self.board == 0, 1, 0);

    def valid_actions(self):
        if(self.stones == self.n2): return None
        ret = list()
        for i in range(self.n):
            for j in range(self.n):
                if(self.board[i][j] == 0):
                    ret.append((i,j))
        return ret

    def take_action(self, player, pos):
        (x, y) = pos
        if self.board[x][y] != 0:
            return None
        self.board[x][y] = player
        status = self.check()
        #print(board)
        self.stones += 1
        return status

    def check(self):
        s0 = np.sum(self.board, axis = 0)
        s1 = np.sum(self.board, axis = 1)
        d0 = np.sum(self.board.diagonal())
        d1 = np.sum(np.flip(self.board, 0).diagonal())
        all_sum = np.r_[s0.reshape(-1), s1.reshape(-1), np.asarray([d0, d1])]
        #print(all_sum)
        if self.winn in all_sum:
            return 1
        elif -self.winn in all_sum:
            return -1;
        else:
            return 0;
        s1 = np.sum(self.board, axis = 1)
        d0 = np.sum(self.board.diagonal())
        d1 = np.sum(np.flip(self.board, 0).diagonal())
        all_sum = np.r_[s0.reshape(-1), s1.reshape(-1), np.asarray([d0, d1])]
        #print(all_sum)
        if self.winn in all_sum:
            return 1
        elif -self.winn in all_sum:
            return -1;
        else:
            return 0;
