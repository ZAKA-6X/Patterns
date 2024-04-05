# Patterns

This Python code generates various staircase and diamond patterns using asterisks (`*`). Let's break down each part:

1. **Increasing Staircase**:
   - Starts with one asterisk and increases by one in each step up to `n`.

2. **Decreasing Staircase**:
   - Starts with `n` asterisks and decreases by one in each step down to one.

3. **Right-aligned Staircase**:
   - Similar to the decreasing staircase, but each line is right-aligned within the width of `n`.

4. **Left-aligned Staircase**:
   - Similar to the increasing staircase, but each line is left-aligned within the width of `n`.

5. **Diamond**:
   - The top part of a diamond. Starts with one asterisk and increases by two asterisks in each step.

6. **Reversed Diamond**:
   - The bottom part of a diamond. Starts with one asterisk and decreases by two asterisks in each step.

Each pattern is created using nested loops and string manipulations to adjust the spacing and the number of asterisks on each line. At the end of each pattern, there's a newline character (`'\n'`) to separate them visually.
