#include <iostream> 
#include <fstream> 
#include <math.h>
# include <string>

using namespace std;

int main (){
  int insert_number = 6;
  int initial_number = rand();
  int id_number = min (351, 279);
  std::cout << "Test Run"<< std::endl; 
  for (int i=0; i<initial_number; i++){
    if (i==insert_number){
      cout << "You hit the target" << "\n";
      while (insert_number<id_number){
           int new_id_number = max(id_number, 1000);
           cout << new_id_number << "\n";
           break;
      }
      break;
    }
    cout << i << "\n";
  }
  return 0;
}

