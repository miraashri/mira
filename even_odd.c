#include <stdio.h>

void main()
{
 int length,i;
 scanf("%d",&length);
 char str[length+1];
 scanf("%s",str);
 if(length&1)
 {
  length= length-1;
 }
 for(i=0;i<length;i+=2)
 {
     char c;
     c=str[i];
     str[i]=str[i+1];
     str[i+1]=c;
 }
  printf("%s\n",str);


}
