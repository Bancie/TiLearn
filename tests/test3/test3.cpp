#include <iostream>
#include <cstdlib>
using namespace std;

// Comparison function for qsort
int compare(const void *a, const void *b) {
    int *rowA = *(int **)a;
    int *rowB = *(int **)b;
    return (rowA[1] - rowB[1]);
}

int main() {
    // Initialize 2D array
    int arr[3][2] = {
        {3, 7},
        {2, 6},
        {4, 2}
    };

    int *arrPtrs[3];
    for (int i = 0; i < 3; i++) {
        arrPtrs[i] = arr[i];
    }

    qsort(arrPtrs, 3, sizeof(double *), compare);

    for (int i = 0; i < 3; i++) {
        // printf("%d %d\n", arrPtrs[i][0], arrPtrs[i][1]);
        for (int j=0; j<2; j++)
            cout<<arrPtrs[i][j]<<" ";
        cout<<endl;
    }

    return 0;
}