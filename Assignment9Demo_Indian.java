import java.util.ArrayList;
import java.util.List;

public class Assignment9Demo_Indian {
    public static void main(String[] args) {
        System.out.println("\n╔════════════════════════════════════════════════════════════╗");
        System.out.println("║          Indian Banking System - OOP Concepts Demo         ║");
        System.out.println("╚════════════════════════════════════════════════════════════╝\n");

        // ============ 1. Encapsulation Demo ============
        System.out.println("\n▶ 1. Encapsulation Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9Account_Indian basicAccount = new Assignment9Account_Indian("ACC001", "Raj Kumar", 50000);
        basicAccount.display();
        basicAccount.deposit(10000);
        basicAccount.withdraw(5000);
        basicAccount.display();

        // ============ 2. Constructor Overloading Demo ============
        System.out.println("\n▶ 2. Constructor Overloading Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9Account_Indian account1 = new Assignment9Account_Indian("ACC002", "Priya Sharma", 100000);
        Assignment9Account_Indian account2 = new Assignment9Account_Indian("ACC003", "Amit Patel");
        
        System.out.println("Account 1 - Balance: ₹" + account1.getBalance());
        System.out.println("Account 2 - Balance: ₹" + account2.getBalance());

        // ============ 3. Inheritance Demo ============
        System.out.println("\n▶ 3. Inheritance Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9SavingsAccount_Indian savingsAccount = new Assignment9SavingsAccount_Indian(
            "SAV001", "Vijay Singh", 200000, 5.5
        );
        savingsAccount.display();
        savingsAccount.applyInterest();
        savingsAccount.display();

        // ============ 4. Method Overriding Demo ============
        System.out.println("\n▶ 4. Method Overriding Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9CurrentAccount_Indian currentAccount = new Assignment9CurrentAccount_Indian(
            "CUR001", "Neeta Verma", 150000, 100000
        );
        currentAccount.display();
        
        System.out.println("\nAttempting to withdraw ₹80,000:");
        currentAccount.withdraw(80000);
        currentAccount.display();

        // ============ 5. Polymorphism Demo ============
        System.out.println("\n▶ 5. Polymorphism Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        List<Assignment9Account_Indian> accounts = new ArrayList<>();
        accounts.add(new Assignment9Account_Indian("ACC004", "Rahul Gupta", 75000));
        accounts.add(new Assignment9SavingsAccount_Indian("SAV002", "Seema Sharma", 300000, 6.0));
        accounts.add(new Assignment9CurrentAccount_Indian("CUR002", "Anil Kumar", 250000, 75000));
        accounts.add(new Assignment9SavingsAccount_Indian("SAV003", "Deepa Verma", 150000, 4.5));

        System.out.println("\nAll Account Details:\n");
        for (Assignment9Account_Indian account : accounts) {
            account.display();
        }

        // ============ 6. Validation & Exception Handling Demo ============
        System.out.println("\n▶ 6. Validation & Exception Handling:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9Account_Indian testAccount = new Assignment9Account_Indian("ACC005", "Test User", 50000);
        
        // Invalid withdrawal
        try {
            System.out.println("\n❌ Attempting invalid withdrawal:");
            testAccount.withdraw(100000);
        } catch (IllegalArgumentException e) {
            System.out.println("Error caught: " + e.getMessage());
        }
        
        // Invalid deposit
        try {
            System.out.println("\n❌ Attempting invalid deposit:");
            testAccount.deposit(-5000);
        } catch (IllegalArgumentException e) {
            System.out.println("Error caught: " + e.getMessage());
        }

        // ============ 7. Overdraft Demo ============
        System.out.println("\n▶ 7. Overdraft Facility Demonstration:");
        System.out.println("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
        
        Assignment9CurrentAccount_Indian overdraftAccount = new Assignment9CurrentAccount_Indian(
            "CUR003", "Mohan Sharma", 30000, 50000
        );
        overdraftAccount.display();
        
        System.out.println("\nAttempting to withdraw ₹60,000:");
        overdraftAccount.withdraw(60000);
        overdraftAccount.display();

        System.out.println("\n╔════════════════════════════════════════════════════════════╗");
        System.out.println("║                    Demo Complete                           ║");
        System.out.println("╚════════════════════════════════════════════════════════════╝\n");
    }
}
