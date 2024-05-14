import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        int numero = 0;

        System.out.println("Digite um número: ");
        numero = objScan.nextInt();

        if (primo(numero)){
            System.out.println(numero + " é primo.");
        } else {
            System.out.println(numero + " não é primo.");
        }
    }

    public static boolean primo(int numero){
        if (numero <= 1){
            return false;
        } else {
            for (int i = 2; i < numero; i++) {
                if (numero % i == 0){
                    return false;
                }
            }
            return true;
        }
    }
}
