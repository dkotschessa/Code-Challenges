from datetime import datetime, timedelta

from simple_property import Promo


def test_expired():
    #current_date = datetime.now()
    expiration_date = datetime.now() - timedelta(days=2)
    name = "expired product"
    expired_case = Promo(name, expiration_date)
    assert expired_case.expired == True

def test_notexpired():
    #current_date = datetime.now()
    expiration_date = datetime.now() + timedelta(days=2)
    name = "nonexpired product"
    expired_case = Promo(name, expiration_date)
    assert expired_case.expired == False
