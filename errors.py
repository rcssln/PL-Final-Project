"""
errors.py - The error used for every problem in a Calcute program.
"""
class CalcuteError(Exception):
    """An error found in a Calcute program.

    Class variables:
        kind    -- "Syntax Error" (wrong format) or "Runtime Error" (cannot compute).
        message -- what went wrong, in plain words.
        line    -- line number of the problem (starting at 1).
        column  -- column number of the problem (starting at 1).
    """
    def __init__(self, kind, message, token):
        super().__init__(message)
        self.kind = kind
        self.message = message
        self.line = token.line
        self.column = token.column

    def show(self, source):
        """Return the error with the wrong line and a ^ under the problem."""
        code = source.split("\n")[self.line - 1]
        pointer = " " * (self.column - 1) + "^"
        return (f"{self.kind} at line {self.line}, column {self.column}:\n"
                f"    {code}\n"
                f"    {pointer}\n"
                f"{self.message}")