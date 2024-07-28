#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void *a, const void *b) {
    int *rowA = *(int **)a;
    int *rowB = *(int **)b;
    return (rowA[0] - rowB[0]);
}

int main() {
    // Initialize 2D array
    int arr[3][2] = {
        {3, 2},
        {2, 6},
        {1, 7}
    };

    // Convert 2D array to array of pointers
    int *arrPtrs[3];
    for (int i = 0; i < 3; i++) {
        arrPtrs[i] = arr[i];
    }

    // Sort using qsort
    qsort(arrPtrs, 3, sizeof(int *), compare);

    // Print sorted array
    for (int i = 0; i < 3; i++) {
        printf("%d %d\n", arrPtrs[i][0], arrPtrs[i][1]);
    }

    return 0;
}