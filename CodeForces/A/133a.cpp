#include <iostream>
#include <cstring>
using namespace std;

bool isWord(){
  char word[100];
  cin >> word;
  int n = strlen(word);
  for(int i=0; i<n; i++){
    if(word[i] == 'H' || word[i] == 'Q' || word[i] == '9'){
      return true;
    }
  }
  return false;
}

int main(){
  if(isWord()){
    cout << "YES";
  }
  else{
    cout << "NO";
  }
}
