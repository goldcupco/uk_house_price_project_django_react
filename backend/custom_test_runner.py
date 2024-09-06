# custom_test_runner.py

from django.test.runner import DiscoverRunner
from unittest import TextTestResult, TextTestRunner

class DetailedTestResult(TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.writeln(f"PASS: {self.getDescription(test)}")

    def addError(self, test, err):
        super().addError(test, err)
        self.stream.writeln(f"ERROR: {self.getDescription(test)}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.stream.writeln(f"FAIL: {self.getDescription(test)}")

class DetailedTestRunner(TextTestRunner):
    resultclass = DetailedTestResult

class CustomDiscoverRunner(DiscoverRunner):
    test_runner = DetailedTestRunner