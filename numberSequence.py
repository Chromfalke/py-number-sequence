import argparse
import sys


ROOT = "1"


def count_numbers(row: str) -> str:
    next_row = ""

    numbers = row.split(" ")

    last_number = ""
    number_count = 0
    for number in numbers:
        if number == last_number:
            number_count += 1
            continue

        if number_count > 0:
            if next_row != "":
                next_row += f" {number_count} {last_number}"
            else:
                next_row = f"{number_count} {last_number}"

        last_number = number
        number_count = 1

    if next_row != "":
        next_row += f" {number_count} {last_number}"
    else:
        next_row = f"{number_count} {last_number}"
    
    return next_row


def generate_sequence(row_index: int) -> str:
    if row_index == 0:
        return ROOT
    
    return count_numbers(generate_sequence(row_index-1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="numberSequence"
    )

    parser.add_argument(
        "-r", "--root",
        type=str,
        help="Specify a custom root row for the generated sequence. Defaults to '1'"
    )

    parser.add_argument(
        "row_index",
        type=int,
        help="Index of the row that you want to print."
    )

    args = parser.parse_args()

    if args.root:
        try:
            for element in args.root.split(" "):
                int(element)
        except ValueError:
            print("Invalid custom root specified. Not all elements are numbers.")
            sys.exit(1)
        
        ROOT = args.root

    print(generate_sequence(args.row_index))