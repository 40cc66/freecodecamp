# [24 game](https://www.freecodecamp.org/learn/rosetta-code/rosetta-code-challenges/24-game)

The 24 Game tests a person's mental arithmetic.

The aim of the game is to arrange four numbers in a way that when evaluated, the result is 24

---

Implement a function that takes a string of four digits as its argument, with each digit from 1 to 9 (inclusive) with
repetitions allowed, and returns an arithmetic expression that evaluates to the number 24. If no such solution exists,
return "no solution exists".

**Rules:**

* Only the following operators/functions are allowed: multiplication, division, addition, subtraction.
* Division should use floating point or rational arithmetic, etc, to preserve remainders.
* Forming multiple digit numbers from the supplied digits is disallowed. (So an answer of 12+12 when given 1, 2, 2, and
  1 is wrong).
* The order of the digits when given does not have to be preserved.

| Example input      | Example output |
|--------------------|----------------|
| `solve24("4878");` | `(7-8/8)*4`    |
| `solve24("1234");` | `3*1*4*2`      |
| `solve24("6789");` | `(6*8)/(9-7)`  |
| `solve24("1127");` | `(1+7)*(2+1)`  |