import java.util.*;
public class Main{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    if (a<(0.1*1000)){
      System.out.println("00");
    } else if (a<1*1000){
      System.out.println("0" + a*10 /1000);
    } else if (a<=5*1000){
      System.out.println(a*10 /1000);
    } else if (a<=30*1000){
      System.out.println((a+50*1000)/1000);
    } else if (a<=70*1000){
      System.out.println(((a- 30*1000)/5 + 80*1000)/1000);
    } else{
      System.out.println(89);
    }
  }
}
