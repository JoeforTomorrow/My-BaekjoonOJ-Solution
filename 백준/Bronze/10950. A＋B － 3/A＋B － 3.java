import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int iter = in.nextInt();

        for (int i = 0; i < iter; i++) {
            int first = in.nextInt();
            int second = in.nextInt();
            int sum = first + second;
            System.out.println(sum);
        }

        in.close();

    }
}
