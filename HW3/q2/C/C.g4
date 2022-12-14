grammar C;

begin
    : THREE_B
    ;

THREE_B
    : (THREE_CONSECUTIVE_OR_MORE_B)+
    ;

THREE_CONSECUTIVE_OR_MORE_B
    : [abc]*? 'bbb' [abc]*
    ; 