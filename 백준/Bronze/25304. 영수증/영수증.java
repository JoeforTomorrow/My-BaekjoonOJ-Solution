import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
 
		Scanner in = new Scanner(System.in);
        int total = in.nextInt();
        int iter = in.nextInt();
        int sum = 0;

        for(int i=0;i<iter;i++){
            int price = in.nextInt();
            int count = in.nextInt();
            sum = sum + price * count;
        }
        in.close();
        
        if (sum == total){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
	}
}
