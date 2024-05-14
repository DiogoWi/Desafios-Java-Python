import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        float numero1 = 0, numero2 = 0;
        int operacao = 0;
        boolean aux = true;

        System.out.println("Digite o primeiro número: ");
        numero1 = objScan.nextFloat();

        System.out.println("Digite o segundo número: ");
        numero2 = objScan.nextFloat();

        System.out.println("Número das operações:");
        System.out.println("1 - Soma");
        System.out.println("2 - Subtração");
        System.out.println("3 - Multiplicação");
        System.out.println("4 - Divisão");

        while (aux){
            System.out.println("Escolha a opção desejada: ");
            operacao = objScan.nextInt();

            if (operacao == 1){
                System.out.println("A soma dos números é: " + (numero1 + numero2));
                aux = false;
            } else if (operacao == 2){
                System.out.println("A subtração dos números é: " + (numero1 - numero2));
                aux = false;
            } else if (operacao == 3){
                System.out.println("A multiplicação dos números é: " + (numero1 * numero2));
                aux = false;
            } else if (operacao == 4){
                System.out.println("A divisão dos números é: " + (numero1 / numero2));
                aux = false;
            } else {
                System.out.println("Esta opção não existe.");
            }
        }
    }
}
