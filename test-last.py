class BankAccount:
    """A simple bank account with deposits, withdrawals, and a transfer feature."""
 
    # The minimum balance the account is allowed to reach.
    MINIMUM_BALANCE = 0.0
 
    def __init__(self, owner: str, initial_balance: float = 0.0):
        """
        Create a new BankAccount.
 
        Parameters
        ----------
        owner : str
            The name of the account holder.  Must be a non-empty string.
        initial_balance : float
            Starting balance.  Must be >= MINIMUM_BALANCE.
 
        Raises
        ------
        ValueError
            If owner is empty or initial_balance is negative.
        """
        if not owner or not owner.strip():
            raise ValueError("Owner name cannot be empty.")
        if initial_balance < self.MINIMUM_BALANCE:
            raise ValueError(
                f"Initial balance cannot be negative (got {initial_balance})."
            )
 
        self._owner = owner.strip()
        self._balance = float(initial_balance)
        self._transactions: list[str] = []  # human-readable log
 
    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------
 
    @property
    def owner(self) -> str:
        """The account holder's name (read-only)."""
        return self._owner
 
    @property
    def balance(self) -> float:
        """Current account balance (read-only)."""
        return self._balance
 
    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------
 
    def deposit(self, amount: float) -> float:
        """
        Add money to the account.
 
        Parameters
        ----------
        amount : float
            The amount to deposit.  Must be strictly greater than 0.
 
        Returns
        -------
        float
            The new balance after the deposit.
 
        Raises
        ------
        ValueError
            If amount is zero or negative.
        """
        if amount <= 0:
            raise ValueError(f"Deposit amount must be positive (got {amount}).")
        self._balance += amount
        self._transactions.append(f"deposit  +{amount:.2f}  -> {self._balance:.2f}")
        return self._balance
 
    def withdraw(self, amount: float) -> float:
        """
        Remove money from the account.
 
        Parameters
        ----------
        amount : float
            The amount to withdraw.  Must be strictly greater than 0 and
            no larger than the current balance.
 
        Returns
        -------
        float
            The new balance after the withdrawal.
 
        Raises
        ------
        ValueError
            If amount is zero or negative.
        InsufficientFundsError
            If amount exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError(f"Withdrawal amount must be positive (got {amount}).")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f}; "
                f"current balance is only {self._balance:.2f}."
            )
        self._balance -= amount
        self._transactions.append(f"withdraw -{amount:.2f}  -> {self._balance:.2f}")
        return self._balance
 
    def transfer(self, amount: float, target: "BankAccount") -> None:
        """
        Move money from this account to another BankAccount.
 
        This is equivalent to:
            self.withdraw(amount)
            target.deposit(amount)
 
        Parameters
        ----------
        amount : float
            The amount to transfer.  Same rules as withdraw().
        target : BankAccount
            The destination account.  Must not be this same account.
 
        Raises
        ------
        ValueError
            If target is the same object as self, or if amount is invalid.
        InsufficientFundsError
            If this account does not have enough funds.
        """
        if target is self:
            raise ValueError("Cannot transfer money to the same account.")
        # withdraw() and deposit() handle their own validation.
        self.withdraw(amount)
        target.deposit(amount)
        self._transactions.append(
            f"transfer -{amount:.2f} to {target.owner}"
        )
 
    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------
 
    def get_transaction_count(self) -> int:
        """Return the total number of transactions recorded."""
        return len(self._transactions)
 
    def get_history(self) -> list[str]:
        """Return a copy of the transaction log (oldest first)."""
        return list(self._transactions)
 
    def __repr__(self) -> str:
        return f"BankAccount(owner={self._owner!r}, balance={self._balance:.2f})"
 
 
# ---------------------------------------------------------------------------
# Custom exception
# ---------------------------------------------------------------------------
 
class InsufficientFundsError(Exception):
    """Raised when a withdrawal or transfer would drop the balance below zero."""
 
 
# ---------------------------------------------------------------------------
# Quick manual smoke-test – run this file directly to see basic behaviour:
#     python bank_account.py
# ---------------------------------------------------------------------------
 
if __name__ == "__main__":
    alice = BankAccount("Alice", initial_balance=500.00)
    bob = BankAccount("Bob")
 
    alice.deposit(250.00)
    alice.withdraw(100.00)
    alice.transfer(200.00, bob)
 
    print(alice)
    print(bob)
    print("\nAlice's history:")
    for entry in alice.get_history():
        print(" ", entry)
    print("\nBob's history:")
    for entry in bob.get_history():
        print(" ", entry)
 
