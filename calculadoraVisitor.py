# Generated from calculadora.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .calculadoraParser import calculadoraParser
else:
    from calculadoraParser import calculadoraParser

# This class defines a complete generic visitor for a parse tree produced by calculadoraParser.

class calculadoraVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calculadoraParser#Div.
    def visitDiv(self, ctx:calculadoraParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Add.
    def visitAdd(self, ctx:calculadoraParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Sub.
    def visitSub(self, ctx:calculadoraParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#TanFunc.
    def visitTanFunc(self, ctx:calculadoraParser.TanFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Number.
    def visitNumber(self, ctx:calculadoraParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#log3Func.
    def visitLog3Func(self, ctx:calculadoraParser.Log3FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Mul.
    def visitMul(self, ctx:calculadoraParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#Parens.
    def visitParens(self, ctx:calculadoraParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#CosFunc.
    def visitCosFunc(self, ctx:calculadoraParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#SqrtFunc.
    def visitSqrtFunc(self, ctx:calculadoraParser.SqrtFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calculadoraParser#SinFunc.
    def visitSinFunc(self, ctx:calculadoraParser.SinFuncContext):
        return self.visitChildren(ctx)



del calculadoraParser