from creditclass import CreditCard


# The body of our new constructor relies upon making a call to the inherited constructor to perform most of the initialization. The mechanism for calling the inherited constructor relies on the syntax super()

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interests and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        customer the name of the customer (e.g., John Bowman )
         bank the name of the bank (e.g., California Savings )
        acnt the acount identifier (e.g., 5391 0375 9387 5309 )
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, back, acnt, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed
        Return False and assess $5 fee if charge is denied
        """
        success = super().charge(price)   # call inherited method
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
            
