public class Assignment9CurrentAccount_Indian extends Assignment9Account_Indian {
    private double overdraftLimit;

    public Assignment9CurrentAccount_Indian(String accountNumber, String ownerName, double balance, double overdraftLimit) {
        super(accountNumber, ownerName, balance);
        assert overdraftLimit >= 0 : "Overdraft limit cannot be negative";
        this.overdraftLimit = overdraftLimit;
    }

    public Assignment9CurrentAccount_Indian(String accountNumber, String ownerName, double balance) {
        this(accountNumber, ownerName, balance, 50000);
    }

    public Assignment9CurrentAccount_Indian(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0, 50000);
    }

    public double getOverdraftLimit() {
        return overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive");
        }
        double availableFunds = getBalance() + overdraftLimit;
        if (amount > availableFunds) {
            throw new IllegalArgumentException("Insufficient available funds");
        }
        
        double newBalance = getBalance() - amount;
        if (newBalance < 0) {
            System.out.println("⚠️ Using overdraft facility");
        }
        
        super.withdraw(amount);
    }

    public double getAvailableFunds() {
        return getBalance() + overdraftLimit;
    }

    public boolean isOverdrawn() {
        return getBalance() < 0;
    }

    @Override
    public void display() {
        System.out.println("\n========== Current Account Details ==========");
        System.out.println("Account Number: " + getAccountNumber());
        System.out.println("Owner Name: " + getOwnerName());
        System.out.println("Balance: ₹" + String.format("%.2f", getBalance()));
        System.out.println("Overdraft Limit: ₹" + String.format("%.2f", overdraftLimit));
        System.out.println("Available Funds: ₹" + String.format("%.2f", getAvailableFunds()));
        if (isOverdrawn()) {
            System.out.println("Status: ⚠️ Overdrawn");
        } else {
            System.out.println("Status: ✓ Normal");
        }
        System.out.println("==============================================");
    }
}
