#include<stdio.h>

int main()
{
    int max = 100;
    char ch, s[max], sen[max];

    //Blank space after "%c" in scanf format string ignores last character
    scanf("%c ",&ch);
    scanf("%s ",s);
    fgets(sen, max, stdin);

    printf("%c\n",ch);
    printf("%s\n",s);
    printf("%s\n",sen);

    return 0;
}
