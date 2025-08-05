from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from datetime import datetime

from items.models import Product, Transaction
from core.models import UserProfile, Role

from constants.enums import ErrorMessages

class ItemViewTest(TestCase):

    product = Product(name="Potato")

    person1 = User(username="person1")
    person2 = User(username="person2")
    person3 = User(username="person3")

    farmer = Role(name="Farmer")
    customer = Role(name="Customer")
    other = Role(name="Other")

    seller = UserProfile(user=person1, role=farmer)
    buyer = UserProfile(user=person2, role=customer)
    third_party = UserProfile(user=person3, role=other)

    def test_new_valid_transaction(self):

        price = 10000
        quantity = 1000
        time = datetime.now()

        transaction = Transaction(name=self.product, created_by=self.seller.user, price=price, quantity=quantity, created_at=time)

        self.assertFalse(transaction.is_sold)
        self.assertIsNone(transaction.sold_at)
        self.assertIsNone(transaction.sold_to)

    def test_customer_tries_to_sell(self):

        transaction = Transaction(name=self.product, created_by=self.buyer.user)

        self.assertRaisesMessage(ValidationError, ErrorMessages.TRANSACTION_FARMER_ACCESS)