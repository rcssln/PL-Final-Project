"""
test_calcute.py - Automatic tests for Calcute.

Run from the project folder with:   python -m unittest discover tests -v
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from errors import CalcuteError       # noqa: E402
from interpreter import Interpreter  # noqa: E402

def calc(source):
    """Run source and return everything it displayed, as a list of lines."""
    lines = []
    Interpreter(output=lines.append).run(source)
    return lines

# Program -> the line it should display.
CORRECT_RESULTS = {
    "1 + 2": "3", "10 - 4": "6", "6 * 7": "42", "8 / 2": "4", "7 / 2": "3.5",
    "7 % 3": "1", "2 ^ 10": "1024", "2 ^ 100": str(2 ** 100),
    "2 + 3 * 4": "14", "(2 + 3) * 4": "20", "10 - 4 - 3": "3", "2 ^ 3 ^ 2": "512",
    "-2 ^ 2": "-4", "(-2) ^ 2": "4", "2 * -3": "-6", "2 ^ -1": "0.5",
    "0.1 + 0.2": "0.3", "2.5 * 2": "5", "x = 5\nx * 2": "10",
    'print "Total:", 3 * 4': "Total: 12",
}

SYNTAX_ERRORS = ["5 +", "(2 + 3", "3 4", "2 * * 3", ")", "5 = x",
                 "2 $ 3", "1.2.3", "print", '"text"', "x ="]

RUNTIME_ERRORS = ["1 / 0", "1 % 0", "0 ^ -1", "y + 1", "9 ^ 9 ^ 9",
                  "(-8) ^ 0.5", "10.0 ^ 400"]

class TestCalcute(unittest.TestCase):

    def test_correct_results(self):
        for source, expected in CORRECT_RESULTS.items():
            with self.subTest(source=source):
                self.assertEqual(calc(source), [expected])

    def test_syntax_errors(self):
        for source in SYNTAX_ERRORS:
            with self.subTest(source=source), self.assertRaises(CalcuteError) as caught:
                calc(source)
            self.assertEqual(caught.exception.kind, "Syntax Error")

    def test_runtime_errors(self):
        for source in RUNTIME_ERRORS:
            with self.subTest(source=source), self.assertRaises(CalcuteError) as caught:
                calc(source)
            self.assertEqual(caught.exception.kind, "Runtime Error")

    def test_nothing_runs_if_there_is_a_syntax_error(self):
        with self.assertRaises(CalcuteError):
            calc("print 1\nprint 2 +")      # line 1 must not print

    def test_error_points_at_the_problem(self):
        source = "x = 1\nx / 0"
        with self.assertRaises(CalcuteError) as caught:
            calc(source)
        self.assertEqual((caught.exception.line, caught.exception.column), (2, 3))
        self.assertIn("    x / 0\n      ^", caught.exception.show(source))

if __name__ == "__main__":
    unittest.main()