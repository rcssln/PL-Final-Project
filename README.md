# Calcute

**A small, sweet programming language for math.**

CMPSC 132: Programming Languages — Final Project (1st Semester, A.Y. 2025–2026)

**Group members:**
1. Bullanday, Luis T.
2. Bagasani, Nythan
3. Bonifacio, Nathaniel
4. Sambat, Reymart
5. Polendey, Stephen Jay

---

## 1. What is Calcute?

Calcute is a simple programming language that does arithmetic.
The name is **calc + cute**: a calculator language that is small and cute.

You write math the way you normally would, and Calcute gives you the answer:

```
cute> 7 + 6 * 10
67
```

What it can do:
- Add, subtract, multiply, divide, remainder and power: `+  -  *  /  %  ^`
- Whole numbers (`67`), decimals (`3.14`) and negative numbers (`-5`)
- Parentheses: `(2 + 3) * 4`
- Variables: `price = 250`
- Show text and answers: `print "Total:", price * 3`
- Comments: `# this line is ignored`
- Clear error messages when something is wrong

---

## 2. How to run it

You only need **Python 3.8 or newer**. Nothing else needs to be installed.

Open a terminal in this folder and type one of these:

| I want to... | Type this |
|---|---|
| Type math and see answers right away | `python main.py` |
| Run a program file | `python main.py examples/basics.cute` |
| Run the automatic tests | `python -m unittest discover tests -v` |

In the interactive mode (`cute>`), you can also type:
- `help` to see examples
- `vars` to see your variables
- `exit` to quit

---

## 3. Writing Calcute (cheat sheet)

```
# A comment starts with #

x = 10                 # store 10 in x
x * 2                  # shows 20
print "x is", x        # shows: x is 10

7 / 2                  # shows 3.5
8 / 2                  # shows 4  (exact answers stay whole numbers)
7 % 2                  # shows 1  (remainder)
2 ^ 10                 # shows 1024  (power)
```

**Order of operations:** Calcute follows the order you learned in school.

| Done first | Operator | Example |
|---|---|---|
| 1 | `( )` parentheses | `(2 + 3) * 4` = 20 |
| 2 | `^` power | `2 ^ 3 ^ 2` = 512 (done right to left) |
| 3 | `-` negative | `-2 ^ 2` = -4 |
| 4 | `*` `/` `%` | `7 + 6 * 10` = 67 |
| 5 | `+` `-` | `100 - 20 - 13` = 67 (done left to right) |

---

## 4. How Calcute works

Calcute reads your code in **3 steps**, like an assembly line:

```
your code  →  1. LEXER  →  2. PARSER  →  3. INTERPRETER  →  answer
              lexer.py    syntax_parser.py  interpreter.py
```

The example `7 + 6 * 10` goes through each step like this.

### Step 1 — Lexer: split the text into pieces ("tokens")

The lexer works like reading the words of a sentence. It cuts the code into small pieces:

```
7 + 6 * 10   →   [7]  [+]  [6]  [*]  [10]
```

Spaces and comments are thrown away. If it finds a character that is not allowed, such as `$`, it reports an error.

### Step 2 — Parser: check the grammar and build a tree

The parser works like checking that a sentence is correct. It makes sure the pieces are in a valid order. For example, `5 +` is wrong because something is missing after `+`.

Then it builds a **tree** that shows what to calculate first:

```
        +
       / \
      7   *
         / \
        6   10
```

The `*` is lower in the tree, so it is done **first** (6 × 10 = 60). Then 7 + 60 = 67.

### Step 3 — Interpreter: calculate the answer

The interpreter starts at the bottom of the tree and works its way up:

```
6 * 10 = 60   →   7 + 60 = 67   →   shows 67
```

---

## 5. No if/else for the operations

The simple way to build a calculator is a long if/else chain:

```python
# We do NOT do this:
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif ...
```

Calcute uses a **table** (a Python dictionary) instead. Each operator points to the function that does the math:

```python
OPERATIONS = {
    "+": operator.add,       # adds
    "-": operator.sub,       # subtracts
    "*": operator.mul,       # multiplies
    "/": divide,             # divides
    "%": operator.mod,       # remainder
    "^": power,              # power
}

result = OPERATIONS[op](a, b)    # look up the operator, then use it
```

