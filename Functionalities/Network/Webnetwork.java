package Network;
// Functions used in the in files.
import java.util.Scanner;
import java.util.*;
import java.util.random.*;
import java.util.Arrays;
import java.util.ArrayList;
import static java.lang.Math.*;
// Functions used in the in files.

public class Webnetwork { 
    public static int CorrectAnswer = 7;
    public static int trials = 0;

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
      int count;
      int looping = 0;
        if (answer == CorrectAnswer){
          GoodEnding();
       } else{
          for (count=0;0<trials;count++){
                if (answer == CorrectAnswer){
                  GoodEnding();
                  break;
                }
                else{
                    trials++;
                    BadEnding(); 
                  }
              }
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



// first the user have to be input the answer,
// check if it's 7, if it's 7 return a statment, end the program.
// if it isn't 7, return a statment and ask them to answer it again,
// until they are correct.
// 1. QuestionRelease
// 2. Handling
// 3. Reconstruction
// void 
// static
// static void
// public
// public void
// public static void 
// public static String
// private 
// private void
// private static
// private static void
// class
// enum 
// struct