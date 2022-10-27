# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""
import decimal
import unittest

from petstore_api.components.schema.money import Money


class TestMoney(unittest.TestCase):
    """Money unit test stubs"""

    def test_Money(self):
        """Test Money"""
        price = Money(
            currency='usd',
            amount='10.99'
        )
        self.assertEqual(price.amount.as_decimal_oapg, decimal.Decimal('10.99'))
        self.assertEqual(
            price,
            dict(currency='usd', amount='10.99')
        )


if __name__ == '__main__':
    unittest.main()
