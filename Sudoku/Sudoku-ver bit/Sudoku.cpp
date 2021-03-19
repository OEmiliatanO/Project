// Sudoku.cpp
#include <iostream>
#include <algorithm>
#include <cstring>
#include <ctime>

using namespace std;

constexpr int wi[11][11] = { {6,6,6,6,6,6,6,6,6,0,0},
                             {6,7,7,7,7,7,7,7,6,0,0},
                             {6,7,8,8,8,8,8,7,6,0,0},
                             {6,7,8,9,9,9,8,7,6,0,0},
                             {6,7,8,9,10,9,8,7,6,0,0},
                             {6,7,8,9,9,9,8,7,6,0,0},
                             {6,7,8,8,8,8,8,7,6,0,0},
                             {6,7,7,7,7,7,7,7,6,0,0},
                             {6,6,6,6,6,6,6,6,6,0,0} };

int table[11][11];
bool fix[11][11];

int nineCell[4][4];
int rSet[10], cSet[10];

int ans = -1;

inline int findCandidate(int r, int c)
{
    return nineCell[r / 3][c / 3] & rSet[r] & cSet[c];
}

inline void SetXinCell(int r, int c, int x)
{
    rSet[r] ^= (1 << x);
    cSet[c] ^= (1 << x);
    nineCell[r / 3][c / 3] ^= (1 << x);
}

bool dfs(int r, int c)
{
    if (r == 9 && c == 0)
    {
        int res = 0;
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j)
                res += table[i][j] * wi[i][j];

        ans = max(ans, res);

        return true;
    }

    int candidate = findCandidate(r, c) & ((1 << 10) - 1) ^ 1;

    for (int i = 1; candidate; ++i)
    {
        if (candidate & (1 << i))
        {
            SetXinCell(r, c, i);
            fix[r][c] = true;
            table[r][c] = i;
            candidate ^= (1 << i);

            int _r = r, _c = c;
            while (fix[_r][_c])
            {
                ++_c;
                _r += _c / 9;
                _c %= 9;
            }

            dfs(_r, _c);

            table[r][c] = 0;
            fix[r][c] = false;
            SetXinCell(r, c, i);
        }
    }

    return false;
}

int main()
{

    memset(fix, false, sizeof(fix));
    memset(nineCell, -1, sizeof(nineCell));
    memset(rSet, -1, sizeof(rSet));
    memset(cSet, -1, sizeof(cSet));

    /*
    for (int i = 0; i < 9; ++i, cout << '\n')
        for (int j = 0; j < 9; ++j)
            cout << '\t' << wi[i][j] << ' ';
    */

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

    //double START, END;
    //START = clock();

    int r = 0, c = 0;
    
    while (fix[r][c])
    {
        ++c;
        r += c / 9;
        c %= 9;
    }

    dfs(r, c);

    cout << ans << '\n';

    //END = clock();

    //cout << "execution time: " << (END - START) << " ms" << '\n';

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
17ms
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
23ms
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
25ms
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
41ms
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
15ms
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
11ms
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
18ms
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
11ms
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
6ms
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
43ms
*/
