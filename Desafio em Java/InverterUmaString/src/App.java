import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        String entrada = "", saida = "";

        System.out.println("--Inverter uma String--\n");

        System.out.println("Digite uma palavra ou frase: ");
        entrada = objScan.nextLine();

        for (int i = entrada.length() - 1; i >= 0; i--){
            saida += entrada.charAt(i);
        }
        System.out.println(saida);
    }
}
