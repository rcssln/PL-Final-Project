# Calcute — 4-Minute Presentation Script

**Time limit: 3–4 minutes of presentation + 1 minute Q&A.**
Every part is short on purpose. Speak at a normal pace and don't add extra demos.

| Time | Presenter | Parts | Covers requirement |
|---|---|---|---|
| 0:00 – 1:00 | **Presenter 1:** _name_ | 1. What Calcute can do<br>2. Programming language used | 6.a.i, 6.a.ii |
| 1:00 – 1:50 | **Presenter 2:** _name_ | 3. Strategies in building Calcute | 6.a.iii |
| 1:50 – 3:40 | **Presenter 3:** _name_ | 4. Live demo: math, variables, errors<br>5. Live demo: program file and closing | 6.b |
| 3:40 – 4:40 | All three | Q&A (1 minute) | — |

> Presenter 3 does the whole live demo, so Presenter 3's computer is the one that shares its screen.

---

## BEFORE JOINING THE MEETING (no time for debugging!)

Presenter 3 does all of this on the computer that will share its screen, **before** the meeting starts:

1. ☐ Open the project folder in VS Code.
2. ☐ Open a terminal (``Ctrl+` ``) and run the tests: `python -m unittest discover tests`. It must say `OK`.
3. ☐ Make the terminal text big: click inside it and press `Ctrl` + `=` a few times.
4. ☐ Run `python main.py` so the `cute>` prompt is **already showing** when you share the screen.
5. ☐ Keep `interpreter.py` open in an editor tab, scrolled to the `OPERATIONS` table (for Part 3).
6. ☐ Close other apps and notifications. Share only the VS Code window.
7. ☐ Rehearse once with a timer. If you go over 4 minutes, shorten the "Say" lines, not the demo.

---

## PART 1 — What Calcute Can Do (30 sec)
**Presenter 1**

**Say:**
> "Good day! We are [names]. Our programming language is called **Calcute**: calc plus cute. It's a small, simple language for arithmetic.
>
> Calcute can add, subtract, multiply, divide, find the remainder and calculate powers. It works with whole numbers, decimals and negative numbers, and it follows the correct order of operations. It also supports **variables**, a **print** statement for showing text and answers, and **comments**. Most importantly, it has **clear error handling**: when the input is in the wrong format, Calcute tells you what's wrong and points to the exact spot."

---

## PART 2 — Programming Language Used (30 sec)
**Presenter 1 (continues)**

**Say:**
> "We built Calcute using **Python**. We chose Python because it's easy to read, it handles very large whole numbers exactly, and it runs on any computer.
>
> We didn't use any outside libraries, so there's nothing to install. We only used two built-in Python modules: **`re`**, for regular expressions, to recognize numbers, names and symbols, and **`operator`**, which provides the math functions like add and multiply. We wrote the main parts of the language ourselves."

---

## PART 3 — Strategies in Building Calcute (50 sec)
**Presenter 2**

**Say:**
> "We used three main strategies.
>
> **First, we split the work into three steps, like an assembly line.** The **lexer** cuts the code into small pieces called tokens. The **parser** checks the grammar and builds a tree. The **interpreter** calculates the answer from that tree.
>
> **Second, the order of operations comes from the grammar.** The parser has one rule for each level: plus and minus, then times and divide, then power, then numbers and parentheses. So in `7 + 6 * 10`, the multiplication is placed deeper in the tree and is done first.
>

**Do:** switch to the `interpreter.py` tab and point at `OPERATIONS`.

> "Instead of writing 'if the input is plus, add; else if it's minus, subtract', we use a **dictionary** that maps each symbol to its function. It's shorter and cleaner, and adding a new operator takes only one line."

---

## PART 4 — Live Demo: Math, Variables, Errors (70 sec)
**Presenter 3**

**Do:** switch back to the terminal (the `cute>` prompt is already running). Type each line.

**Say:** "Let me show Calcute in action. First, basic math and the order of operations."
```
cute> 7 + 6 * 10
67
cute> (7 + 6) * 10
130
cute> 7 / 2
3.5
cute> 2 ^ 10
1024
```
> "Multiplication is done first, so 67. With parentheses, the addition goes first, so 130."

**Say:** "Next, variables."
```
cute> price = 50
cute> quantity = 4
cute> print "Total:", price * quantity
Total: 200
```

**Say:** "Now the error handling. Let's make some mistakes on purpose."
```
cute> 5 +
Syntax Error at line 1, column 4:
    5 +
       ^
Expected a number, a variable or '(' but found the end of the program.
cute> 10 / 0
Runtime Error at line 1, column 4:
    10 / 0
       ^
Cannot divide by zero.
cute> y + 1
Runtime Error at line 1, column 1:
    y + 1
    ^
Undefined variable 'y'. Give it a value first, e.g. y = 10
```
> "Calcute doesn't crash. It tells us the kind of error, the line and column, and points at the problem with a caret."

**Do:** type `exit`.

---

## PART 5 — Live Demo: Program File + Closing (40 sec)
**Presenter 3 (continues)**

**Do:**
```
python main.py examples/basics.cute
```
**Say:**
> "Calcute can also run a whole program saved in a file. This file tests every operator and every order-of-operations rule, and we made every answer 67 on purpose. If any rule were wrong, the answer wouldn't be 67, so this proves Calcute calculates correctly."

**Say (closing):**
> "To sum up: Calcute is **readable** because it looks like normal math, **writable** because programs are short, **reliable** because every mistake is caught with its exact location, and **low-cost** because anyone who knows basic math can use it, and it only needs Python. Thank you! We're happy to answer questions."

---

## Q&A CHEAT SHEET (1 minute, so keep answers short)

| If asked... | Answer |
|---|---|
| What is a token? | The smallest piece of code, like a number, a name or a symbol. |
| Why is `*` done before `+`? | The parser's grammar puts `*` deeper in the tree, so it's calculated first. |
| Why a dictionary instead of if/else? | Shorter, cleaner, the same for every operator, and adding an operator takes one line. |
| What libraries did you use? | Only Python's built-in `re` and `operator`. Nothing to install. |
| Syntax Error vs Runtime Error? | Syntax = wrong format, found before running. Runtime = right format, but it can't be calculated. |
| Is `22` alone an error? | No. A single number is a complete expression, like on a calculator. |
| Can you use any variable name? | Yes: letters, numbers and underscores, but not starting with a number. `Score` and `score` are different. |
| What if the code has a mistake on the last line? | Calcute checks the whole program before running, so nothing runs. |
| Does it handle huge numbers? | Yes, whole numbers are exact (`2 ^ 100` works). Results that are too large, like `9 ^ 9 ^ 9`, give an error instead of freezing. |
