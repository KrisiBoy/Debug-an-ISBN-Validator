import argparse

# Simple ISBN validator supporting ISBN-10 and ISBN-13.
# Supports command-line arguments and interactive prompt input.


def validate_isbn(isbn, length):
    # Check that the entered ISBN has the correct length.
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    try:
        # Split the code into the main digits and the check digit.
        main_digits = isbn[0:length-1]
        given_check_digit = isbn[length-1]
    except IndexError:
        print('Invalid ISBN code.')
        return
    
    try:
        # Convert the main digits to integers for checksum calculation.
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return
    
    # Compute the expected check digit based on ISBN length.
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare the provided check digit with the expected one.
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')
        

def calculate_check_digit_10(main_digits_list):
    # ISBN-10 checksum: weighted sum from 10 to 2.
    digits_sum = 0
    
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    # Map special cases: 10 -> 'X', 11 -> '0'.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    # ISBN-13 checksum: alternating weights of 1 and 3.
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    # If the result is 10, the check digit should be 0.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit


def main():
    # Prompt the user for an ISBN code and the expected length.
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    try:
        isbn = values[0]
        length_str = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return
    
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


def parse_args():
    parser = argparse.ArgumentParser(
        description='Validate ISBN-10 or ISBN-13 codes.'
    )
    parser.add_argument(
        'isbn',
        nargs='?',
        help='The ISBN code to validate. For ISBN-10, the last digit may be X.'
    )
    parser.add_argument(
        'length',
        nargs='?',
        type=int,
        choices=[10, 13],
        help='The ISBN length: 10 or 13.'
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.isbn and args.length:
        validate_isbn(args.isbn.strip(), args.length)
        return

    # Prompt the user for input when command-line arguments are not provided.
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')

    try:
        isbn = values[0].strip()
        length_str = values[1].strip()
    except IndexError:
        print('Enter comma-separated values.')
        return
    
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')


if __name__ == '__main__':
    main()