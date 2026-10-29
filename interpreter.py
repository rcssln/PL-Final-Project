"""
interpreter.py - Step 3: walk the syntax tree and compute the results.

No if/else chain decides which operation to do. Instead:
  * OPERATIONS maps each operator symbol to the function that computes it.
  * Interpreter.evaluators / executors map each kind of tree node to the
    method that handles it.
"""
import math
import operator

from errors import CalcuteError
from lexer import Lexer
from syntax_parser import Parser

def divide(a, b):
    """'/' keeps exact answers whole: 8 / 2 = 4, but 7 / 2 = 3.5."""
    if isinstance(a, int) and isinstance(b, int) and a % b == 0:
        return a // b
    return a / b

def power(a, b):
    """'^' that refuses answers which are not real numbers or are far too big."""
    if a < 0 and b != int(b):
        raise ValueError("A negative number cannot have a fractional power.")
    if abs(a) > 1 and b * math.log2(abs(a)) > 13000:     # more than ~3,900 digits
        raise OverflowError
    return a ** b

# Operator symbol -> function that computes it.
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": divide,
    "%": operator.mod,
    "^": power,
}

# Python error -> message Calcute shows instead.
ERROR_MESSAGES = {
    ZeroDivisionError: "Cannot divide by zero.",
    OverflowError: "The result is too large to compute.",
}

def format_value(value):
    """Show decimals to 12 digits, so 0.1 + 0.2 shows as 0.3 and 2.5 * 2 as 5."""
    return f"{value:.12g}" if isinstance(value, float) else str(value)

class Interpreter:
    """Runs Calcute programs.

    Class variables:
        variables  -- dictionary of variable names and their values.
        output     -- function used to display results (normally print).
        evaluators -- which method computes each kind of expression node.
        executors  -- which method runs each kind of statement.
    """
    def __init__(self, output=print):
        self.variables = {}
        self.output = output
        self.evaluators = {
            "number": self.literal,
            "text": self.literal,
            "variable": self.variable,
            "negate": self.negate,
            "binary": self.binary,
        }
        self.executors = {
            "assign": self.assign,
            "print": self.print_values,
            "show": self.show,
        }

    def run(self, source):
        """Check the whole program for syntax errors first, then run it."""
        statements = Parser(Lexer(source).tokenize()).parse()
        for statement in statements:
            self.executors[statement[0]](statement)

    def evaluate(self, node):
        """Compute the value of a tree node using the method for its kind."""
        return self.evaluators[node[0]](node)

    # ----- statements -----

    def assign(self, statement):
        _, name, expression = statement
        self.variables[name.text] = self.evaluate(expression)

    def print_values(self, statement):
        values = [format_value(self.evaluate(item)) for item in statement[1]]
        self.output(" ".join(values))

    def show(self, statement):
        self.output(format_value(self.evaluate(statement[1])))

    # ----- expressions -----

    def literal(self, node):
        return node[1]

    def variable(self, node):
        name = node[1]
        if name.text not in self.variables:
            raise CalcuteError("Runtime Error", f"Undefined variable '{name.text}'. "
                                             f"Give it a value first, e.g. {name.text} = 10", name)
        return self.variables[name.text]

    def negate(self, node):
        return -self.evaluate(node[1])

    def binary(self, node):
        _, op, left, right = node
        a, b = self.evaluate(left), self.evaluate(right)
        try:
            result = OPERATIONS[op.kind](a, b)          # e.g. "+" -> operator.add
            if result in (math.inf, -math.inf):
                raise OverflowError
        except (ZeroDivisionError, OverflowError, ValueError) as error:
            message = ERROR_MESSAGES.get(type(error), str(error))
            raise CalcuteError("Runtime Error", message, op)
        return result