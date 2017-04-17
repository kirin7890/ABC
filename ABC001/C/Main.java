import java.util.*;
import java.math.*;
public class Main{
  public static final double defD = 11.25*10;
  public static final double oneD = (360.0/16)*10;

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();

    String dir;
    int wind;

    double b2 = Math.round(((double)b*10.0/60.0))/10.0;

    if(b <= 0.2*60){
      dir = "C";
    } else if(a < defD + oneD*0 || a >= defD + oneD*15 ){
      dir = "N";
    } else if(a < defD + oneD*1){
      dir = "NNE";
    } else if(a < defD + oneD*2){
      dir = "NE";
    } else if(a < defD + oneD*3){
      dir = "ENE";
    } else if(a < defD + oneD*4){
      dir = "E";
    } else if(a < defD + oneD*5){
      dir = "ESE";
    } else if(a < defD + oneD*6){
      dir = "SE";
    } else if(a < defD + oneD*7){
      dir = "SSE";
    } else if(a < defD + oneD*8){
      dir = "S";
    } else if(a < defD + oneD*9){
      dir = "SSW";
    } else if(a < defD + oneD*10){
      dir = "SW";
    } else if(a < defD + oneD*11){
      dir = "WSW";
    } else if(a < defD + oneD*12){
      dir = "W";
    } else if(a < defD + oneD*13){
      dir = "WNW";
    } else if(a < defD + oneD*14){
      dir = "NW";
    } else {
      dir = "NNW";
    }



    if(b2 <= 0.2){
      wind = 0;
    } else if(b2 <= 1.5){
      wind = 1;
    } else if(b2 <= 3.3){//3.3*60=198
      wind = 2;
    } else if(b2 <= 5.4){//5.4*60=324
      wind = 3;
    } else if(b2 <= 7.9){
      wind = 4;
    } else if(b2 <= 10.7){
      wind = 5;
    } else if(b2 <= 13.8){
      wind = 6;
    } else if(b2 <= 17.1){
      wind = 7;
    } else if(b2 <= 20.7){
      wind = 8;
    } else if(b2 <= 24.4){
      wind = 9;
    } else if(b2 <= 28.4){
      wind = 10;
    } else if(b2 <= 32.6){
      wind = 11;
    } else {
      wind = 12;
    }

    System.out.println(dir + " " +wind);
  }
}
