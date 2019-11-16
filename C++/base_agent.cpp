#include "base_agent.h"

using namespace std;

/*
POS genmove(Player &p, const Board& b)
{
  cerr << "in genmove player" << endl;
  return p.genmove(b);
}
*/

HumanPlayer::HumanPlayer(){};
POS HumanPlayer::genmove(const Board& b)
{
  POS pos;
  cout << b;
  while(cout << "enter move as 3i+j, i,j 0-indexed" << endl)
  {
    cin >> pos;
    if(pos >= b.vol || pos < 0) cout << "error : overflow!!" << endl;
    if(b.board[pos] != 0) cout << "error : occupied!!" << endl;
    if(b.board[pos] == 0) break;
  }
  return pos;
}


RandomPlayer::RandomPlayer(){srand(time(NULL));};
POS RandomPlayer::genmove(const Board& b)
{
  //cerr << "in genmove rand" << endl;
  vector<POS> actions = b.valid_pos();
  int idx = rand()%actions.size();
  return actions[idx];
}
