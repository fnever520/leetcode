#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

void print_vector(vector<int> data) {
  for (int i=0;i<data.size();i++) {
    cout << data[i] << endl;
  }
}

void play_game() {
  vector<int> guesses;
  int random = rand()%251;
  cout << random << endl;
  cout << "Guess anumber" << endl;
  while (true) {
    int guess;
    cin >> guess;
    guesses.push_back(guess);
    if (guess == random) {
      break;
    }
  }

  print_vector(guesses);
  
}

int main() {
  play_game();

  return 0;
}