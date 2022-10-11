#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double doubleCheck();

void Qmake(int matrCount)
{
  double ***A = (double ***)malloc(matrCount*sizeof(double **));
  int **matrSize = (int **)malloc(matrCount*sizeof(int *));
  
  int i,j,k,s;
  double tmp;
  int matrI;
  int matrJ;
  
  for(i = 0; i < matrCount; i++)
  {
       matrSize[i] = (int *)malloc(2*sizeof(int)); 
  }
  
  for( i = 0; i < matrCount; i++)
  {
     printf("������ ���-�� ��ப: ");
     matrI = intCheck();
     printf("������ ���-�� �⮫�殢: ");
     matrJ = intCheck();
     A[i] = (double **)malloc(matrI*sizeof(double *));  
     for(j=0;j<matrI;j++)
     {
        A[i][j] = (double *)malloc(matrJ*sizeof(double)); 
     }
     
     matrSize[i][0]= matrI;
     matrSize[i][1]= matrJ;
     
     printf("�a������ �a����\n");
     for(j=0;j<matrI;j++)
     {
        for(k=0;k<matrJ;k++)
         {
            A[i][j][k] = doubleCheck();
         } 
     } 
  }
  
  for(i=0;i<matrCount;i++)
  {
     for(j=0;j<matrSize[i][0];j++)
     {
        for(k=0;k<matrSize[i][1];k++)
         {
            printf("%lf ", A[i][j][k]);
         }
         printf("\n"); 
     }
     system("PAUSE");
     printf("\n");
     printf("\n");                      
  } 
  
  for(i=0;i<matrCount;i++)
  {
     for(j=0;j<matrSize[i][0];j++)
     {
        for(k=0;k<matrSize[i][1];k++)
         {
            for(s=0;s<matrSize[i][1]-k-1;s++)
            {
               if(A[i][j][s]<A[i][j][s+1]){
                  tmp = A[i][j][s];
                  A[i][j][s] = A[i][j][s+1];
                  A[i][j][s+1]=tmp;
               }                        
            }
         }
     }                     
  }
  
  printf("�८��a���a��� �a����:\n");
  for(i=0;i<matrCount;i++)
  {
     for(j=0;j<matrSize[i][0];j++)
     {
        for(k=0;k<matrSize[i][1];k++)
         {
            printf("%lf ", A[i][j][k]);
         }
         printf("\n"); 
     }
     system("PAUSE");
     printf("\n");
     printf("\n");                      
  }
  
  
  free(A); 
   
}

int intCheck()
{   
    int n;
	do
	{
		if(!scanf("%d", &n))
		   printf("�� ��a����� ��a� �a��� ��a, ������ ������:\n");
        else if(n<1||n>1000)
           printf("�� ��a����� ��a� �a��� ��a, ������ ������:\n");
	} while (getchar() != '\n');
    return n;
}

double doubleCheck()
{   
    double n;
	do
	{
		if(!scanf("%lf", &n))
		   printf("�� ��a����� ��a� �a��� ��a, ������ ������:\n");
		
	} while (getchar() != '\n');
    return n;
}

int main(int argc, char *argv[])
{

  int matrCount, matrI, matrJ;
  int run = 1;
  int event;
  int x;


  while(run)
  {
     printf("1 - ����� �a����\n2 - ��室\n");
     event = intCheck();
     if(event == 1)
     {
        printf("������ ���-�� �a���: ");
        matrCount = intCheck();       
  
        Qmake(matrCount);
     }
     
     if(event == 2)
        run = 0;
  }
  
  
  system("PAUSE");	
  return 0;
}

