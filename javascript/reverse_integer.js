var reverse = function(x) {
    /*
    The algorithm:
    - turn into a string
    - turn into an array
    - reverse an array
    - turn back into a string
    - turn back into a Number

    In case of negative number, get absolute value and add minus before conversion to Number.

    Faster syntax was used for if else statements: logicalExpression ? executeWhenTrue : executeWhenFalse
    */
    x = x > 0 ? Number(x.toString().split("").reverse().join("")) : Number('-' + Math.abs(x).toString().split("").reverse().join(""));
    return -(2 ** 31) < x && x < 2 ** 31 ? x : 0;
};