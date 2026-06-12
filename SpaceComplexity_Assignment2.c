#include <stdio.h>
#include <stdlib.h>

void constantSpace(int n)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
        sum += i;

    printf("Sum (O(1) space): %d\n", sum);
}

void linearSpace(int n)
{
    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        arr[i] = i + 1;

    printf("Linear space array elements:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\n");
    free(arr);
}

int recursiveSum(int n)
{
    if (n == 0)
        return 0;

    return n + recursiveSum(n - 1);
}

int main()
{
    int n;
    printf("Enter value of n: ");
    scanf("%d", &n);

    constantSpace(n);
    linearSpace(n);

    int result = recursiveSum(n);
    printf("Recursive sum (O(n) space): %d\n", result);

    return 0;
}
