from creditclass import CreditCard


class PredatoryCreditCard(CreditCard):
    OVERLIMIT_FEE = 5
    def charge(self,price):
        success = super().charge(price)
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success


# A class-level data memeber is often used when there is some value, such as a constant that is to be shared by all instances of a class. In such a case, it would be unnecessari;y wasteful to have each instance store that value in its instance namespace
# The data memeber, OVERLIMIT_FEE, is entered into the PredatoryCreditCard class namespace because that assignment takes place within the immidiate scope of the class definition and without any qualifying identifier