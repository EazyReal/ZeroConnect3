#ifndef BOARDH
#define BOARDH

#include <iostream>
#include <cmath>
#include <cassert>
#include <vector>
using namespace std;

#define NEND -2
const int N = 3;
const int N2 = 9;
const char ox[3] = {'x', '.', 'o'};

typedef int POS;
typedef int STATUS;
typedef int COL;

/*
class HumanPlayer
{
public:
  HumanPlayer(){};
  gen_move(Board b){};
};
*/

//connect3 board
class Board
{
public:
  int sz;
  int vol;
  int nwin;
  int stones;
  int board[N2];

public:
  Board();
  void reset();
  inline COL c2play();
  STATUS check();
  STATUS status();
  STATUS is_end();
  STATUS set_pos(int value, POS pos); //return status
  STATUS take_action(POS pos);
  vector<POS> valid_pos() const;//const

  friend ostream &operator<<(ostream &s, const Board& b);
};

#endif //BOARDH
