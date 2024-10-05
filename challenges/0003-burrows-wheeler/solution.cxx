#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <tuple>
#include <iterator>

using namespace std;

typedef struct shift {
    int index, first_half_rank, second_half_rank;
    shift(): index(-1), first_half_rank(-1), second_half_rank(-1) {}
} suffix;

bool operator <(const shift &s, const shift &o)
{
   return make_tuple(s.first_half_rank, s.second_half_rank) < make_tuple(o.first_half_rank, o.second_half_rank);
}


vector<shift> sorted_cyclic_shifts(const string &s)
{
    int n = static_cast<int>(size(s));
    vector<shift> shifts(n);
    vector<int> ranks(n);

    for (int i = 0; i < n; ++i) {
        shifts[i].index = i;
        ranks[i] = s[i] - 32;
    }

    int limit = 2 * n;

    for (int length = 2; length < limit; length *= 2) {
        auto h = length / 2;

        for (int i = 0; i < n; ++i) {
            shifts[i].first_half_rank = ranks[shifts[i].index];
            shifts[i].second_half_rank = ranks[(shifts[i].index + h) % n];
        }

        sort(begin(shifts), end(shifts));

        int current_rank = 0;

        ranks[shifts[0].index] = current_rank;
        for (int i = 1, current_rank = 0; i < n; ++i) {
            auto previous_shift_rank = make_tuple(shifts[i-1].first_half_rank, shifts[i-1].second_half_rank);
            auto current_shift_rank = make_tuple(shifts[i].first_half_rank, shifts[i].second_half_rank);

            if (previous_shift_rank != current_shift_rank) {
                ++current_rank;
            }

            ranks[shifts[i].index] = current_rank;
        }
    }

    return shifts;
}

int main()
{
    string s, t;

    while (getline(cin, s)) {
        int n = static_cast<int>(size(s));
        auto shifts = sorted_cyclic_shifts(s);
        string t;

        for (const auto &sh: shifts) {
            t.push_back(s[(sh.index + n - 1) % n]);
        }

        cout << t << endl;
    }

    return 0;
}

