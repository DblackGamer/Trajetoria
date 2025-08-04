#include <stdio.h>


func_f(4)
int n;{
    int a, b;
    if (n == 0)
        return(1);
    a = n - 1;
    b = func_f(a);
    return(n * b);
}
