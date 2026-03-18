class InsufficientFundsError(Exception): pass
def process_transaction(balance, amount, target_account):
    try:
        if amount > balance:
            raise InsufficientFundsError("Overdraft attempted.") 
        if len(target_account) != 8:
            raise ValueError("Incorrect account number format.") 
        # Simulating a timeout
        timeout = True 
        if timeout:
            raise ConnectionError("Transaction timed out. Please try again.") 
    except InsufficientFundsError as e:
        print(f"Bank Error: {e}")
    except (ValueError, ConnectionError) as e:
        print(f"System Error: {e}")
process_transaction(100, 500, "123")
                                           