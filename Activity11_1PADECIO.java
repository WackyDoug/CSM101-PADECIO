package PadecioCSM101;
import java.util.Arrays;
import java.util.Scanner;

public class Activity11_1PADECIO {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] myArray = new int[11];
		
		
		for (int i = 1; i < myArray.length; i++) {
			System.out.printf("imput a intager #%d > ", i);
			int userInput = sc.nextInt();
			myArray[i] = userInput;
		}
		
		Arrays.sort(myArray);
		for (int i = 1; i < myArray.length; i++) {
			System.out.print(" | "+myArray[i]);
		}
		

	}

}
