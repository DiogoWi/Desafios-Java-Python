import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        int sequencia = 0;
        List<Integer> lista = new ArrayList<Integer>();

        System.out.println("--Ordenação de Números--\n");

        System.out.println("Digite quantos números você quer na sequência: ");
        sequencia = objScan.nextInt();

        for (int i = 0; i < sequencia; i++){
            System.out.println("\nDigite o " + (i + 1) + "º número: ");
            lista.add(objScan.nextInt());
        }

        lista.sort(null);
        System.out.println("Sua sequência em ordem crescente: " + lista);

        objScan.close();
    }
}
