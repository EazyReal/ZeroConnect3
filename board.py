import numpy as np

N = 3

class Env(object):
    #connect3 environment
    #0 = no play
    #1 = black
    #-1 = white
    def __init__(self, n = N):
        #params
        self.n = n
        self.n2 = n*n
        self.winn = self.n
        #board related
        self.board = np.zeros(self.n2).astype(int)
        self.stones = 0
    def __str__(self):
        #where is so convenient
        tmp = np.where(self.board.reshape(N,N) == 1, 'o', self.board.reshape(N,N))
        tmp = np.where(tmp == '-1', 'x', tmp)
        tmp = np.where(tmp == '0', '.', tmp)
        return str(tmp)
    def reset(self):
        self.board = np.zeros(self.n2).astype(int)
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
        for i in range(self.n2):
            if(self.board[i] == 0):
                ret.append(i)
        return ret

    def take_action(self, player, pos):
        if self.board[pos] != 0:
            return None
        self.board[pos] = player
        status = self.check()
        #print(board)
        self.stones += 1
        return status

    def check(self):
        board2d = self.board.reshape(N,N)
        s0 = np.sum(board2d, axis = 0)
        s1 = np.sum(board2d, axis = 1)
        d0 = np.sum(board2d.diagonal())
        d1 = np.sum(np.flip(board2d, 0).diagonal())
        all_sum = np.r_[s0.reshape(-1), s1.reshape(-1), np.asarray([d0, d1])]
        #print(all_sum)
        if self.winn in all_sum:
            return 1
        elif -self.winn in all_sum:
            return -1;
        else:
            return 0;
