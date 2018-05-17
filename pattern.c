#include<stdio.h>
#include<stdlib.h>

void row_numbers(int row)
{
	int i,j;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<2*i+1;j++)
			printf("%d",i+1);
		printf("\n");
	}
}
void row_numbers_backwards(int row)
{
	int i,j;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<2*i+1;j++)
			printf("%d",row-i);
		printf("\n");
	}
}
void up_down_numbers(int row)
{
	int i,j;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<i+1;j++)
			printf("%d",j+1);
		for(j=0;j<i;j++)
			printf("%d",i-j);
		printf("\n");
	}
}
void up_numbers_down_alphabets(int row)
{
	int i,j;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<i+1;j++)
			printf("%d",j+1);
		for(j=0;j<i;j++)
			printf("%c",64+i-j);
		printf("\n");
	}
}
void alpha_numeric_alternate(int row)
{
	int i,j;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<i+1;j++)
		{
			if(j%2==0)
				printf("%c",65+j); //ASCII of A = 65
			else
				printf("%d",j+1);
		}
		for(j=i+1;j<2*i+1;j++)
		{
			if(j%2==0)
				printf("%c",65+2*i-j);
			else
				printf("%d",2*i+1-j);
		}
		printf("\n");
	}
}
void consecutive_series(int row)
{
	int i,j,k=1;
	for(i=0;i<row;i++)
	{
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<2*i+1;j++,k++)
		{
			if(k>9)
				k=0;
			printf("%d",k);
		}
		printf("\n");
	}
}
void row_number_up_down(int row)
{
	int i,j,k;
	for(i=0;i<row;i++)
	{
		k=i+1;
		for(j=0;j<row-1-i;j++)
			printf(" ");
		for(j=0;j<i+1;j++)
		{
			if(k>9)
				k=1;
			printf("%d",k);
			k++;
		}
		k-=2;
		for(j=0;j<i;j++)
		{
			if(k==0)
				k=9;
			printf("%d",k);
			k--;
		}
		printf("\n");
	}
}
void diamond_alpha_numeric(int row)
{
	int i,j;
	for(i=0;i<2*row-1;i++)
	{
		if(i<row)
		{
			for(j=0;j<row-1-i;j++)
				printf(" ");
			for(j=0;j<2*i+1;j++)
				printf("%d",i+1);
		}
		else
		{
			for(j=0;j<i+1-row;j++)
				printf(" ");
			for(j=0;j<2*(2*row-1-i)-1;j++)
				printf("%c",64+2*row-1-i);
		}
		printf("\n");
	}
}
void diamond_alpha_star(int row)
{
	int i,j;
	for(i=0;i<2*row-1;i++)
	{
		if(i<row)
		{
			for(j=0;j<row-1-i;j++)
				printf(" ");
			for(j=0;j<i+1;j++)
				printf("%d",j+1);
			for(j=0;j<i;j++)
				printf("*");
		}
		else
		{
			for(j=0;j<i+1-row;j++)
				printf(" ");
			for(j=0;j<2*row-i-2;j++)
				printf("*");
			for(j=0;j<2*row-1-i;j++)
				printf("%d",2*row-1-i-j);
		}
		printf("\n");
	}
}
void main()
{
	int option,row;
	while(1)
	{
		printf("-----------------\n");
		printf(" ** MAIN MENU **\n");
		printf("-----------------\n");
		printf("1. Row Numbers\n");
		printf("2. Row Numbers Backwards\n");
		printf("3. Up Down Numbers\n");
		printf("4. Up Numbers Down Alphabets\n");
		printf("5. Alpha Numeric Alternate\n");
		printf("6. Consecutive Series\n");
		printf("7. Row Number Up Down\n");
		printf("8. Diamond Alpha Numeric\n");
		printf("9. Diamond Alpha Star\n");
		printf("10.SET ROW_LEVEL\n");
		printf ("0. EXIT\n");
		printf("\nEnter your option (1 to 10) (0 to Exit): ");
		scanf("%d",&option);
	
		switch(option)
		{
			case 1:
			{
				printf("Row Numbers\n");
				row_numbers(row);
				break;
			}
			case 2:
			{
				printf("Row Numbers Backwards\n");
				row_numbers_backwards(row);
				break;
			}
			case 3:
			{
				printf("Up Down Numbers\n");
				up_down_numbers(row);
				break;
			}
			case 4:
			{
				printf("Up Numbers Down Alphabets\n");
				up_numbers_down_alphabets(row);
				break;
			}
			case 5:
			{
				printf("Alpha Numeric Alternate\n");
				alpha_numeric_alternate(row);
				break;
			}
			case 6:
			{
				printf("Consecutive Series\n");
				consecutive_series(row);
				break;
			}
			case 7:
			{
				printf("Row Number Up Down\n");
				row_number_up_down(row);
				break;
			}
			case 8:
			{
				printf("Diamond Alpha Numeric\n");
				diamond_alpha_numeric(row);
				break;
			}
			case 9:
			{
				printf("Diamond Alpha Star\n");
				diamond_alpha_star(row);
				break;
			}
			case 10:
			{
				printf("SET ROW_LEVEL\n");
				scanf("%d",&row);
				break;
			}
			case 0:
			{
				printf("EXIT\n");
				exit(EXIT_SUCCESS);
				break;
			}
			default:
				printf("Wrong Input\n");
		}
	}
}

