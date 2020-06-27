import java.lang.Math;

class Magic8{

  public static void main(String [] args){
  int rand=(int) (Math.random()*8);
  System.out.println("Hello!");
  System.out.println("Ask me any question you would like.");
  String userQuestion="Will I be rich one day?";
  
  
  switch(rand){
    case 1:
    System.out.println("It is certain");
    break;

    case 2:
    System.out.println("It is decidedly so");
    break;

    case 3:
    System.out.println("Reply hazy, try again");
    break;

    case 4:
    System.out.println("Cannot predict now");
    break;

    case 5:
    System.out.println("Do not count on it");
    break;

    case 6:
    System.out.println("My sources say so");
    break;

    case 7:
    System.out.println("Outlook not so good");
    break;

    case 8:
    System.out.println("Signs point to yes");
    break;

  }

  }

}