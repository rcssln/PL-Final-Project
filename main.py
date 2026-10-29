"""
main.py - Start Calcute.

    python main.py                 interactive mode: type a line, see the answer
    python main.py program.cute    run a program file
"""
import sys

from errors import CalcuteError
from interpreter import Interpreter, format_value

BANNER = """
  Calcute - small, sweet, and good at math!
  Type  help  for examples,  vars  for variables,  exit  to quit.
"""

HELP = """
  2 + 3 * 4          add, subtract, multiply      -> 14
  (2 + 3) * 4        parentheses go first         -> 20
  7 / 2              divide                       -> 3.5
  7 % 2              remainder                    -> 1
  2 ^ 10             power                        -> 1024
  -5 + 2             negative numbers             -> -3
  x = 10             store a value in a variable
  print "x is", x    show text and values
  # a note           a comment (ignored)
"""

def run(interpreter, source):
    """Run source code. Errors are shown neatly instead of crashing.
    Returns True if it ran without errors."""
    try:
        interpreter.run(source)
        return True
    except CalcuteError as error:
        print(error.show(source))
        return False
    except RecursionError:
        print("Error: the code has too many parentheses inside each other.")
        return False

def show_help(interpreter, line):
    print(HELP)

def show_variables(interpreter, line):
    for name, value in interpreter.variables.items():
        print(f"  {name} = {format_value(value)}")

# Words the interactive prompt understands. Anything else is run as code.
COMMANDS = {"help": show_help, "vars": show_variables}

def read_line():
    """Read one line from the user. Ctrl+C or Ctrl+Z counts as 'exit'."""
    try:
        return input("cute> ").strip()
    except (EOFError, KeyboardInterrupt):
        return "exit"

def interactive():
    """Read a line, run it, show the result, and repeat until 'exit'."""
    interpreter = Interpreter()     # one interpreter, so variables are remembered
    print(BANNER)
    line = read_line()
    while line != "exit":
        action = COMMANDS.get(line, run)
        action(interpreter, line)
        line = read_line()
    print("Goodbye!")

def run_file(path):
    """Run a whole program file. Returns the exit code (0 = success)."""
    try:
        with open(path, encoding="utf-8") as file:
            source = file.read()
    except OSError:
        print(f"Cannot open the file '{path}'.")
        return 1
    return 0 if run(Interpreter(), source) else 1

if __name__ == "__main__":
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)   # allow printing very long whole numbers
    if len(sys.argv) > 1:
        sys.exit(run_file(sys.argv[1]))
    interactive()