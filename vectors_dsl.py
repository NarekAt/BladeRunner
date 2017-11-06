
from lark import Lark

vectors_grammar = """
    start: instructions

    instructions: (instruction)*

    instruction: "let" variable "=" VECTOR  -> _declare
               | "add" VECTOR "+" VECTOR    -> _add
               | "div" VECTOR "/" VECTOR    -> _div
               | "mult" VECTOR "*" VECTOR   -> _mult
               | "smult" VECTOR "*" NUMBER  -> _smult
               | "repeat" NUMBER code_block -> _repeat
               | "print" variable           -> _print


    VECTOR: "{" NUMBER ("," NUMBER)* "}"

    code_block: "{" instruction+ "}"
    variable: LETTER+

    %import common.NEWLINE -> _NL
    %import common.WS_INLINE
    %ignore WS_INLINE
    %import common.LETTER
    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

text = """
let vec = {12,2}
let otherVec = {3,2}
print vec
"""

parser = Lark(vectors_grammar, start="instructions", parser="earley", lexer='standard')

print(parser.parse(text).pretty())

