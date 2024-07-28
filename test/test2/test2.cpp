#include <iostream>
#include <cstdlib>
using namespace std;

/*int compare ( const void *a, const void *b ) {
    const int (*x)[4] = a;
    const int (*y)[4] = b;
    if ( (*x)[3] < (*y)[3] ) return -1;
    if ( (*x)[3] > (*y)[3] ) return +1;
    return 0;
}*/

/*int compare ( const void *pa, const void *pb ) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;
    if(a[0] == b[0])
        return a[1] - b[1];
    else
        return a[0] - b[0];
}*/

/*int compare(const void* a, const void* b) {
	const int* x = (int*) a;
	const int* y = (int*) b;

	if (*x > *y)
		return 1;
	else if (*x < *y)
		return -1;
	return 0;
}*/


int compare(const void *a, const void *b) {
    int *rowA = *(int **)a;
    int *rowB = *(int **)b;
    return (rowA[0] - rowB[0]);
}

int main() {
	const int m = 3;
    const int n = 2;
    int *arrPtrs[3];
	int arr[m][n] = {{3,2},
                    {2,6},
                    {1,7}};

    
	for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++)
            cout << arr[i][j] << " ";
        cout<<endl;
    }

    for (int i = 0; i < 3; i++) {
        arrPtrs[i] = arr[i];
    }

	qsort(arr,m,sizeof(*arr),compare);
	cout << endl;
	for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++)
            cout << arr[i][j] << " ";
        cout<<endl;
    }

    for (int i = 0; i < 3; i++) {
        printf("%d %d\n", arrPtrs[i][0], arrPtrs[i][1]);
    }
	return 0;
}