package Network;
import java.util.Scanner;
import java.util.*;
import java.util.random.*;
import java.util.Arrays;
import java.util.ArrayList;
import static java.lang.Math.*;
public class backup {
  public static int i,j,k;
  public static int status = 3;
  public static int marker = 0;
  public static String confirmation;
    public static void main (String args[]){
    boolean localchecker = checker(status);      // checking if the length is 3       
    confirmation = new Boolean(localchecker).toString(localchecker); 
                                                // reassign checker variable to confirmation.
     System.out.println(confirmation);
    }     

    public static boolean checker(int count){
      int localmarker = 1;                        // for marker implementation.
        for(i=0;i<5;i++){                         // 
          System.out.println("trial");
          count ++;                               // placing counter to check the condition.
          if(3<count){
           for(j=0;j<3;j++){
             int length = k++;                    // the length would raise up the k value 
               while(length==3){
                     System.out.println(length);
                     marker ++;                   // ending marker introduced.
                     break;
                  }
               }
             }
           }
      if (marker == localmarker){                 //check the status if all conditions fullfilled
        return true;                              // ot should be marker = 1, hence the true status.
      } else {
        return false;
      }
    }
}