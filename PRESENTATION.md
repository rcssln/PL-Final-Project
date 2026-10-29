# Calcute — Presentation Guide

How to demonstrate Calcute, split into 5 parts, one per member.

Each step has:
- **Do**: what to type
- **You'll see**: what appears on the screen
- **Say**: what to explain (what it is, how it works, why we did it this way)

| Member | Part | Topic |
|---|---|---|
| Bullanday, Luis T. | Part 1 | Starting Calcute and arithmetic (`basics.cute`) |
| Bagasani, Nythan | Part 2 | Variables (`variables.cute`) |
| Bonifacio, Nathaniel | Part 3 | Error handling, live demo |
| Sambat, Reymart | Part 4 | Errors in a file (`error_demo.cute`) and automatic tests |
| Polendey, Stephen Jay | Part 5 | How Calcute works and why there is no if/else |

> Before presenting: open a terminal in VS Code (``Ctrl+` ``) in the project folder. Run through the whole guide once so nothing surprises you.

---

## PART 1 — Starting Calcute and Arithmetic
**Presenter: Bullanday, Luis T.**

### 1A. Start Calcute

**Do:**
```
python main.py
```
**You'll see:**
```
  Calcute - small, sweet, and good at math!
  Type  help  for examples,  vars  for variables,  exit  to quit.

cute>
```
**Say:**
> "This is Calcute's interactive mode. `main.py` is the starting point of our program. We type one line of Calcute, it's calculated right away, and we see the answer. If you're new, typing `help` shows examples."

**Do:** type `help` to show the cheat sheet.

### 1B. Every operator

**Do:**
```
cute> 60 + 7
67
cute> 100 - 33
67
cute> 134 * 0.5
67
cute> 134 / 2
67
cute> 7 / 2
3.5
cute> 167 % 100
67
cute> 2 ^ 10
1024
cute> -5 + 2
-3
```
**Say:**
> "Calcute supports addition, subtraction, multiplication, division, remainder and power, plus negative numbers and decimals. `134 / 2` gives the whole number 67, but `7 / 2` gives 3.5. Calcute keeps answers as whole numbers when it can."

### 1C. Order of operations

**Do:**
```
cute> 7 + 6 * 10
67
cute> (7 + 6) * 10
130
cute> 2 ^ 3 ^ 2
512
cute> -2 ^ 2
-4
```
**Say:**
> "Calcute follows the math order we learned in school. In `7 + 6 * 10`, multiplication comes first, so it's 7 + 60 = 67. With parentheses, the addition is done first, so it becomes 130. Power is done right to left, so `2 ^ 3 ^ 2` is 2^9 = 512. And power comes before the negative sign, so `-2 ^ 2` is -4."

### 1D. Run basics.cute

**Do:** type `exit`, then:
```
python main.py examples/basics.cute
```
**You'll see:**
```
--- Every operator ---
60 + 7             = 67
100 - 33           = 67
134 * 0.5          = 67
134 / 2            = 67
167 % 100          = 67
8 ^ 2 + 3          = 67
--- Order of operations ---
7 + 6 * 10         = 67
(10 - 3) * 10 - 3  = 67
2 ^ 3 ^ 2 / 8 + 3  = 67
-2 ^ 2 + 71        = 67
(-2) ^ 2 + 63      = 67
100 - 20 - 13      = 67
--- Big whole numbers stay exact ---
67 ^ 20 = 3322737661703085672358476688602579601
```

**Say: What is basics.cute?**
> "basics.cute is a Calcute program saved in a file. It shows every operator and every order-of-operations rule together in one run."

**Say: How does it work?**
> "Each line uses `print` with two parts. The text in quotes is a label that shows the problem, like `"60 + 7 ="`. After the comma comes the actual math, `60 + 7`, which Calcute calculates. So each line displays the problem next to its answer."

**Say: Why this approach?**
> "We made every answer 67 on purpose, so the file checks itself. If Calcute did the order of operations wrong, the answer wouldn't be 67. For example, if it did `7 + 6 * 10` left to right, it would get 130. Seeing 67 on every line proves every rule is correct at a glance. We also used a file instead of typing by hand, so anyone can repeat the same test and get the same results. The last line, `67 ^ 20`, shows that Calcute handles very large whole numbers exactly, with no rounding."

---

## PART 2 — Variables
**Presenter: Bagasani, Nythan**

### 2A. Creating and using variables

**Do:** `python main.py`, then:
```
cute> price = 50
cute> quantity = 4
cute> price * quantity
200
```
**Say:**
> "A variable is a name that stores a value. `price = 50` saves 50 under the name `price`. Assignment shows nothing on the screen. It only remembers the value. Then we can use the name in math."

### 2B. Any name works

**Do:**
```
cute> my_grade = 95
cute> x1 = 7
cute> x1 * 2
14
cute> _bonus = 5
cute> Score = 10
cute> score = 3
cute> Score + score
13
```
**Say:**
> "We're not limited to `price`. A variable name can use letters, numbers and underscores, like `my_grade`, `x1` or `_bonus`, as long as it doesn't start with a number. Names are case-sensitive: `Score` and `score` are two different variables, which is why `Score + score` is 13."

### 2C. Changing a variable

**Do:**
```
cute> price = 60
cute> price * quantity
240
```
**Say:**
> "If we give `price` a new value, every calculation after that uses the new value."

### 2D. Variables, print and vars together

**Do:**
```
cute> total = price * quantity + _bonus
cute> print "Total:", total
Total: 245
cute> vars
  price = 60
  quantity = 4
  my_grade = 95
  Score = 10
  score = 3
  x1 = 7
  _bonus = 5
  total = 245
```
**Say:**
> "Variables can be built from other variables. `print` shows text and values together, and `vars` lists every variable Calcute remembers."

### 2E. Names that are not allowed

**Do:**
```
cute> 1x = 5
Syntax Error ... Found 'x'.
cute> my-grade = 5
Syntax Error ... Found '='.
cute> print = 5
Syntax Error ... found '='.
```
**Say:**
> "These names are rejected. A name can't start with a number, like `1x`. A dash isn't allowed, because Calcute reads `my-grade` as 'my minus grade'. And `print` is a keyword, so it can't be a variable name."

### 2F. Run variables.cute

**Do:** type `exit`, then:
```
python main.py examples/variables.cute
```
**You'll see:**
```
Subtotal: 750
Discount: 75
Total:    675
Circle area: 78.53975
100
```

**Say: What is variables.cute?**
> "variables.cute is a small real-life program: a shopping receipt and the area of a circle."

**Say: How does it work?**
> "First it stores the values: `price = 250`, `quantity = 3`, `discount = 0.10`. Then each step builds on the one before. `subtotal = price * quantity` gives 750. `savings = subtotal * discount` gives 75. `total = subtotal - savings` gives 675. The circle part uses `pi * radius ^ 2`. The last line, `(total + 25) / 7`, is a calculation with no `print`, so Calcute just shows the answer, 100."

**Say: Why this approach?**
> "We chose a real problem to show why variables matter. Without them, we would have to write `250 * 3 - 250 * 3 * 0.10`, which is hard to read. With variables, each line says what it means, like `total = subtotal - savings`. That's the readability criterion. It's also easy to change: update `price` once and everything recalculates. It mixes whole numbers and decimals too, which shows both work together."

---

## PART 3 — Error Handling (Live Demo)
**Presenter: Bonifacio, Nathaniel**

### 3A. Syntax Errors (wrong format)

**Do:** `python main.py`, then:
```
cute> 5 +
Syntax Error at line 1, column 4:
    5 +
       ^
Expected a number, a variable or '(' but found the end of the program.
```
**Say:**
> "A Syntax Error means the code is written in the wrong format. Here, the plus has nothing after it. Calcute doesn't crash. It gives the line and column, puts a `^` under the problem, and explains it."

**Do:**
```
cute> (2 + 3
Missing ')' to close the '(' at column 1. Found the end of the program.
cute> 3 4
Expected the end of the line. Did you forget an operator? Found '4'.
cute> 2 * * 3
Expected a number, a variable or '(' but found '*'.
cute> 2 $ 3
The character $ is not allowed.
cute> 1.2.3
The character . is not allowed.
```
**Say:**
> "A missing parenthesis, a missing operator, a doubled operator, an unknown symbol, a wrong number. Each one gets its own clear message."

### 3B. Runtime Errors (cannot compute)

**Do:**
```
cute> 10 / 0
Runtime Error at line 1, column 4:
    10 / 0
       ^
Cannot divide by zero.
cute> y + 1
Undefined variable 'y'. Give it a value first, e.g. y = 10
cute> (-8) ^ 0.5
A negative number cannot have a fractional power.
cute> 9 ^ 9 ^ 9
The result is too large to compute.
```
**Say:**
> "A Runtime Error means the format is correct, but the answer can't be calculated: dividing by zero, using a variable with no value, or a number too big to handle. `9 ^ 9 ^ 9` would freeze many programs, but Calcute checks the size first and stops safely."

### 3C. If someone asks: "Is a single number an error?"

```
cute> 22
22
```
> "No. A single number is a complete expression, like on a calculator. An error only happens when an operator is missing a number, like `22 +`, or when two numbers are missing an operator between them, like `22 5`."

---

## PART 4 — Errors in a File and Automatic Tests
**Presenter: Sambat, Reymart**

### 4A. Run error_demo.cute

**Do:** type `exit`, then:
```
python main.py examples/error_demo.cute
```
**You'll see:**
```
Items: 12
Runtime Error at line 10, column 34:
    print "Each person gets:", items / people
                                     ^
Cannot divide by zero.
```

**Say: What is error_demo.cute?**
> "error_demo.cute shows what happens when an error occurs inside a program file instead of in interactive mode."

**Say: How does it work?**
> "It sets `items = 12` and prints it. That works. Then it sets `people = 0` and tries `items / people`, which divides by zero. Calcute stops at that line and reports line 10, column 34, the exact position of the `/`. The line after it never runs."

**Say: Why this approach?**
> "In a long program, the error has to point at the exact line, or you'd have to search the whole file. It also shows that the earlier lines run correctly, and Calcute stops safely when it reaches the mistake, without a messy crash. That's the reliability criterion."

### 4B. Syntax is checked before anything runs

**Do:** create a file `test.cute` containing:
```
print "Hello"
print 2 +
```
then run:
```
python main.py test.cute
```
**You'll see:** only the Syntax Error for line 2. `Hello` is **not** printed.

**Say:**
> "Calcute checks the whole program before running any of it, so a mistake on the last line is caught before the first line runs. Half-finished programs never run."

### 4C. Automatic tests

**Do:**
```
python -m unittest discover tests -v
```
**You'll see:** 5 tests, each marked `ok`, ending with `OK`.

**Say: What is it?**
> "test_calcute.py checks Calcute automatically: about 20 correct answers, 11 syntax errors and 7 runtime errors."

**Say: Why this approach?**
> "Testing by hand is slow and easy to get wrong. With automatic tests, one command proves the output is correct. If we change the code later, we run the tests again to make sure nothing broke."

---

## PART 5 — How Calcute Works (and Why No If/Else)
**Presenter: Polendey, Stephen Jay**

### 5A. The 3 steps

**Say:**
> "Calcute reads code in 3 steps, like an assembly line."

```
your code  →  1. LEXER  →  2. PARSER  →  3. INTERPRETER  →  answer
              lexer.py    syntax_parser.py  interpreter.py
```

> "**Step 1, the lexer**, cuts the code into pieces called tokens. `7 + 6 * 10` becomes `7`, `+`, `6`, `*`, `10`. It's like reading the words of a sentence."

> "**Step 2, the parser**, checks the grammar, like checking that a sentence is correct, and builds a tree:"

```
        +
       / \
      7   *
         / \
        6   10
```

> "Multiplication sits lower in the tree, so it's done first."

> "**Step 3, the interpreter**, calculates from the bottom up: 6 × 10 = 60, then 7 + 60 = 67."

### 5B. Why no if/else

**Do:** open `interpreter.py` and show the `OPERATIONS` table.

**Say:**
> "The simple way to build a calculator is a long if/else chain: if the input is plus, add; else if it's minus, subtract; and so on. We don't do that. We use a dictionary called `OPERATIONS` that maps each symbol to its function."

```python
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": divide,
    "%": operator.mod,
    "^": power,
}

result = OPERATIONS[op](a, b)    # look up the operator, then use it
```

> "It's shorter and cleaner, and every operator works the same way. Adding a new operator only takes one new line. We used the same idea for the interactive commands (`COMMANDS`) and the error messages (`ERROR_MESSAGES`)."

### 5C. PL evaluation criteria (closing)

**Say:**
> "To finish, here's how Calcute meets the PL evaluation criteria.
> **Readability:** it looks like normal math.
> **Writability:** programs are short, with no declarations or data types.
> **Reliability:** every mistake is caught with its exact location, and automatic tests prove the answers are correct.
> **Cost:** anyone who knows basic math can learn it in minutes, and it only needs Python.
> Thank you!"

---

## Quick Q&A cheat sheet

| If asked... | Answer |
|---|---|
| What is a token? | The smallest piece of code, like a number, a name or an operator. |
| Why is `*` done before `+`? | The parser's grammar rules put `*` lower in the tree, so it's calculated first. |
| Why a dictionary instead of if/else? | It's shorter, cleaner, the same for every operator, and adding an operator takes one line. |
| What libraries did you use? | Only Python's built-in `re` (regular expressions, in the lexer) and `operator` (the math functions). Nothing to install. |
| Difference between Syntax and Runtime Error? | Syntax = wrong format (found before running). Runtime = right format, but it can't be calculated (found while running). |
| Is `22` alone an error? | No. A single number is a complete expression. |
