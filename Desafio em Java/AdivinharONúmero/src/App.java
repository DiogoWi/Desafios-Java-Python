import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        int numero = 0;
        double sorteado = Math.random() * 100 + 1;
        boolean aux = true;

        System.out.println("--Adivinhar o Número--\n");

        System.out.println("Tente acertar qual número entre 1 e 100 foi sorteado");

        while (aux){
            System.out.println("Escolha um número: ");
            numero = objScan.nextInt();
            
            if (numero > (int)sorteado){
                System.out.println("O número que você digitou está a cima do sorteado.");
            } else if (numero < (int)sorteado){
                System.out.println("O número que você digitou está a baixo do sorteado.");
            } else {
                System.out.println("Parabéns você acertou!!!");
                aux = false;
            }
        }
        
        objScan.close();
    }
}
