from dataclasses import dataclass
from .tokenizer import TokenType

@dataclass(frozen=True)
class Node: 
    line_num: int
    col_start: int
    col_end: int

@dataclass(frozen=True)
class Statement(Node):
    line_id: int

@dataclass(frozen=True)
class NumericExpression(Node):
    pass 

@dataclass(frozen=True)
class UnaryOperation(NumericExpression):
    operator: TokenType
    expr: NumericExpression

    def __repr__(self) -> str:
        return f"{self.operator}{self.expr}"
    
@dataclass(frozen=True)
class BinaryOperation(NumericExpression):
    operator: TokenType
    left_expr: NumericExpression
    right_expr: NumericExpression
    def __repr__(self) -> str:
        return f"{self.left_expr} {self.operator} {self.right_expr}"
    
@dataclass(frozen=True)
class NumberLiteral(NumericExpression):
    number: int

@dataclass(frozen=True)
class VarRetrieve(NumericExpression):
    name: str

@dataclass(frozen=True)
class BooleanExpression(Node):
    operator: TokenType
    left_expr: NumericExpression
    right_expr: NumericExpression

    def __repr__(self) -> str:
        return f"{self.left_expr} {self.operator} {self.right_expr}"
    

@dataclass(frozen=True)
class LetStatement(Statement):
    name: str
    expr: NumericExpression

@dataclass(frozen=True)
class GoToStatement(Statement):
    line_expr: NumericExpression

@dataclass(frozen=True)
class GoSubStatement(Statement):
    line_expr: NumericExpression

@dataclass(frozen=True)
class ReturnStatement(Statement):
    pass

@dataclass(frozen=True)
class PrintStatement(Statement):
    printables: list[str | NumericExpression]


@dataclass(frozen=True)
class IfStatement(Statement):
    boolean_expr: BooleanExpression
    then_statement: Statement
