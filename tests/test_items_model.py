from django.test import TestCase
from django.contrib.auth.models import User

from datetime import datetime

from items.models import Product, Transaction
from core.models import UserProfile, Role

class ItemModelTest(TestCase):

    def test_product_name(self):

        item = "potato"
        product = Product(name = item)
        self.assertEqual(product.name, item)


    def test_transaction_name(self):

        farmer = User(username="Farmer")
        product = Product(name="Potato")
        price = 10000
        quantity = 1000
        time = datetime.now()

        transaction = Transaction(name=product, created_by=farmer, price=price, quantity=quantity, created_at=time)

        self.assertEqual(transaction.name.name, product.name)
        self.assertEqual(transaction.created_by.username, farmer.username)
        self.assertEqual(transaction.price, price)
        self.assertEqual(transaction.quantity, quantity)
        self.assertIsInstance(transaction.created_at, datetime)



