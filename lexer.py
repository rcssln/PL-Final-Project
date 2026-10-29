"""
lexer.py - Step 1: split the source text into tokens.

Example:   x = (2 + 3) * 4
becomes:   NAME(x)  =  (  NUMBER(2)  +  NUMBER(3)  )  *  NUMBER(4)  EOF
"""
import re
from errors import CalcuteError

# Each kind of token is described by a regular expression (Python's re module).
# The first pattern that matches wins, so ERROR (any other character) is last.
TOKEN_PATTERNS = re.compile(r"""
      (?P<NUMBER>  \d+\.\d+ | \d+ )        # 42 or 3.14
    | (?P<NAME>    [A-Za-z_]\w* )          # x, total, print
    | (?P<TEXT>    "[^"\n]*" )             # "Hello"
    | (?P<OP>      [-+*/%^()=,] )          # operators and punctuation
    | (?P<NEWLINE> \n )                    # end of a statement
    | (?P<SKIP>    [ \t\r]+ | \#[^\n]* )   # spaces and comments
    | (?P<ERROR>   . )                     # anything else is not allowed
""", re.VERBOSE)

# How some tokens are named in error messages.
SPECIAL_NAMES = {"NEWLINE": "the end of the line", "EOF": "the end of the program"}

class Token:
    """One piece of the program, such as a number, a name or an operator.

    Class variables:
        kind   -- "NUMBER", "NAME", "TEXT", "NEWLINE", "EOF",
                  or the symbol itself for operators ("+", "(", "=", ...).
        text   -- the exact characters from the source code.
        line   -- line number where the token starts (starting at 1).
        column -- column number where the token starts (starting at 1).
    """
    def __init__(self, kind, text, line, column):
        self.kind = kind
        self.text = text
        self.line = line
        self.column = column

    def describe(self):
        """Name of the token for error messages, e.g. '+' or the end of the line."""
        return SPECIAL_NAMES.get(self.kind, f"'{self.text}'")

class Lexer:
    """Turns the source text into a list of tokens.

    Class variables:
        source -- the program text to split.
    """
    def __init__(self, source):
        self.source = source

    def tokenize(self):
        """Return the list of tokens, ending with an EOF (end of file) token."""
        tokens = []
        line = 1
        line_start = 0          # where the current line begins in the source

        for match in TOKEN_PATTERNS.finditer(self.source):
            kind, text = match.lastgroup, match.group()
            token = Token(kind, text, line, match.start() - line_start + 1)

            if kind == "ERROR":
                raise CalcuteError("Syntax Error", f"The character {text} is not allowed.", token)
            if kind == "OP":
                token.kind = text   # operators are known by their own symbol
            if kind == "NEWLINE":
                line, line_start = line + 1, match.end()
            if kind != "SKIP":
                tokens.append(token)

        tokens.append(Token("EOF", "", line, len(self.source) - line_start + 1))
        return tokens