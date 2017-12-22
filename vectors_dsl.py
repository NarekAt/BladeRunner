
from lark import Lark, inline_args, InlineTransformer

vectors_grammar = """
    start: instructions

    instructions: (instruction)*

    instruction: "let" variable "=" VECTOR  -> declare_
               | "let" variable "=" instruction -> declare_
               | "ADD" variable "," variable "->" variable  -> add_
               | "div" VECTOR "/" VECTOR    -> div_
               | "mult" VECTOR "*" VECTOR   -> mult_
               | "smult" VECTOR "*" NUMBER  -> smult_
               | "repeat" NUMBER code_block -> repeat_
               | "print" variable           -> print_


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

class VectorGrammarTree(InlineTransformer):
    _lineNumber = 1

    def __init__(self):
        self.vars = {}

    def declare_(self, variable, value):
        self.vars[variable] = value
        self._lineNumber += 1
        return value

    def print_(self, variable):
      if variable in self.vars:
        print(self.vars[variable])
      else:
        print('ERROR at line %d : Undeclared variable passed as print argument' % self._lineNumber)
      self._lineNumber += 1

    def add_(self, var1, var2, sum):
        var1Numbers = self.var(var1)
        var1Numbers = var1Numbers.replace('}', '')
        var1Numbers = var1Numbers.replace('{', '')
        var1Numbers = var1Numbers.split(',')

        result = []
        for number in var1Numbers:
          result.append (int(number))

          result2 = [1, 3]
          sumValue = [a + b for (a, b) in zip(result, result2)]

        self.declare_(sum, sumValue)

    def var(self, name):
        return self.vars[name]


text = """
let vec = {12,2}
print vec
"""

#parser = Lark(vectors_grammar, start="instructions", parser="earley", lexer='standard')
parser = Lark(vectors_grammar, parser="lalr", transformer=VectorGrammarTree())
def test():
    print(parser.parse(text).pretty())

test()