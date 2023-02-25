import sys
from unittest import TestCase

from ExampleContract import ExampleContract


class testContract(TestCase):

    def test_contract(self) -> None:
        self.subTest
        for rule in ExampleContract.rules:
            rule.check()
