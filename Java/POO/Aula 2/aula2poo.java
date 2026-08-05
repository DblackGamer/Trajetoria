
public class aula2poo {
    
    public static void main(String[] args) {
        //Inicio
        class Animal{
            String Nome;
            void barulho(){
                System.out.println("Algum Som");
            }
            int idade;
            String CordoPelo;
            }
        class Cachorro extends Animal {
            @Override
            void barulho(){
                System.out.println("Au au Au");
            }
        }
        
        //Fim das classes.
        //Inicio dos Objetos
        Cachorro Malu = new Cachorro();
        Malu.Nome= "Malu";
        Malu.idade = 4;
        System.out.println(Malu.Nome);
        Malu.barulho();
        Malu.CordoPelo= "Branco";


    }
}
