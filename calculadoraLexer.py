# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,84,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,5,3,5,51,8,5,1,5,4,5,54,8,5,11,5,12,5,55,1,
        5,1,5,4,5,60,8,5,11,5,12,5,61,3,5,64,8,5,1,6,4,6,67,8,6,11,6,12,
        6,68,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,
        12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,88,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,31,1,0,0,0,5,35,1,0,0,0,7,39,1,
        0,0,0,9,44,1,0,0,0,11,50,1,0,0,0,13,66,1,0,0,0,15,72,1,0,0,0,17,
        74,1,0,0,0,19,76,1,0,0,0,21,78,1,0,0,0,23,80,1,0,0,0,25,82,1,0,0,
        0,27,28,5,115,0,0,28,29,5,105,0,0,29,30,5,110,0,0,30,2,1,0,0,0,31,
        32,5,99,0,0,32,33,5,111,0,0,33,34,5,115,0,0,34,4,1,0,0,0,35,36,5,
        116,0,0,36,37,5,97,0,0,37,38,5,110,0,0,38,6,1,0,0,0,39,40,5,115,
        0,0,40,41,5,113,0,0,41,42,5,114,0,0,42,43,5,116,0,0,43,8,1,0,0,0,
        44,45,5,108,0,0,45,46,5,111,0,0,46,47,5,103,0,0,47,48,5,51,0,0,48,
        10,1,0,0,0,49,51,5,45,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,
        0,0,52,54,7,0,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,63,1,0,0,0,57,59,5,46,0,0,58,60,7,0,0,0,59,58,1,0,0,0,
        60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,57,1,
        0,0,0,63,64,1,0,0,0,64,12,1,0,0,0,65,67,7,1,0,0,66,65,1,0,0,0,67,
        68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,6,6,0,
        0,71,14,1,0,0,0,72,73,5,43,0,0,73,16,1,0,0,0,74,75,5,45,0,0,75,18,
        1,0,0,0,76,77,5,42,0,0,77,20,1,0,0,0,78,79,5,47,0,0,79,22,1,0,0,
        0,80,81,5,40,0,0,81,24,1,0,0,0,82,83,5,41,0,0,83,26,1,0,0,0,6,0,
        50,55,61,63,68,1,6,0,0
    ]

class calculadoraLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SIN = 1
    COS = 2
    TAN = 3
    SQRT = 4
    LOG3 = 5
    NUMBER = 6
    WS = 7
    PLUS = 8
    MINUS = 9
    MUL = 10
    DIV = 11
    LPAREN = 12
    RPAREN = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'sin'", "'cos'", "'tan'", "'sqrt'", "'log3'", "'+'", "'-'", 
            "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "SIN", "COS", "TAN", "SQRT", "LOG3", "NUMBER", "WS", "PLUS", 
            "MINUS", "MUL", "DIV", "LPAREN", "RPAREN" ]

    ruleNames = [ "SIN", "COS", "TAN", "SQRT", "LOG3", "NUMBER", "WS", "PLUS", 
                  "MINUS", "MUL", "DIV", "LPAREN", "RPAREN" ]

    grammarFileName = "calculadora.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


