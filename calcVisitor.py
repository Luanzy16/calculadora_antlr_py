import math
from calculadoraVisitor import calculadoraVisitor

class calcVisitor(calculadoraVisitor):
    def visitNumber(self, ctx):
        return float(ctx.NUMBER().getText())  # Permitir números decimales

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right  

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right

    def visitSinFunc(self, ctx):
        value = self.visit(ctx.expr())
        return math.sin(value)

    def visitCosFunc(self, ctx):
        value = self.visit(ctx.expr())
        return math.cos(value)

    def visitTanFunc(self, ctx):
        value = self.visit(ctx.expr())
        return math.tan(value)

    def visitSqrtFunc(self, ctx):
        value = self.visit(ctx.expr())
        if value < 0:
            raise ValueError("Error: no se puede con numeros negativos.")
        return math.sqrt(value)

    def visitLog3Func(self, ctx):
        value = self.visit(ctx.expr())
        if value <= 0:
            raise ValueError("Error: solo acepta positivos.")
        return math.log(value, 3) 
