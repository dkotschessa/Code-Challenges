"""
Write a simple Promo class. Its constructor receives two variables: 
name (which must be a string) and expires (which must be a datetime object).

Add a property called expired which returns a boolean value indicating 
whether the promo has expired or not.

Checkout the tests and datetime module for more info. Have fun!

"""
from datetime import datetime

NOW = datetime.now()


class Promo:
    
    def __init__(self, name, expirydate):
        self.date = datetime.now()
        self.expired = expirydate < self.date

    @property
    def expired(self):
        return self.expired
        