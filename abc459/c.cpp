# include <iostream>
# include <string>
# include <fstream>
#include <ranges>
#include <algorithm>

using namespace std;

int main()
{
    int N, Q;
    cin >> N, Q;
    
    int masu[N];

    while (Q >= 1) {
        int qa, qb;
        cin >> qa >> qb;
        if (qa == 1) {
            masu[qa-1] ++;
            if (std::ranges::all_of(masu, [](int t) { return (t != 0); })) {
                for (int i=0; i>)
            }
        }
    }
}