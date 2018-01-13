
from lark import Lark, inline_args, InlineTransformer
from vectors_helper import *
import sys

vectors_grammar = """
    start: instructions

    instructions: (instruction)*

    instruction: "let" variable "=" VECTOR      -> declare_
               | "let" variable "=" instruction -> declare_
               | "add" variable "," variable    -> add_
               | "mult" variable "," variable   -> mult_
               | "smult" variable "," NUMBER    -> smult_
               | "repeat" NUMBER code_block     -> repeat_
               | "print" variable               -> print_


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

    def add_(self, var1, var2):
        vector1 = self.var(var1)
        vector2 = self.var(var2)
        return BladeAdd(vector1, vector2)

    def mult_(self, var1, var2):
        vector1 = self.var(var1)
        vector2 = self.var(var2)
        return BladeMult(vector1, vector2)

    def smult_(self, var, number):
        vector = self.var(var)
        return BladeSMult(vector, int(number))

    def repeat_(self, number, code_block):
      # TODO: Not implemented
      return

    def var(self, name):      
        if name not in self.vars:
            form = 'ERROR at line %d: Undeclared variable.' % (self._lineNumber)
            raise InputError(None, form)

        return self.vars[name]

#parser = Lark(vectors_grammar, start="instructions", parser="earley", lexer='standard')
parser = Lark(vectors_grammar, parser="lalr", transformer=VectorGrammarTree())

def eval(programm):
    try:
        print(parser.parse(programm).pretty())
    except InputError as e:
        print e.message
        if (e.expression != None):
            print e.expression
    sys.exit()