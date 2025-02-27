grammar calculadora;

// Reglas léxicas
NUMBER  : [0-9]+ ;
WS      : [ \t\r\n]+ -> skip ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
LPAREN  : '(' ;
RPAREN  : ')' ;

// Reglas sintácticas con etiquetas
expr    : expr MUL expr   # Mul
        | expr DIV expr   # Div
        | expr PLUS expr  # Add
        | expr MINUS expr # Sub
        | NUMBER          # Number
        | LPAREN expr RPAREN # Parens
        ;
