import sys
from unittest import TestCase

from ExampleContract import ExampleContract
from ThenreturnContract import ThenreturnContract
from WhenContract import WhenContract
from ShallConstructorContract import ShallConstructorContract
from IfCalledWithContract import IfCalledWithContract
from MeanWhileContract import MeanWhileContract
from SuchThatContract import SuchThatContract


class testContract(TestCase):

    def test_contract(self) -> None:
        for rule in ExampleContract.rules:
            rule.check()

    def test_when(self) -> None:
        for rule in WhenContract.rules:
            rule.check()

    def test_constructor(self) -> None:
        for rule in ShallConstructorContract.rules:
            rule.check()

    def test_ifcalledwith(self) -> None:
        for rule in IfCalledWithContract.rules:
            rule.check()

    def test_meanwhile(self) -> None:
        for rule in MeanWhileContract.rules:
            rule.check()

    def test_suchthat(self) -> None:
        for rule in SuchThatContract.rules:
            rule.check()

    def test_thenreturn(self) -> None:
        for rule in ThenreturnContract.rules:
            rule.check()
