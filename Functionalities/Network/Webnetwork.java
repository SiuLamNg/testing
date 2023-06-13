package Network;
// Functions used in the in files.
import java.util.Scanner;
// Functions used in the in files.

public class Webnetwork { 
    public static int CorrectAnswer = 7;

    public static void Question(){
      System.out.println("How many Access Points in the server now?");
    }
    public static void GoodEnding(){
      System.out.println("YOU ARE CORRECT!");
    }
    public static void BadEnding(){
      System.out.println("This is not the correct answer, please try again.");
    }

    public static void AnswerChecking(int answer){
      if (answer == CorrectAnswer){
        GoodEnding();
      }else if(answer != CorrectAnswer){
        do {
          BadEnding();
          Question();
          AnswerHandling();
          if (answer == CorrectAnswer){
            GoodEnding();
            break;
          }
          break;
        } while (answer != CorrectAnswer);
      }
    }
    
    public static void AnswerHandling (){
      Scanner host = new Scanner(System.in);
      try{
        int userinput = host.nextInt();
        AnswerChecking(userinput);
      } finally {
        host.close();
      }
    }
    public static void main (String args[]){
      Question();
      AnswerHandling();
    }
}