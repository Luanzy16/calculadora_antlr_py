grammar calculadora;

SIN     : 'sin' ;
COS     : 'cos' ;
TAN     : 'tan' ;
SQRT    : 'sqrt' ; 
LOG3    : 'log3' ;
NUMBER  : '-'?[0-9]+('.'[0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
LPAREN  : '(' ;
RPAREN  : ')' ;


expr    : expr MUL expr        # Mul
        | expr DIV expr        # Div
        | expr PLUS expr       # Add
        | expr MINUS expr      # Sub
        | SIN LPAREN expr RPAREN # SinFunc
        | COS LPAREN expr RPAREN # CosFunc
        | TAN LPAREN expr RPAREN # TanFunc
        | SQRT LPAREN expr RPAREN # SqrtFunc
        | LOG3 LPAREN expr RPAREN # log3Func
        | NUMBER               # Number
        | LPAREN expr RPAREN   # Parens
        ;
