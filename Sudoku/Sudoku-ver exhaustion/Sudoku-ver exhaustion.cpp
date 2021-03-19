// Sudoku-ver exhaustion.cpp
#include <iostream>
#include <set>
#include <cstring>
#include <algorithm>
#include <iterator>
#include <ctime>
#include <random>

using namespace std;

set<int> nineCell[4][4];
set<int> rSet[10];
set<int> cSet[10];

bool fix[10][10];
int table[10][10];

void SetXinCell(int r, int c, int x)
{
    nineCell[r / 3][c / 3].erase(x);
    rSet[r].erase(x);
    cSet[c].erase(x);
}

void RemoveXinCell(int r, int c, int x)
{
    nineCell[r / 3][c / 3].emplace(x);
    rSet[r].emplace(x);
    cSet[c].emplace(x);
}

#define Set(s) s.begin(), s.end()
set<int> findCandidate(int r, int c)
{
    set<int> tmp, res;
    set_intersection(Set(rSet[r]), Set(cSet[c]), inserter(tmp, tmp.begin()));
    set_intersection(Set(tmp), Set(nineCell[r / 3][c / 3]), inserter(res, res.end()));

    return res;
}

bool dfs(int r, int c)
{
    if (r == 9 && c == 0)
        return true;

    set<int> tmp = findCandidate(r, c);
    int Candidates[10];
    int n = 0;

    for (auto it : tmp)
        Candidates[n++] = it;

    random_shuffle(Candidates, Candidates + n);

    for (int i = 0, it; i < n; ++i)
    {
        it = Candidates[i];

        SetXinCell(r, c, it);
        fix[r][c] = true;
        table[r][c] = it;

        int _r = r, _c = c;
        while (fix[_r][_c])
        {
            ++_c;
            _r += _c / 9;
            _c %= 9;
        }

        if (dfs(_r, _c))
            return true;

        table[r][c] = 0;
        fix[r][c] = false;
        RemoveXinCell(r, c, it);
    }

    return false;
}

int main()
{
    for (int i = 0; i < 9; ++i)
        for (int j = 0; j < 9; ++j)
            for (int k = 1; k <= 9; ++k)
            {
                nineCell[i / 3][j / 3].emplace(k);
                rSet[i].emplace(k);
                cSet[j].emplace(k);
            }

    for (int i = 0; i < 9; ++i)
        for (int j = 0; j < 9; ++j)
        {
            cin >> table[i][j];
            if (table[i][j])
            {
                fix[i][j] = true;

                SetXinCell(i, j, table[i][j]);
            }
        }

    double START, END;
    START = clock();

    int r = 0, c = 0;
    while (fix[r][c])
    {
        ++c;
        r += c / 9;
        c %= 9;
    }

    dfs(r, c);

    cout << "\nanswer:" << '\n';

    for (int i = 0; i < 9; ++i)
    {
        for (int j = 0; j < 9; ++j)
        {
            cout << table[i][j] << ' ';
            if (!((j + 1) % 3))
                cout << ' ';
        }
        cout << '\n';
        if (!((i + 1) % 3))
            cout << '\n';
    }

    END = clock();

    cout << "execution time: " << (END - START) << " ms" << '\n';

    return 0;
}

