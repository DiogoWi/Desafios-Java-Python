import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner objScan = new Scanner(System.in);
        float temperaturaCelsius = 0, temperaturaFahrenheit = 0;

        System.out.println("--Conversor de Temperatura--\n");

        System.out.println("Digite uma temperatura em Celsius: ");
        temperaturaCelsius = objScan.nextFloat();

        temperaturaFahrenheit = temperaturaCelsius * 9 / 5 + 32;

        System.out.println("A temperatura em " + temperaturaCelsius + "°C para Fahrenheit é: " + temperaturaFahrenheit + "°F");
    }
}
