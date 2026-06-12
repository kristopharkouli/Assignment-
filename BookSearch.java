import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {
    public static void main(String[] args) {

        ArrayList<String> books = new ArrayList<>();

        books.add("Harry Potter and the Sorcerer's Stone");
        books.add("The Lord of the Rings");
        books.add("The Alchemist");
        books.add("Introduction to Java Programming");
        books.add("Data Structures and Algorithms");

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word to search in book titles: ");
        String word = sc.nextLine().toLowerCase();

        System.out.println("\nBooks containing the word \"" + word + "\":");

        boolean found = false;

        for (String book : books) {
            if (book.toLowerCase().contains(word)) {
                System.out.println(book);
                found = true;
            }
        }

        if (!found) {
            System.out.println("No book found with the given word.");
        }

        sc.close();
    }
}
