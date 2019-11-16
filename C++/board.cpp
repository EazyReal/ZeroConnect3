#include "board.h"

#define NEND -2
//#define TEST

using namespace std;

Board::Board()
{
  sz = N;
  nwin = N;
  vol = N2;
  stones = 0;
  memset(board, 0, sizeof(board));
};

void Board::reset()
{
  stones = 0;
  memset(board, 0, sizeof(board));
}

inline COL Board::c2play()
{
  return (stones%2 == 0)?1:-1;
}

STATUS Board::check()
{
  for(int i = 0; i < sz; i++)
  {
    int sh = 0;
    int sv = 0;
    for(int j = 0; j < sz; j++)
    {
      sh += board[i*3+j];
      sv += board[j*3+i];
    }
    if(sh == nwin || sv == nwin) return 1;
    if(sh == -nwin || sv == -nwin) return -1;
  }
  int sd1 = 0;
  int sd2 = 0;
  for(int i = 0; i < sz; i++)
  {
    sd1 += board[i*3+i];
    sd2 += board[i*3+2-i];
  }
  if(sd1 == nwin || sd2 == nwin) return 1;
  if(sd1 == -nwin || sd2 == -nwin) return -1;
  return 0;
}

STATUS Board::status()
{
  COL winner = check();
  if(winner) return winner;
  return (stones == vol)? 0: NEND;
}

STATUS Board::set_pos(int value, POS pos)
{
  board[pos] = value;
  return status();
}

STATUS Board::take_action(POS pos)
{
  assert(board[pos] == 0);
  board[pos] = c2play();
  stones++;
  return status();
}

vector<POS> Board::valid_pos() const
{
  vector<POS> ret;
  for(int i = 0; i < vol; i++) if(board[i]==0) ret.push_back(i);
  return ret;
}

ostream &operator<<(ostream &s, const Board& b)
{
  cout << "___________" << endl;
  for(int i = 0; i < b.sz; i++)
  {
    for(int j = 0; j < b.sz; j++)
    {
      cout << ox[b.board[i*3+j]+1] << ' ';
    }
    cout << endl;
  }
  cout << "___________" << endl;
  return s;
}

#ifdef TEST
int main()
{
  Board b = Board(N)


  return 0;
}
#endif //TEST
