import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        String sequencia = "";
        float media = 0;

        System.out.println("--Média de Números--\n");

        System.out.println("Digite uma sequência de números: ");
        sequencia = objScan.nextLine();
        String lista[] = sequencia.split(" ");

        for (int i = 0; i < lista.length; i++){
            media += Float.valueOf(lista[i]);
        }

        System.out.println("A média da sua sequência de números é: " + media / lista.length);
    }
}
