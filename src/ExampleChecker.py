from io import StringIO
import sys
from typing import Callable
from unittest.mock import MagicMock
from ExampleService import ExampleService
from shall.SideEffectChecker import SideEffectChecker


class ExampleChecker(SideEffectChecker[[ExampleService, int], int]):
    def setUp(self, service: Callable[[ExampleService, int], int], itself: ExampleService, value: int) -> None:
        self.service = service
        self.value = value
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def runTest(self) -> bool:
        serviceMock: ExampleService = MagicMock()
        self.service(serviceMock, self.value)
        output = self.capturedOutput.getvalue()
        return output == str(self.value)+"\n"
