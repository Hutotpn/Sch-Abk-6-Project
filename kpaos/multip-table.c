#include <stdio.h>

int main()
{
    // Variable
    int a,b;
    
    // Input
    printf("Input number: ");
    scanf("%d", &a);
    
    // For loop
    for(b=1; b <= 12; b++) {
        printf("%d x %d = %d\n", a, b, a*b);
    }
    
    return 0;
}