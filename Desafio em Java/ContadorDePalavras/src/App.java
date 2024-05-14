import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        String frase = "";

        System.out.println("--Contador de Palavras--\n");

        System.out.println("Digite uma frase: ");
        frase = objScan.nextLine();
        String palavras[] = frase.split(" ");

        System.out.println("Nesta frase existe " + palavras.length + " palavras.");
    }
}
