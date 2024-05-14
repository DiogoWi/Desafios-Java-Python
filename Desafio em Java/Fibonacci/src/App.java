import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        int sequencia = 0, numeroAnterior = 0, numeroAtual = 1, aux = 0;

        System.out.println("--Fibonacci--\n");

        System.out.println("Digite quantos números da sequência Fibonacci você quer: ");
        sequencia = objScan.nextInt();
        System.out.println("--Sequência--\n");

        for (int i = 0; i < sequencia; i++){
            System.out.println(numeroAtual);

            aux = numeroAtual;
            numeroAtual += numeroAnterior;
            numeroAnterior = aux;
        }

        objScan.close();
    }
}
