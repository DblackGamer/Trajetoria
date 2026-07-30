import java.util.Scanner;
public class areadocirculo{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        double π = 3.14159;
        
        System.out.println("Digite o Raio para calcular a area do circulo.");
        int raio = input.nextInt();

        double area = π * (raio* raio);
        System.out.println("A Area do circulo e: " + area);
    }
}