/*
0 0 0  0 0 1  0 4 5
0 3 0  0 0 0  0 0 0
8 0 0  3 0 0  0 0 6

7 0 0  0 9 0  1 0 0
0 5 0  0 0 2  0 0 9
0 0 0  7 0 0  0 0 0

5 0 6  0 2 0  0 0 0
0 2 0  0 1 0  0 0 0
0 0 9  0 8 0  0 5 4
3474 ms
3058 ms
2914 ms
---
0 4 0  0 0 0  0 0 0
0 0 6  0 1 0  4 0 0
0 0 1  0 3 7  0 0 0

0 0 0  0 0 8  0 1 0
0 6 0  7 0 0  0 5 0
0 0 8  0 9 0  0 7 0

0 5 0  1 0 0  8 6 0
0 0 0  3 0 0  0 9 0
9 0 0  0 0 0  2 0 0
4300 ms
3995 ms
3947 ms
--- world hardest
8 0 0  0 0 0  0 0 0
0 0 3  6 0 0  0 0 0
0 7 0  0 9 0  2 0 0

0 5 0  0 0 7  0 0 0
0 0 0  0 4 5  7 0 0
0 0 0  1 0 0  0 3 0

0 0 1  0 0 0  0 6 8
0 0 8  5 0 0  0 1 0
0 9 0  0 0 0  4 0 0
1960 ms
3805 ms
3681 ms
---
0 0 0  0 0 5  4 0 6
0 0 0  0 0 0  0 0 0
0 0 0  2 0 8  0 5 0

0 1 3  0 9 0  8 0 7
0 0 4  0 0 0  0 0 1
0 0 0  8 0 0  0 0 9

0 0 8  0 0 1  9 0 0
0 2 0  7 3 0  0 0 0
5 0 0  0 0 0  0 7 0
10590 ms
2411 ms
2469 ms
---
0 7 2  0 3 0  0 8 9
5 0 0  8 0 0  0 0 0
8 0 0  0 4 0  0 0 0

0 0 0  9 0 2  8 7 0
0 0 3  0 0 5  0 2 0
0 0 0  0 0 0  0 0 0

3 0 0  0 1 0  5 0 0
0 0 7  0 0 0  0 0 0
0 0 0  0 0 0  6 9 1
2762 ms
2863 ms
2766 ms
---
2 0 0  0 0 0  0 0 8
7 0 0  0 9 0  0 0 0
6 0 5  0 3 0  0 0 0

3 0 0  0 0 0  6 0 0
0 0 8  4 0 7  9 0 0
1 0 0  6 8 0  0 0 0

0 0 3  2 0 0  0 0 1
0 5 0  0 0 0  0 0 6
0 0 0  8 0 0  0 4 0
181 ms
124 ms
122 ms
---
8 0 0  0 0 0  9 0 0
0 0 0  0 9 5  6 0 0
7 0 1  0 6 0  0 0 0

5 0 0  3 0 0  0 7 0
0 3 0  0 0 8  0 0 2
0 0 0  0 0 4  0 3 0

0 0 0  0 0 6  0 9 0
0 0 0  0 0 0  0 0 5
1 0 8  4 0 0  0 0 0
2041 ms
70 ms
72 ms
---
9 8 0  6 0 0  0 3 1
0 0 7  0 0 0  0 0 0
6 0 0  5 4 0  0 0 0

0 0 0  0 0 8  3 7 4
0 0 0  0 6 0  0 0 0
0 0 0  0 0 0  9 0 2

0 3 2  0 0 7  4 0 0
0 4 0  3 0 0  0 1 0
0 0 0  0 0 0  0 0 0
1494 ms
299 ms
296 ms
---
0 4 0  8 0 0  0 0 6
0 0 1  0 0 6  0 0 3
0 0 6  3 0 9  8 0 0

2 5 0  6 0 3  0 0 0
0 0 0  0 0 0  0 0 0
0 8 7  0 0 0  0 4 0

0 0 0  0 9 0  7 0 0
0 0 0  0 0 4  0 1 0
0 0 0  0 0 2  0 0 5
466 ms
38 ms
35 ms
---
4 1 0  0 0 0  0 0 0
0 0 3  0 0 0  0 2 9
0 0 0  0 0 4  0 6 0

0 0 0  7 0 0  0 9 0
0 0 7  4 0 0  0 0 2
0 0 0  0 0 8  0 0 5

6 7 0  0 0 1  0 0 0
0 0 9  0 2 0  0 0 3
0 3 0  0 0 9  0 5 0
10205 ms
8382 ms
8172 ms
*/