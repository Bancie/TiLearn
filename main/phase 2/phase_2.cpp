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
    int job_amount;
    // SCANNING DATA FILE <---- NON-PRECEDENCE DATA (na.out)
    void readfile () {
        FILE *f;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/na.out","rt");
            fscanf(f, "%d", &prec);
            fscanf(f, "%d", &job_amount);
            for (int i=0; i<maxm; i++) {
                for (int j=0; j<var; j++) {
                    fscanf(f, "%d", &a[i][j]);
                }
            }
        fclose(f);
    }

    // SORTING
    int count_rows (int a[maxm][maxn]) {
        for (int i=0; i<=job_amount; i++) {
            for (int j=0; j<=7; j++) {
                
            }
        }
    }


    // PRINTING OUTPUT FILE ----> NON-PRECEDENCE SORTING (nonprec_sorting.out)
    void writefile () { 
        FILE *f;
        double sum=0;
        f=fopen("/Users/chibangnguyen/Documents/TiLearn/data/nonprec_sorting.out","wt");
        fprintf(f, "abc");
        fclose(f);
    }
};

int main () {
    Job_Type type1;
    type1.readfile();
    type1.writefile();
	return 0;
} 