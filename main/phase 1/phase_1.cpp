#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std; 
#define maxm 1000
#define maxn 1000
#define var 5 // <-- Variable Summarized from Data File

int compare(const void *a, const void *b) {
    double *rowA = *(double **)a;
    double *rowB = *(double **)b;
    if (rowA[6] > rowB[6]) return -1;
    if (rowA[6] < rowB[6]) return 1;
    return 0;
}

class Job_Type {
    public:
    double a[maxm][maxn];
    int prec;
    int plan_time;
    
    // SCANNING DATA FILE
    void readfile () {
        FILE *f;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/na.inp","rt");
            fscanf(f, "%d", &prec);
            fscanf(f, "%d", &plan_time);
            for (int i=0; i<maxm; i++) {
                for (int j=0; j<var; j++) {
                    fscanf(f, "%lf", &a[i][j]);
                }
            }
        fclose(f);
    }

    // NECESSARY VARIABLES
    // Amount of Job
    int job_amount (double a[maxm][maxn]) {
        int sum=0;
        for (int i=0; i<maxm; i++) {
            if (a[i][0]==0)
                break;
            for (int j=0; j<1; j++)
                sum ++;
        }
        return sum;
    }
    // Scaling Job
    int jobscale (double a[maxm][maxn], int job_amount) {
        int sum=0;
        for (int i=0; i<job_amount; i++) {
            for (int j=0; j<1; j++) {
                sum += a[i][1];
            }
        }
        return sum;
    }
    // Process Variable
    double process (int i, double a[maxm][maxn], int &plan_time, int job_scale) {
        double p = (double) (a[i][1]*plan_time)/job_scale;
        return p;
    }
    // Non-precedence p-factor Variable
    double p_factor_nonprec (int i, double a[maxm][maxn], double p) {
        double p_factor_nonprec = (double) a[i][4]/p;
        return p_factor_nonprec;
    }
    // Precedence p-factor Variable
    double p_factor_prec_tu (int i, double a[maxm][maxn], double p) {
        if (i<0) {
            return 0;
        }
        return a[i][4] + p_factor_prec_tu(i-1,a,p);
    }
    double p_factor_prec (int i, double a[maxm][maxn], int job_amount, int job_scale, double p, double sum) {
        return p_factor_prec_tu(i,a,p)/sum;
    }

    // PRINTING OUTPUT FILE
    void writefile () {
        FILE *f;
        double sum=0;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/na.out","wt");
        fprintf(f, "%d\n", prec);
        // Summarizing the amount of job
        for (int i=0; i<job_amount(a); i++) {
            for (int j=0; j<var; j++) {
                fprintf(f, "%lf ", a[i][j]);
            }
            // Non-Precedence Job Type
            if (prec==0) {
                fprintf(f, "%.1lf %lf\n", 
                    process(
                        i, a, plan_time,
                        jobscale(a,job_amount(a))
                    ),
                    p_factor_nonprec(
                        i, a,
                        process(
                            i,a,plan_time,
                            jobscale(a,job_amount(a))
                        )
                    )
                );
            }
            // Precedence Job Type
            else if (prec==1) {
                sum += process(i,a,plan_time,jobscale(a,job_amount(a)));
                double p = process(
                    i, a, plan_time,
                    jobscale(a,job_amount(a))
                );
                fprintf(f, "%.1lf %lf\n",
                    p,
                    p_factor_prec(
                        i, a, job_amount(a),
                        jobscale(a,job_amount(a)),
                        p, sum
                    )
                );
            }
        }
        fclose(f);
    }

    void readfile_2 () {
        FILE *f;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/na.out","rt");
            fscanf(f, "%d", &prec);
            for (int i=0; i<job_amount(a); i++) {
                for (int j=0; j<7; j++) {
                    fscanf(f, "%lf", &a[i][j]);
                }
            }
        fclose(f);
    }

    void sorting (int job_amount) {
        int ja = job_amount;
        double *arrPtrs[ja];
        for (int i=0; i<ja; i++) {
            arrPtrs[i] = a[i];
        }
        qsort(arrPtrs, ja, sizeof(double *), compare);
        for (int i=0; i<ja; i++) {
            for (int j=0; j<7; j++) {
                printf("%lf ", arrPtrs[i][j]);
            }
            printf("\n");
        }
    }

    void writefile_2 () { 
        FILE *f;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/nonprec_sorting.out","wt");
        fclose(f);
    }
};

int main () {
    Job_Type type1;
    type1.readfile();
    type1.writefile();
    type1.readfile_2();
    type1.writefile_2();
    type1.sorting(10);
	return 0;
} 