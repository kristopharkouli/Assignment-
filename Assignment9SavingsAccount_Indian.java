public class Assignment9SavingsAccount_Indian extends Assignment9Account_Indian {
    private double interestRate;

    public Assignment9SavingsAccount_Indian(String accountNumber, String ownerName, double balance, double interestRate) {
        super(accountNumber, ownerName, balance);
        assert interestRate >= 0 && interestRate <= 100 : "Interest rate must be between 0 and 100";
        this.interestRate = interestRate;
    }

    public Assignment9SavingsAccount_Indian(String accountNumber, String ownerName, double balance) {
        this(accountNumber, ownerName, balance, 4.0);
    }

    public Assignment9SavingsAccount_Indian(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0, 4.0);
    }

    public double getInterestRate() {
        return interestRate;
    }

    public void applyInterest() {
        double interest = getBalance() * (interestRate / 100);
        deposit(interest);
        System.out.println("Interest Applied: ₹" + String.format("%.2f", interest));
    }

    public double getAnnualInterest() {
        return getBalance() * (interestRate / 100);
    }

    @Override
    public void display() {
        System.out.println("\n========== Savings Account Details ==========");
        System.out.println("Account Number: " + getAccountNumber());
        System.out.println("Owner Name: " + getOwnerName());
        System.out.println("Balance: ₹" + String.format("%.2f", getBalance()));
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Annual Interest: ₹" + String.format("%.2f", getAnnualInterest()));
        System.out.println("=============================================");
    }
}
