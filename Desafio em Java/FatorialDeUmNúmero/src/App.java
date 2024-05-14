import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        int numero = 0, fatorial = 1;

        System.out.println("--Fatorial de um Número--\n");

        System.out.println("Digite um número: ");
        numero = objScan.nextInt();

        for (int i = numero; i > 1; i--){
            fatorial *= i;
        }

        System.out.println("O fatorial de " + numero + " é " + fatorial);
    }
}
