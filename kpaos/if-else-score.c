#include <stdio.h>

int main()
{
    // Variable
    int pts;
    
    // Input
    printf("Enter your score: ");
    scanf("%d", &pts);
    
    // If-else
    if (pts >= 60) {
        printf("You pass!");
    } else {
        printf("You fail, your Asian dad will say:\nWHAT DA HAIL YOU SAY you don't know F stands for FAILURE.");
    }

    return 0;
}
