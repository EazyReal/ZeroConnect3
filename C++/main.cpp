#include "board.h"
#include "base_agent.h"

using namespace std;

typedef pair<COL, vector<POS> > REC;

void display(REC rec)
{
  COL winner = rec.first;
  Board b;
  for(POS pos : rec.second)
  {
    b.take_action(pos);
    cout << b;
  }
  cout << "winner is " << winner << endl;
}

REC play(Player &p1, Player &p2)
{
  Board b;
  vector<POS> pos_record;
  while(b.status() == NEND)
  {
    Player &cur_player = (b.c2play() == 1) ? p1 : p2;
    POS pos = cur_player.genmove(b);
    pos_record.push_back(pos);
    b.take_action(pos);
  }
  return REC(b.check(), pos_record);
}

int main()
{
  RandomPlayer p1 = RandomPlayer();
  RandomPlayer p2 = RandomPlayer();
  REC rec = play(p1, p2);
  display(rec);
  return 0;
}

/*first test board
int main()
{
  //srand(time(NULL));
  Board b;
  vector<POS> record;
  while(b.status() == NEND)
  {
    POS pos;
    cout << b;
    while(1)
    {
      cout << "enter move as 3i+j, i,j 0-indexed" << endl;
      cin >> pos;
      if(b.board[pos] == 0) break;
    }
    record.push_back(pos);
    b.take_action(pos);
  }
  cout << "winner is " << ox[b.status()+1] << endl;

  return 0;
}
*/
