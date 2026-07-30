//Lets try figure out if the number insered is PAR or not
import java.util.Scanner;
public class PAR {
    public static void main(String[] args) {
        Scanner input= new Scanner(System.in);
        System.out.println("Digite o numero a verificar: ");
        double verifica = input.nextInt();
        if (verifica % 2 == 0) {
            System.out.println("PAR");
            

        }
        else{
            System.out.println("IMPAR");
        }
    }
}
