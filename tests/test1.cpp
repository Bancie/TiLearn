#include <iostream>
#include <random>
#include <algorithm>
using namespace std;

int main()
{
    int ar[3][2] = {{3,2},
                    {2,6},
                    {1,7}};

    // populate with random data
    /*
    random_device rd;
    default_random_engine rng(rd());
    uniform_int_distribution<> dist(1,20);
    for_each(begin(ar), end(ar),
        [&](int (&ar)[2]){ ar[0] = dist(rng); ar[1] = dist(rng); });

    cout << "Before Sort..." << '\n';
    for_each(begin(ar), end(ar),
        [](const int(&ar)[2]) { cout << ar[0] << ',' << ar[1] << '\n';});
    */

    qsort(ar, 3, sizeof(*ar),
        [](const void *arg1, const void *arg2)->int {
            int const *lhs = static_cast<int const*>(arg1);
            int const *rhs = static_cast<int const*>(arg2);
            return (lhs[0] < rhs[0]) ? -1
                :  ((rhs[0] < lhs[0]) ? 1
                :  (lhs[1] < rhs[1] ? -1
                :  ((rhs[1] < lhs[1] ? 1 : 0))));
        }
    );

    cout << "After Sort..." << '\n';
    for_each(begin(ar), end(ar),
        [](const int(&ar)[2]) { cout << ar[0] << ',' << ar[1] << '\n';});

    return 0;
}