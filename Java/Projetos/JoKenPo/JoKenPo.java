import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
public class JoKenPo{
    public static void main(String[] args) {
        Random gerador = new Random();
        Scanner input = new Scanner(System.in);
        List<String> Jogo = Arrays.asList("Pedra", "Papel", "Tesoura");
        System.out.println("Escolha Pedra, Papel ou Tesoura:");
        String Player1 = input.nextLine();
        String Computador= Jogo.get(gerador.nextInt(Jogo.size()));
        System.out.println("O jogador escolheu: " + Player1);
        System.out.println("O computador escolheu: " + Computador);
        if (Player1.equals(Computador)){
            System.out.println("Empate!");
        } else if (Player1.equals("Pedra") && Computador.equals("Tesoura") || Player1.equals("Papel") && Computador.equals("Pedra") || Player1.equals("Tesoura") && Computador.equals("Papel")){
            System.out.println("Jogador venceu!");
        } else {
            System.out.println("Computador venceu!");
        }

    }

}