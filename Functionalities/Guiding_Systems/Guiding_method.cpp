#include <iostream> 
#include <fstream> 
#include <math.h>
# include <string>

using namespace std;
class Direction{
  private: 
         double x_axis;
         double y_axis;
         double z_axis;
  public:
         void vectors(double x, double y, double z){
             x_axis = x;
             y_axis = y;
             z_axis = z;
  }

  double Reducedcalculation();
  void ReducedAreaOutput(){
   cout << "Reduced Area is: " << Reducedcalculation() << endl;
  } 

  double Sizedcalculation();
  void SizedAreaOutput(){
   cout << "Sized Area is: " << Sizedcalculation() << endl;
  } 
};

double Direction::Reducedcalculation(){
   double originVar = ((x_axis-y_axis)/2*z_axis);
   double Var = -1; 
   double posVar; 
    if (originVar<0){
      posVar = originVar*Var;
      return posVar;
    } else{
      return originVar;
    }
}

double Direction::Sizedcalculation(){
    return ((x_axis+y_axis)*z_axis);
}

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
           if (new_id_number==1000){
                cout << "Jackpot, within the gap" << "\n";
           }
           break;
      }
      break;
    }
    cout << i << "\n";
  }
  Direction direction1;
  direction1.vectors(200, 500, 700);
  direction1.ReducedAreaOutput();
  direction1.SizedAreaOutput();
  return 0;
}