# Generated from calculadora.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,53,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,3,0,34,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,0,1,0,1,0,0,0,61,0,33,1,
        0,0,0,2,3,6,0,-1,0,3,4,5,1,0,0,4,5,5,12,0,0,5,6,3,0,0,0,6,7,5,13,
        0,0,7,34,1,0,0,0,8,9,5,2,0,0,9,10,5,12,0,0,10,11,3,0,0,0,11,12,5,
        13,0,0,12,34,1,0,0,0,13,14,5,3,0,0,14,15,5,12,0,0,15,16,3,0,0,0,
        16,17,5,13,0,0,17,34,1,0,0,0,18,19,5,4,0,0,19,20,5,12,0,0,20,21,
        3,0,0,0,21,22,5,13,0,0,22,34,1,0,0,0,23,24,5,5,0,0,24,25,5,12,0,
        0,25,26,3,0,0,0,26,27,5,13,0,0,27,34,1,0,0,0,28,34,5,6,0,0,29,30,
        5,12,0,0,30,31,3,0,0,0,31,32,5,13,0,0,32,34,1,0,0,0,33,2,1,0,0,0,
        33,8,1,0,0,0,33,13,1,0,0,0,33,18,1,0,0,0,33,23,1,0,0,0,33,28,1,0,
        0,0,33,29,1,0,0,0,34,49,1,0,0,0,35,36,10,11,0,0,36,37,5,10,0,0,37,
        48,3,0,0,12,38,39,10,10,0,0,39,40,5,11,0,0,40,48,3,0,0,11,41,42,
        10,9,0,0,42,43,5,8,0,0,43,48,3,0,0,10,44,45,10,8,0,0,45,46,5,9,0,
        0,46,48,3,0,0,9,47,35,1,0,0,0,47,38,1,0,0,0,47,41,1,0,0,0,47,44,
        1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,1,1,0,0,0,51,
        49,1,0,0,0,3,33,47,49
    ]

class calculadoraParser ( Parser ):

    grammarFileName = "calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sin'", "'cos'", "'tan'", "'sqrt'", "'log3'", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SIN", "COS", "TAN", "SQRT", "LOG3", 
                      "NUMBER", "WS", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", 
                      "RPAREN" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    SIN=1
    COS=2
    TAN=3
    SQRT=4
    LOG3=5
    NUMBER=6
    WS=7
    PLUS=8
    MINUS=9
    MUL=10
    DIV=11
    LPAREN=12
    RPAREN=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calculadoraParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def DIV(self):
            return self.getToken(calculadoraParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(calculadoraParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(calculadoraParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class TanFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TAN(self):
            return self.getToken(calculadoraParser.TAN, 0)
        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTanFunc" ):
                listener.enterTanFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTanFunc" ):
                listener.exitTanFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTanFunc" ):
                return visitor.visitTanFunc(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(calculadoraParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class Log3FuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOG3(self):
            return self.getToken(calculadoraParser.LOG3, 0)
        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog3Func" ):
                listener.enterLog3Func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog3Func" ):
                listener.exitLog3Func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog3Func" ):
                return visitor.visitLog3Func(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calculadoraParser.ExprContext)
            else:
                return self.getTypedRuleContext(calculadoraParser.ExprContext,i)

        def MUL(self):
            return self.getToken(calculadoraParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class CosFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COS(self):
            return self.getToken(calculadoraParser.COS, 0)
        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCosFunc" ):
                listener.enterCosFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCosFunc" ):
                listener.exitCosFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCosFunc" ):
                return visitor.visitCosFunc(self)
            else:
                return visitor.visitChildren(self)


    class SqrtFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SQRT(self):
            return self.getToken(calculadoraParser.SQRT, 0)
        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqrtFunc" ):
                listener.enterSqrtFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqrtFunc" ):
                listener.exitSqrtFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqrtFunc" ):
                return visitor.visitSqrtFunc(self)
            else:
                return visitor.visitChildren(self)


    class SinFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calculadoraParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIN(self):
            return self.getToken(calculadoraParser.SIN, 0)
        def LPAREN(self):
            return self.getToken(calculadoraParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(calculadoraParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(calculadoraParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinFunc" ):
                listener.enterSinFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinFunc" ):
                listener.exitSinFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinFunc" ):
                return visitor.visitSinFunc(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calculadoraParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = calculadoraParser.SinFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                self.match(calculadoraParser.SIN)
                self.state = 4
                self.match(calculadoraParser.LPAREN)
                self.state = 5
                self.expr(0)
                self.state = 6
                self.match(calculadoraParser.RPAREN)
                pass
            elif token in [2]:
                localctx = calculadoraParser.CosFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(calculadoraParser.COS)
                self.state = 9
                self.match(calculadoraParser.LPAREN)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(calculadoraParser.RPAREN)
                pass
            elif token in [3]:
                localctx = calculadoraParser.TanFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(calculadoraParser.TAN)
                self.state = 14
                self.match(calculadoraParser.LPAREN)
                self.state = 15
                self.expr(0)
                self.state = 16
                self.match(calculadoraParser.RPAREN)
                pass
            elif token in [4]:
                localctx = calculadoraParser.SqrtFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                self.match(calculadoraParser.SQRT)
                self.state = 19
                self.match(calculadoraParser.LPAREN)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(calculadoraParser.RPAREN)
                pass
            elif token in [5]:
                localctx = calculadoraParser.Log3FuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 23
                self.match(calculadoraParser.LOG3)
                self.state = 24
                self.match(calculadoraParser.LPAREN)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(calculadoraParser.RPAREN)
                pass
            elif token in [6]:
                localctx = calculadoraParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(calculadoraParser.NUMBER)
                pass
            elif token in [12]:
                localctx = calculadoraParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(calculadoraParser.LPAREN)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(calculadoraParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = calculadoraParser.MulContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 36
                        self.match(calculadoraParser.MUL)
                        self.state = 37
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = calculadoraParser.DivContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 39
                        self.match(calculadoraParser.DIV)
                        self.state = 40
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = calculadoraParser.AddContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 42
                        self.match(calculadoraParser.PLUS)
                        self.state = 43
                        self.expr(10)
                        pass

                    elif la_ == 4:
                        localctx = calculadoraParser.SubContext(self, calculadoraParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 45
                        self.match(calculadoraParser.MINUS)
                        self.state = 46
                        self.expr(9)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




