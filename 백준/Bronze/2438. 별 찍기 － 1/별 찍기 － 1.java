import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);
        int iter = in.nextInt();
        int cnt = 1;

        for (int i = 0; i < iter; i++) {
            for (int j = 0; j < cnt; j++) {
                System.out.print("*");
            }
            System.out.println("");
            cnt += 1;
        }

        in.close();

    }
}