**Why this is better:**
- It is shorter and easier to read.
- Adding a new operator takes **one new line**.
- It is the same for every operator, so there is less chance of mistakes.

The same table idea is used in other places too: the interactive commands (`COMMANDS`), the error messages (`ERROR_MESSAGES`), and the steps that run each part of the tree (`evaluators`, `executors`).

---

## 6. Error handling

Calcute never crashes. It always explains what went wrong and **points at the problem** with `^`.

There are two kinds of errors:

**Syntax Error**: the code is written in the wrong format.
```
cute> 5 +
Syntax Error at line 1, column 4:
    5 +
       ^
Expected a number, a variable or '(' but found the end of the program.
```
More examples: `(2 + 3` (missing `)`), `3 4` (missing operator), `2 $ 3` (unknown symbol).

**Runtime Error**: the format is right, but the answer cannot be calculated.
```
cute> 10 / 0
Runtime Error at line 1, column 4:
    10 / 0
       ^
Cannot divide by zero.
```
More examples: `y + 1` when `y` has no value yet, `9 ^ 9 ^ 9` (too large), `(-8) ^ 0.5` (not a real number).

Calcute checks the **whole program for syntax errors before running anything**, so a mistake on the last line is caught before the first line runs.

---

## 7. Files in this project

| File | What it does |
|---|---|
| `main.py` | Starts Calcute: interactive mode or running a file |
| `lexer.py` | Step 1: splits code into tokens |
| `syntax_parser.py` | Step 2: checks grammar and builds the tree |
| `interpreter.py` | Step 3: calculates the answer |
| `errors.py` | The error message format (line, column, `^`) |
| `examples/` | Sample programs: `basics.cute`, `variables.cute`, `error_demo.cute` |
| `tests/` | Automatic tests that check the answers and errors |

### Classes and their variables

| Class | File | Variables |
|---|---|---|
| `Token` | lexer.py | `kind`: what type of piece it is (NUMBER, NAME, `+`, ...) · `text`: the actual characters · `line`, `column`: where it is in the code |
| `Lexer` | lexer.py | `source`: the code to split |
| `Parser` | syntax_parser.py | `tokens`: the pieces from the lexer · `position`: which piece it is reading now · `primary_rules`: table of how to read a number, a variable or `( )` |
| `Interpreter` | interpreter.py | `variables`: saved variables and their values · `output`: where answers are shown · `evaluators`: table of how to calculate each part of the tree · `executors`: table of how to run each kind of line |
| `CalcuteError` | errors.py | `kind`: "Syntax Error" or "Runtime Error" · `message`: what went wrong · `line`, `column`: where it happened |

---

## 8. PL evaluation criteria

| Criterion | Question it asks | How Calcute does it |
|---|---|---|
| **Readability** | Is the code easy to read? | It looks like normal math: `(2 + 3) * 4`. There is only one keyword (`print`) and comments are allowed. |
| **Writability** | Is the code easy to write? | Programs are short: no declarations, no data types, no semicolons. |
| **Reliability** | Does it behave correctly and catch mistakes? | Every mistake gets a clear error with its exact location. Division by zero and undefined variables are caught. Whole numbers are always exact. Automatic tests check the answers. |
| **Cost** | Is it cheap to learn and use? | Anyone who knows basic math can learn it in minutes. It is free and only needs Python. The code is small, so it is easy to fix and improve. |

---

## 9. Grammar (the rules of the language)

The grammar lists which arrangements of tokens are allowed. Rules near the bottom are done first.

```
statement  = "print" item { "," item }  |  NAME "=" expression  |  expression
item       = TEXT | expression
expression = term { ("+" | "-") term }           ← add, subtract (done last)
term       = unary { ("*" | "/" | "%") unary }   ← multiply, divide, remainder
unary      = "-" unary | power                   ← negative numbers
power      = primary [ "^" unary ]               ← power
primary    = NUMBER | NAME | "(" expression ")"  ← numbers, variables, ( ) (done first)
```

How to read it: `{ }` means "repeat 0 or more times", `[ ]` means "optional", and `|` means "or".
Each rule is one method in `syntax_parser.py` with the same name.
