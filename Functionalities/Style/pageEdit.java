package Style;
import java.util.Scanner;

public class pageEdit { 

  public static void main (String args[]){
      PageLayers layer = PageLayers.THIRD;
      System.out.println("test run");
      System.out.println();
      switch (layer){
        case FIRST:
        System.out.println("You reached the first level.");
        break;
        case SECOND:
        System.out.println("You reached the second level.");
        break;
        case THIRD:
        System.out.println("You reached the third level.");
        break;
        case FINAL:
        System.out.println("You reached the final level.");
        break;
      }
      for(PageLayers layer1:PageLayers.values()){
         System.out.println(layer1);
      }
    }
}

enum PageLayers{
   FIRST,
   SECOND,
   THIRD,
   FINAL
}