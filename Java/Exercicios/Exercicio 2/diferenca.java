import java.util.Scanner;

public class diferenca {
    public static void main(String[] args){
    Scanner input = new Scanner(System.in);

    double A = input.nextInt();
    double B = input.nextInt();
    double C = input.nextInt();
    double D = input.nextInt(); 
    
    double diferenca= (A*B - C*D);
    System.out.println("A diferenca e: " + diferenca);
}
}