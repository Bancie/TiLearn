#include <iostream>
#include <cmath>
using namespace std; 
#define maxm 1000
#define maxn 1000
#define var 5 // <-- Variables Summarizing in Data File

// Scanning Data File
void readfile (int a[maxm][maxn], int &job_amount, int &prec, int &psum, int &job_scale) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data inp/na.inp","rt");
    fscanf(f, "%d", &job_amount);
    fscanf(f, "%d", &prec);
    fscanf(f, "%d", &psum);
    fscanf(f, "%d", &job_scale);
    for (int i=0; i<job_amount; i++) {
        for (int j=0; j<var; j++) {
            fscanf(f, "%d", &a[i][j]);
        }
    }
	fclose(f);
}

// Process Variable
double process (int i, int a[maxm][maxn], int job_amount, int job_scale) {
    double p = (double) (a[i][1]*job_amount)/job_scale;
    return p;
}

// Non-precedence p-factor Variable
double p_factor_nonprec (int i, int a[maxm][maxn], double p) {
    double p_factor_nonprec = (double) a[i][4]/p;
    return p_factor_nonprec;
}

// Precedence p-factor Variable
double p_factor_prec_tu (int i, int a[maxm][maxn], double p) {
    if (i<=0) {
        return 0;
    }
    return a[i][4] + p_factor_prec(i-1,a,p);
}
double p_factor_prec_mau (int i, int a[maxm][maxn], int job_amount, int job_scale, double p) {
    if (i<=0) {
        return 0;
    }
    return process(i,a,job_amount,job_scale) + process(i-1,a,job_amount,job_scale);
}
double p_factor_prec (int i, int a[maxm][maxn], int job_amount, int job_scale, double p) {
    return p_factor_prec_tu(i,a,p)/p_factor_prec_mau(i,a,job_amount,job_scale,p);
}


// Printing Output File
void writefile (int a[maxm][maxn], int job_amount, int prec, int psum, int job_scale) {
	FILE *f;
	f=fopen("/Users/chibangnguyen/Documents/schedulang/data/data out/na.out","wt");
	fprintf(f, "%d\n", job_amount);
    fprintf(f, "%d\n", prec);
    fprintf(f, "%d\n", psum);
    fprintf(f, "%d\n", job_scale);
    for (int i=0; i<job_amount; i++) {
        //double p_factor_nonprec = (double) a[i][4]/p;
        for (int j=0; j<var; j++) {
            fprintf(f, "%d ", a[i][j]);
        }
        if (prec==0) {
            fprintf(f, "%.4lf %.4lf\n", process(i,a,job_amount,job_scale), p_factor_nonprec(i,a,process(i,a,job_amount,job_scale)));
        } else if (prec==1) {
            fprintf(f, "%.4lf %.4lf\n", process(i,a,job_amount,job_scale), p_factor_nonprec(i,a,process(i,a,job_amount,job_scale)));
        }
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