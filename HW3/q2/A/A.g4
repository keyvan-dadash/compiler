grammar A;

begin
    : TWO | THREE | FOUR
    ;

TWO
    : [abc][abc]
    ;

THREE
    : [abc][abc][abc]
    ;

FOUR
    : [abc][abc][abc][abc]
    ;