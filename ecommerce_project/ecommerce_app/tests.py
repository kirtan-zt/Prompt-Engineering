from decimal import Decimal
from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Product


class ProductModelTestCase(TestCase):

    def test_product_creation_success(self):
        product = Product(name='Laptop-Pro 123', category='Electronics', price=Decimal('10.99'), stock=5)
        self.assertEqual(product.name, 'Laptop-Pro 123')
        self.assertEqual(product.category, 'Electronics')
        self.assertEqual(float(product.price), 10.99)
        self.assertEqual(product.stock, 5)

    def test_product_name_validation_success(self):
        product = Product(name='Valid Name-123', category='Test', price=Decimal('1.00'), stock=1)
        try:
            product.full_clean()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly for a valid name.")

    def test_product_category_validation_success(self):
        product = Product(name='Test', category='Valid Category-456', price=Decimal('1.00'), stock=1)
        try:
            product.full_clean()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly for a valid category.")

    def test_product_price_validation_success(self):
        product = Product(name='Test', category='Test', price=Decimal('10.99'), stock=1)
        try:
            product.full_clean()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly for a valid price.")

    def test_product_stock_validation_success(self):
        product = Product(name='Test', category='Test', price=Decimal('1.00'), stock=5)
        try:
            product.full_clean()
        except ValidationError:
            self.fail("full_clean() raised ValidationError unexpectedly for a valid stock.")

    def test_product_name_validation_failure_regex(self):
        product = Product(name='Invalid@Name', category='Test', price=Decimal('1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_name_validation_failure_symbols(self):
        product = Product(name='Name#$', category='Test', price=Decimal('1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_category_validation_failure_regex(self):
        product = Product(name='Test', category='Invalid Category!', price=Decimal('1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_price_validation_failure_zero(self):
        product = Product(name='Test', category='Test', price=Decimal('0.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_price_validation_failure_negative(self):
        product = Product(name='Test', category='Test', price=Decimal('-1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_stock_validation_failure_zero(self):
        product = Product(name='Test', category='Test', price=Decimal('1.00'), stock=0)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_stock_validation_failure_negative(self):
        product = Product(name='Test', category='Test', price=Decimal('1.00'), stock=-5)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_name_validation_failure_length(self):
        long_name = 'A' * 101
        product = Product(name=long_name, category='Test', price=Decimal('1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_product_category_validation_failure_length(self):
        long_category = 'B' * 101
        product = Product(name='Test', category=long_category, price=Decimal('1.00'), stock=1)
        with self.assertRaises(ValidationError):
            product.full_clean()