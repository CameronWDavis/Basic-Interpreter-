from argparse import ArgumentParser
from .executioner import execute

if __name__ == "__main__":
    file_parser = ArgumentParser("BASIC")
    file_parser.add_argument("basic_file",
                             help="A text file containing BASIC code.")
    arguments = file_parser.parse_args()
    execute(arguments.basic_file)
