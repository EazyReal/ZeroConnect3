from board import *

def softmax(x):
    p = np.exp(x)
    p = p/sum(p)
    return p

class Random_Agent(object):
    #for connect3
    def __init__(self):
        n = 3
        self.actionspace = range(n*n)
    def gen_move(self, env):
        p = np.random.randn(len(self.actionspace))
        p = softmax(p)
        #assert(np.where(p>=0 && p <=1, 0.0, 1.0) = np.zeroslike(p))
        #assert(np.sum(p) == 1)
        #print(env.valid_mask().reshape(-1))
        p = np.where(env.valid_mask().reshape(-1) == 1, p, 0)
        p = p/sum(p)
        #print(p)
        pos = np.argmax(p)
        #print(pos)
        return (pos//3, pos%3)


class Game(object):
    def __init__(self, p1, p2, N = 3):
        self.p1 = p1
        self.p2 = p2
        #self.pcur = p1
        self.env = Env(N)

    def display_play(self, record):
        (winner, rec) = record
        display_env = Env()
        for c, pos in rec:
            display_env.take_action(c,pos)
            print(display_env)

    def reset(self):
        self.env.reset()

    def play(self):
        env = self.env
        env.reset()

        record = list()
        while env.status() == -2: #not ended
            c = env.player_to_move()
            pcur = self.p1 if c == 1 else self.p2
            pos = pcur.gen_move(env) #if pass env, may involve in copy env, care the cost
            assert(pos in env.valid_actions())
            record.append([c, pos])
            env.take_action(c, pos)

        return (env.status(), record)

    def playn(self, num_games):
        records = list()
        for i in range(num_games):
            records.append(self.play())
        return records

    def play2n(self, num_games):
        p1_first_records = self.playn(num_games)
        self.p1, self.p2 = self.p2, self.p1
        p2_first_records = self.playn(num_games)
        return p1_first_records, p2_first_records
