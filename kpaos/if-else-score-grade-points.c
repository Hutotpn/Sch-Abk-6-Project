#include <stdio.h>

int main()
{
    // Variable
    int pts;
    
    // Input
    printf("Enter your score: ");
    scanf("%d", &pts);
    
    // If-else
    if (pts >= 80) {
        printf("Grade 4");
    } else if (pts >= 75) {
        printf("Grade 3.5");
    } else if (pts >= 70) {
        printf("Grade 3");
    } else if (pts >= 65) {
        printf("Grade 2.5");
    } else if (pts >= 60) {
        printf("Grade 2");
    } else if (pts >= 55) {
        printf("Grade 1.5");
    } else if (pts >= 50) {
        printf("Grade 1");
    } else {
        printf("Grade 0");
    }
    
    return 0;
}