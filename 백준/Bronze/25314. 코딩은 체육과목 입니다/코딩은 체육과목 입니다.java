import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
 
public class Main {
 
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
		int num = in.nextInt() / 4;
		String head = "long";
        String tail = "int";

        for(int i=0;i<num;i++){
            System.out.print(head + " ");
        }
        System.out.println(tail);
		in.close();
	}
}