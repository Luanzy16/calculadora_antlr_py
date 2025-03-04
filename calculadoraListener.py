# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete listener for a parse tree produced by calculadoraParser.
class calculadoraListener(ParseTreeListener):

    # Enter a parse tree produced by calculadoraParser#Div.
    def enterDiv(self, ctx:calculadoraParser.DivContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Div.
    def exitDiv(self, ctx:calculadoraParser.DivContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Add.
    def enterAdd(self, ctx:calculadoraParser.AddContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Add.
    def exitAdd(self, ctx:calculadoraParser.AddContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Sub.
    def enterSub(self, ctx:calculadoraParser.SubContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Sub.
    def exitSub(self, ctx:calculadoraParser.SubContext):
        pass


    # Enter a parse tree produced by calculadoraParser#TanFunc.
    def enterTanFunc(self, ctx:calculadoraParser.TanFuncContext):
        pass

    # Exit a parse tree produced by calculadoraParser#TanFunc.
    def exitTanFunc(self, ctx:calculadoraParser.TanFuncContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Number.
    def enterNumber(self, ctx:calculadoraParser.NumberContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Number.
    def exitNumber(self, ctx:calculadoraParser.NumberContext):
        pass


    # Enter a parse tree produced by calculadoraParser#log3Func.
    def enterLog3Func(self, ctx:calculadoraParser.Log3FuncContext):
        pass

    # Exit a parse tree produced by calculadoraParser#log3Func.
    def exitLog3Func(self, ctx:calculadoraParser.Log3FuncContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Mul.
    def enterMul(self, ctx:calculadoraParser.MulContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Mul.
    def exitMul(self, ctx:calculadoraParser.MulContext):
        pass


    # Enter a parse tree produced by calculadoraParser#Parens.
    def enterParens(self, ctx:calculadoraParser.ParensContext):
        pass

    # Exit a parse tree produced by calculadoraParser#Parens.
    def exitParens(self, ctx:calculadoraParser.ParensContext):
        pass


    # Enter a parse tree produced by calculadoraParser#CosFunc.
    def enterCosFunc(self, ctx:calculadoraParser.CosFuncContext):
        pass

    # Exit a parse tree produced by calculadoraParser#CosFunc.
    def exitCosFunc(self, ctx:calculadoraParser.CosFuncContext):
        pass


    # Enter a parse tree produced by calculadoraParser#SqrtFunc.
    def enterSqrtFunc(self, ctx:calculadoraParser.SqrtFuncContext):
        pass

    # Exit a parse tree produced by calculadoraParser#SqrtFunc.
    def exitSqrtFunc(self, ctx:calculadoraParser.SqrtFuncContext):
        pass


    # Enter a parse tree produced by calculadoraParser#SinFunc.
    def enterSinFunc(self, ctx:calculadoraParser.SinFuncContext):
        pass

    # Exit a parse tree produced by calculadoraParser#SinFunc.
    def exitSinFunc(self, ctx:calculadoraParser.SinFuncContext):
        pass



del calculadoraParser