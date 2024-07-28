#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
using namespace std; 
#define maxm 1000
#define maxn 1000
#define var 5 // <-- Variable Summarized from Data File

class Job_Type {
    public:
    int a[maxm][maxn];
    int prec;
    int plan_time;
    char line[maxm];
    // SCANNING DATA FILE
    void readfile () {
        FILE *f;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/na.inp","rt");
            fscanf(f, "%d", &prec);
            fscanf(f, "%d", &plan_time);
            for (int i=0; i<maxm; i++) {
                for (int j=0; j<var; j++) {
                    fscanf(f, "%d", &a[i][j]);
                }
            }
        fclose(f);
    }

    // NECESSARY VARIABLES
        // Amount of Job
        int job_amount (int a[maxm][maxn]) {
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
        int jobscale (int a[maxm][maxn], int job_amount) {
            int sum=0;
            for (int i=0; i<job_amount; i++) {
                for (int j=0; j<1; j++) {
                    sum += a[i][1];
                }
            }
            return sum;
        }
        // Process Variable
        double process (int i, int a[maxm][maxn], int &plan_time, int job_scale) {
            double p = (double) (a[i][1]*plan_time)/job_scale;
            return p;
        }
        // Non-precedence p-factor Variable
        double p_factor_nonprec (int i, int a[maxm][maxn], double p) {
            double p_factor_nonprec = (double) a[i][4]/p;
            return p_factor_nonprec;
        }
        // Precedence p-factor Variable
        double p_factor_prec_tu (int i, int a[maxm][maxn], double p) {
            if (i<0) {
                return 0;
            }
            return a[i][4] + p_factor_prec_tu(i-1,a,p);
        }
        double p_factor_prec (int i, int a[maxm][maxn], int job_amount, int job_scale, double p, double sum) {
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
                fprintf(f, "%d ", a[i][j]);
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
};

int main () {
    Job_Type type1;
    type1.readfile();
    type1.writefile();
	return 0;
} 