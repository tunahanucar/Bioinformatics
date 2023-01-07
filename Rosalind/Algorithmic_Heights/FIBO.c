#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
    int n;
    scanf("%d",&n);
    double a = (1 + sqrt(5)) / 2;
    double b = (1 - sqrt(5)) / 2;
    double result = (pow(a,n) - pow(b,n)) / sqrt(5);
    printf("%d",(int)result);
    return 0;
}
