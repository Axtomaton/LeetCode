public class Numberpalin{


    public static boolean num(int x){
        String nedw = "";

        for (int i = String.valueOf(x).length() -1;i > -1; i--){
            nedw += String.valueOf(x).charAt(i);}
            System.out.println(nedw);
        return (nedw.equals(String.valueOf(x)));
    }
public static void main(String[] args) {
    System.out.println(num(313));
}
}