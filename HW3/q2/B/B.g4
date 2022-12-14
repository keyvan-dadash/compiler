grammar B;

begin
    : THREE_A_ALL | EOF
    ;

THREE_A_ALL
    : (THREE_A)+
    ;

THREE_A
    : [bc]+? | (SINGLE_A SINGLE_A SINGLE_A)
    ;

SINGLE_A
    : [bc]* [a] [bc]*
    ;