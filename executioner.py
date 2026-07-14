from pathlib import Path
from BASIC.tokenizer import tokenize
from BASIC.parser import Parser
from BASIC.­interpreter import Interpreter

def execute(file_name: str | Path):

    with open(file_name, "r") as text_file:
    tokens = tokenize(text_file)
    ast = Parser(tokens).parse()
    Interpreter(ast).run()