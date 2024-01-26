# Calculator module for use in Homework 1.

class Calculator:
    """A number to do calculations on.
    
    Attributes:
        value -- float initial value of the number.
    """
    
    def __init__(self, value = 0):
        """Returns new Calculator with a default value of 0."""
        self.value = value
    
    def add(self, val2):
        """Adds input number to the stored value and stores."""
        self.value = self.value + val2
    
    def sub(self, val2):
        """Subtracts input number from the stored value and stores."""
        self.value = self.value - val2
    
    def mul(self, val2):
        """Multiplies input number by the stored value and stores."""
        self.value = self.value * val2
    
    def div(self, val2):
        """Divides the stored value by the input and stores."""
        self.value = self.value / val2
        
    def clr(self, val2):
        """Sets the Calculator's value to zero."""
        self.value = 0
        
    def result(self):
        """Just returns the Calculator's current value."""
        return self.value