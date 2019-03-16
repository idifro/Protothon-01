#include <stdio.h>

void main()
{
    int no,c=1;
    int k,i,j;
    printf("Input number of rows: ");
    scanf("%d",&no);
    for(i=0;i<no;i++)
    {
        for(k=1;k<=no-i;k++)
        printf("  ");
        for(j=0;j<=i;j++)
        {
            if (j==0||i==0)
                c=1;
            else
               c=c*(i-j+1)/j;
            printf("% 4d",c);
        }
        printf("\n");
    }
}
