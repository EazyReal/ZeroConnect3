from board import *

N = 3

class Human_Agent(object):
    def __init__(self):
        pass
    def gen_move(self,env):
        print(env)
        while True:
            cmd = input("input move (x, y) as 3*x+y (0-indexed):")
            pos = int(cmd)
            if not pos in range(N*N):
                print("not in range(0, N*N)!!")
                continue
            if not pos in env.valid_actions():
                print("occupied!!")
                continue
            break
        return pos


def softmax(x):
    p = np.exp(x)
    p = p/sum(p)
    #assert(np.where(p>=0 && p <=1, 0.0, 1.0) = np.zeroslike(p))
    #assert(np.sum(p) == 1)
    return p


class Random_Agent(object):
    #for connect3
    def __init__(self):
        self.n = N
    def gen_move(self, env):
        cur = env.player_to_move()
        #if can win , win
        for move in env.valid_actions():
            if env.set_board(cur, move) == cur:
                env.set_board(0, move)
                return move
            env.set_board(0, move)
        #if enemy can win, stop him
        for move in env.valid_actions():
            if env.set_board(-cur, move) == -cur:
                env.set_board(0, move)
                return move
            env.set_board(0, move)

        p = np.random.randn(self.n*self.n)
        p = softmax(p)
        p = np.where(env.valid_mask() == 1, p, 1e-10)
        p = p/sum(p)
        #print(p)
        pos = np.argmax(p)
        #print(pos)
        return pos


class Game(object):
    def __init__(self, p1, p2, N = N):
        self.p1 = p1
        self.p2 = p2

    @staticmethod
    def display(record):
        (winner, rec) = record
        display_env = Env()
        for c, pos in rec:
            display_env.take_action(pos)
            print(display_env)

    def play(self):
        env = Env(N)

        record = list()
        while env.status() == -2: #not ended
            c = env.player_to_move()
            pcur = self.p1 if c == 1 else self.p2
            pos = pcur.gen_move(env) #if pass env, may involve in copy env, care the cost
            assert(pos in env.valid_actions())
            record.append([c, pos])
            env.take_action(pos)

        return (env.status(), record)

    def playn(self, num_games):
        records = list()
        for i in range(num_games):
            records.append(self.play())
        return records

    def play2n_symmetric(self, num_games):
        p1_first_records = self.playn(num_games)
        self.p1, self.p2 = self.p2, self.p1
        p2_first_records = self.playn(num_games)
        return p1_first_records, p2_first_records
