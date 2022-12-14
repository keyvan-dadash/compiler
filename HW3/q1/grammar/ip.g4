grammar ip;

begin
    : privateIP
    | IP
    ;

privateIP
    : V24
    | V20
    | V16
    ;

otherIP
    : IP
    ;
V24
    : '10''.' VALID_SECTION '.' VALID_SECTION '.' VALID_SECTION
    ;
V20
    : '172''.' V20VALID_SECTION '.' VALID_SECTION '.' VALID_SECTION
    ;
V16
    : '192.168''.' VALID_SECTION '.' VALID_SECTION
    ;

IP
    : VALID_SECTION '.' VALID_SECTION '.' VALID_SECTION '.' VALID_SECTION
    ;

V20VALID_SECTION
    : [1][6-9]
    | [2][0-9]
    | [3][0-1]
    ;

VALID_SECTION
    : [1]?[0-9]?[0-9]
    | [2][0-4][0-9]
    | [2][5][0-5]
    ;