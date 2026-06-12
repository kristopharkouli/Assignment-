#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void constantTime() {
    clock_t start, end;
    double time_taken;
    size_t memory_used = sizeof(int);

    int a = 10, b = 20, c;

    start = clock();
    c = a + b;
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Constant Time (O(1)):\n");
    printf("Execution Time = %f seconds\n", time_taken);
    printf("Space Used     = %zu bytes\n\n", memory_used);
}

void linearSearch(int *arr, int n) {
    clock_t start, end;
    double time_taken;
    size_t memory_used = n * sizeof(int);
    int key = -1;

    start = clock();
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            break;
    }
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Linear Search (O(n)):\n");
    printf("Execution Time = %f seconds\n", time_taken);
    printf("Space Used     = %zu bytes\n\n", memory_used);
}

void bubbleSort(int *arr, int n) {
    clock_t start, end;
    double time_taken;
    size_t memory_used = n * sizeof(int);

    start = clock();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    end = clock();

    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;

    printf("Bubble Sort (O(n^2)):\n");
    printf("Execution Time = %f seconds\n", time_taken);
    printf("Space Used     = %zu bytes\n\n", memory_used);
}

int main() {
    int n;

    printf("Enter number of elements (n): ");
    scanf("%d", &n);

    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
        arr[i] = i + 1;

    printf("\n--- Time and Space Complexity Analysis ---\n\n");

    constantTime();
    linearSearch(arr, n);
    bubbleSort(arr, n);

    free(arr);
    return 0;
}
