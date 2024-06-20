#include <iostream>
#include <cmath>
using namespace std; 
#define maxm 1000
#define maxn 1000
//Reading and writing data platform
void readfile(int a[maxm][maxn], int &job_amount, int &prec, int &psum, int &job_scale) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data inp/na.inp","rt");
    fscanf(f, "%d", &job_amount);
    fscanf(f, "%d", &prec);
    fscanf(f, "%d", &psum);
    fscanf(f, "%d", &job_scale);
    for (int i=0; i<job_amount; i++) {
        for (int j=0; j<5; j++) {
            fscanf(f, "%d", &a[i][j]);
        }
    }
	fclose(f);
}
void writefile(int a[maxm][maxn], int job_amount, int prec, int psum, int job_scale) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data out/na.out","wt");
	fprintf(f, "%d\n", job_amount);
    fprintf(f, "%d\n", prec);
    fprintf(f, "%d\n", psum);
    fprintf(f, "%d\n", job_scale);
    for (int i=0; i<job_amount; i++) {
        double p = (double) (a[i][1]*job_amount)/job_scale;
        double p_factor = (double) a[i][4]/p;
        for (int j=0; j<5; j++) {
            fprintf(f, "%d ", a[i][j]);
        }
        fprintf(f, "%.4lf %.4lf\n", p, p_factor);
    }
	fclose(f);
}
int main () {
	int a[maxm][maxn];
    int job_amount, psum, job_scale;
    int prec;
    readfile(a, job_amount, prec, psum, job_scale);
    writefile(a, job_amount, prec, psum, job_scale);
	return 0;
} 