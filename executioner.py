from pathlib import Path
from .tokenizer import tokenize
from .parser import Parser
from .interpreter import Interpreter

def execute(file_name: str | Path):

    with open(file_name, "r") as text_file:
        tokens = tokenize(text_file)
        ast = Parser(tokens).parse()
        Interpreter(ast).run()