#include <stdio.h>

int main()
{
    float n1,n2,r;
    char op;
    int flag=0;
    printf("Welcome to Calculator\n");
    printf("Enter the first number\n");
    scanf("%f",&n1);
    printf("Enter the second number\n");
    scanf("%f",&n2);
    printf("Enter the operation to be performed\n");
    printf("The list of operations available are +,-,*,/\n");
    scanf(" %c",&op);
    switch(op)
    {
        case '+':
            r = n1+n2;
            break;
        case'-':
            r = n1-n2;
            break;
        case '*':
            r = n1*n2;
            break;
        case '/':
            r = n1/n2;
            if(n2==0){
                flag = 1;
            }
            break;
        default:
            printf("Invalid input\n");
    }
    if(flag){
        printf("Invalid input or operation\n");
    }
    printf("The answer is %.3f",r);
}
