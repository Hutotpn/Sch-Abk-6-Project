#include <stdio.h>

int main()
{
    // Variable
    int height;
    
    // Input
    printf("Enter your height in centimeter: ");
    scanf("%d", &height);
    
    // If-else
    if (height <= 130) {
        printf("Price: ฿50");
    } else {
        printf("Price: ฿100");
    }

    return 0;
}