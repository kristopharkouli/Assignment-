public class Assignment9Account_Indian {
    private String accountNumber;
    private String ownerName;
    private double balance;

    public Assignment9Account_Indian(String accountNumber, String ownerName, double balance) {
        assert accountNumber != null && !accountNumber.isEmpty() : "Account number cannot be empty";
        assert ownerName != null && !ownerName.isEmpty() : "Owner name cannot be empty";
        assert balance >= 0 : "Balance cannot be negative";
        
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = balance;
    }

    public Assignment9Account_Indian(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0);
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        balance += amount;
        System.out.println("₹" + amount + " Deposited");
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance");
        }
        balance -= amount;
        System.out.println("₹" + amount + " Withdrawn");
    }

    public void display() {
        System.out.println("\n========== Account Details ==========");
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: ₹" + String.format("%.2f", balance));
        System.out.println("=====================================");
    }
}
