import java.util.Scanner;
public class Exercicio5 {
    public static void main(String[] args) {
        // Fazer um levantamento de quanto de taxa pagar de acordo com quant voce recebe
        Scanner input = new Scanner(System.in);
        int sair= 1 ;
     
        do {
            System.out.println("Ola Mundo, para iniciarmos o calculo da taxa do salario siga as instrucoes abaixo");
            System.out.println("---------------------------------------------------------------------------------");
            System.out.println("1- Digite seu salario");
            System.out.println("2- Repetir");
            System.out.println("3- Sair");
            // sair = 0;
            sair = input.nextInt();
            if (sair == 1) {
                System.out.println("Voce escolheu a opcao 1. Digite o seu salario.");
       }

       }  while (sair!= 3);
       

    }
}
 