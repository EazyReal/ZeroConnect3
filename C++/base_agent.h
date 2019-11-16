#ifndef BASEAGENT_H
#define BASEAGENT_H

#include "board.h"
#include <ctime>
using namespace std;

class Player //virtual class
{
public:
  virtual POS genmove(const Board& b) = 0;
};

class HumanPlayer : public Player
{
public:
  HumanPlayer();
  POS genmove(const Board& b);
};

class RandomPlayer : public Player
{
public:
  RandomPlayer();
  POS genmove(const Board& b);
};

class Game
{
public:
  Game();
};

#endif //BASEAGENT_H
