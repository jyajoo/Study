import java.util.Scanner;
public class JAVA {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		double a, b;
		a = scanner.nextInt();
		b = scanner.nextInt();

		System.out.println(a/b);

		scanner.close();
	}
}