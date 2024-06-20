#include <iostream>
#include <cmath>
using namespace std; 
#define maxm 1000
#define maxn 1000
void readfile(int a[maxm][maxn], int &soluong, int &prec, int &psum, int &amount) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data inp/na.inp","rt");
    fscanf(f, "%d", &soluong);
    fscanf(f, "%d", &prec);
    fscanf(f, "%d", &psum);
    fscanf(f, "%d", &amount);
    for (int i=0; i<soluong; i++) {
        for (int j=0; j<5; j++) {
            fscanf(f, "%d", &a[i][j]);
        }
    }
	fclose(f);
}
void writefile(int a[maxm][maxn], int soluong, int prec, int psum, int amount) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data out/na.out","wt");
	fprintf(f, "%d\n", soluong);
    fprintf(f, "%d\n", prec);
    fprintf(f, "%d\n", psum);
    fprintf(f, "%d\n", amount);
    for (int i=0; i<soluong; i++) {
        double p = (double) (a[i][1]*soluong)/amount;
        for (int j=0; j<5; j++) {
            fprintf(f, "%d ", a[i][j]);
        }
        fprintf(f, "%.4lf\n", p);
    }
	fclose(f);
}
int main () {
	int a[maxm][maxn];
    int soluong, psum, amount;
    int prec;
    readfile(a, soluong, prec, psum, amount);
    writefile(a, soluong, prec, psum, amount);
	return 0;
} 