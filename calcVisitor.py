from calculadoraVisitor import calculadoraVisitor

class calcVisitor(calculadoraVisitor):
    def visitNumber(self, ctx):
        return int(ctx.NUMBER().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

    def visitMul(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left * right

    def visitDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left / right  # División real

    def visitAdd(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left + right

    def visitSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        return left - right
