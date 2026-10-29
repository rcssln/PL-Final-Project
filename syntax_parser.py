"""
syntax_parser.py - Step 2: check the grammar and build a syntax tree.

Grammar (from lowest to highest precedence):
    statement  = "print" item { "," item }  |  NAME "=" expression  |  expression
    item       = TEXT | expression
    expression = term { ("+" | "-") term }
    term       = unary { ("*" | "/" | "%") unary }
    unary      = "-" unary | power
    power      = primary [ "^" unary ]
    primary    = NUMBER | NAME | "(" expression ")"

The tree is made of tuples. The first item says what kind of node it is:
    ("number", 42)                      ("assign", name_token, expression)
    ("text", "Hello")                   ("print", [item, item, ...])
    ("variable", name_token)            ("show", expression)
    ("negate", expression)
    ("binary", operator_token, left, right)

For example, 2 + 3 * 4 becomes
    ("binary", +, ("number", 2), ("binary", *, ("number", 3), ("number", 4)))
so 3 * 4 is computed first.
"""

from errors import CalcuteError


class Parser:
    """Builds a syntax tree from the tokens. Each grammar rule is one method
    (this is called a recursive-descent parser).

    Class variables:
        tokens        -- the list of tokens from the lexer.
        position      -- index of the token currently being read.
        primary_rules -- which method reads a primary, by the kind of its first token.
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0
        self.primary_rules = {"NUMBER": self.number, "NAME": self.variable, "(": self.group}

    # ----- helpers -----

    def peek(self, ahead=0):
        """Look at a token without reading it (stays on EOF at the end)."""
        return self.tokens[min(self.position + ahead, len(self.tokens) - 1)]

    def advance(self):
        """Read the current token and move to the next one."""
        token = self.peek()
        self.position += 1
        return token

    def expect(self, kind, message):
        """Read a token of the given kind, or report a syntax error."""
        token = self.peek()
        if token.kind != kind:
            raise CalcuteError("Syntax Error", f"{message} Found {token.describe()}.", token)
        return self.advance()

    def skip_blank_lines(self):
        while self.peek().kind == "NEWLINE":
            self.advance()

    # ----- statements -----

    def parse(self):
        """Read the whole program and return its list of statements."""
        statements = []
        self.skip_blank_lines()
        while self.peek().kind != "EOF":
            statements.append(self.statement())
            if self.peek().kind != "EOF":
                self.expect("NEWLINE", "Expected the end of the line. Did you forget an operator?")
            self.skip_blank_lines()
        return statements

    def statement(self):
        if self.peek().text == "print":
            return self.print_statement()
        if self.peek().kind == "NAME" and self.peek(1).kind == "=":
            return self.assignment()
        return ("show", self.expression())

    def print_statement(self):
        self.advance()                      # the word 'print'
        items = [self.print_item()]
        while self.peek().kind == ",":
            self.advance()
            items.append(self.print_item())
        return ("print", items)

    def print_item(self):
        if self.peek().kind == "TEXT":
            return ("text", self.advance().text[1:-1])   # remove the quotes
        return self.expression()

    def assignment(self):
        name = self.advance()
        self.advance()                      # the '='
        return ("assign", name, self.expression())

    # ----- expressions -----

    def expression(self):
        return self.binary(self.term, ("+", "-"))

    def term(self):
        return self.binary(self.unary, ("*", "/", "%"))

    def binary(self, next_rule, operators):
        """Read  next_rule { operator next_rule }  from left to right."""
        node = next_rule()
        while self.peek().kind in operators:
            operator = self.advance()
            node = ("binary", operator, node, next_rule())
        return node

    def unary(self):
        if self.peek().kind == "-":
            self.advance()
            return ("negate", self.unary())
        return self.power()

    def power(self):
        base = self.primary()
        if self.peek().kind == "^":         # right to left: 2^3^2 = 2^(3^2)
            operator = self.advance()
            return ("binary", operator, base, self.unary())
        return base

    def primary(self):
        token = self.peek()
        rule = self.primary_rules.get(token.kind)
        if rule is None:
            raise CalcuteError("Syntax Error", "Expected a number, a variable or '(' "
                                            f"but found {token.describe()}.", token)
        return rule(self.advance())

    def number(self, token):
        value = float(token.text) if "." in token.text else int(token.text)
        return ("number", value)

    def variable(self, token):
        return ("variable", token)

    def group(self, open_bracket):
        inside = self.expression()
        self.expect(")", f"Missing ')' to close the '(' at column {open_bracket.column}.")
        return inside
