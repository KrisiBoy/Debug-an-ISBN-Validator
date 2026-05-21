# ISBN Validator

A small Python script for validating ISBN-10 and ISBN-13 numbers.

> Lab project from freeCodeCamp.org

## Description

This script validates an ISBN by calculating the expected check digit and comparing it to the provided value.

- ISBN-10 uses a weighted sum from 10 down to 2.
- ISBN-13 uses alternating weights of 1 and 3.

## Requirements

- Python 3.x

## Usage

Run the script from the project folder.

### Show help

```bash
python main.py -h
```

### Command-line mode

```bash
python main.py 0306406152 10
```

### Interactive mode

If you run the script without arguments, it prompts for input:

```bash
python main.py
```

Then enter the ISBN and length separated by a comma:

```text
0306406152,10
```

## Examples

Valid ISBN-10 example (command-line):

```bash
python main.py 0306406152 10
```

Valid ISBN-10 example (interactive):

```text
Enter ISBN and length: 0306406152,10
Valid ISBN Code.
```

Invalid ISBN example:

```text
Enter ISBN and length: 0306406153,10
Invalid ISBN Code.
```

## Supported ISBN Formats

- `10` for ISBN-10
- `13` for ISBN-13

## Input Rules

- Use a comma-separated format: `ISBN,length`
- Leading and trailing spaces are ignored for both values.
- ISBN-10 check digits may be numeric or `X`.

## Notes

- The script is self-contained and has no external dependencies.
- It validates checksum correctness only; it does not verify publisher or registration details.
