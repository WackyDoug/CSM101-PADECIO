package PadecioCSM101;
import java.util.Arrays;
import java.util.Scanner;

public class Activity11_2PADECIO {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String[] names = {"Jenna", "Lilah", "Drought", 
				"Tilda", "Jennifer", "Allison"};
		
		
		System.out.print("Search a name in the list > ");
		String userInput = sc.nextLine();
		
		int truth = 0;
		for (int i = 1; i < names.length; i++) {
			
			if (userInput.equalsIgnoreCase(names[i])) {
				truth = 1;
				System.out.printf("Found (%s)", userInput);
				break;
			}
				
		}
		if (truth == 0) {
			System.out.printf("Not Found (%s)", userInput);
		}
		
	}

}
