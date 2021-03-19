// Sudoku-ver DLX.cpp
#include <iostream>
#include <algorithm>
#include <ctime>

#define LL long long
#define rgi register int
#define il inline

using namespace std;

const int N = 1e6 + 10;
int ans[10][10], stk[N];

struct DLX {
    static const int MAXSIZE = 1e5 + 10;
#define IT(i, A, x) for(i = A[x]; i != x; i = A[i])
    int n, m, tot, first[MAXSIZE + 10], siz[MAXSIZE + 10];
    int L[MAXSIZE + 10], R[MAXSIZE + 10], U[MAXSIZE + 10], D[MAXSIZE + 10];
    int col[MAXSIZE + 10], row[MAXSIZE + 10];
    void build(const int& r, const int& c) {
        n = r, m = c;
        for (rgi i = 0; i <= c; ++i) {
            L[i] = i - 1, R[i] = i + 1;
            U[i] = D[i] = i;
        }
        L[0] = c, R[c] = 0, tot = c;
        memset(first, 0, sizeof(first));
        memset(siz, 0, sizeof(siz));
    }
    void insert(const int& r, const int& c) {
        col[++tot] = c, row[tot] = r, ++siz[c];
        D[tot] = D[c], U[D[c]] = tot, U[tot] = c, D[c] = tot;
        if (!first[r]) first[r] = L[tot] = R[tot] = tot;
        else {
            R[tot] = R[first[r]], L[R[first[r]]] = tot;
            L[tot] = first[r], R[first[r]] = tot;
        }
    }
    void remove(const int& c) {
        rgi i, j;
        L[R[c]] = L[c], R[L[c]] = R[c];
        IT(i, D, c) IT(j, R, i)
            U[D[j]] = U[j], D[U[j]] = D[j], --siz[col[j]];
    }
    void recover(const int& c) {
        rgi i, j;
        IT(i, U, c) IT(j, L, i)
            U[D[j]] = D[U[j]] = j, ++siz[col[j]];
        L[R[c]] = R[L[c]] = c;
    }
    bool dance(int dep) {
        rgi i, j, c = R[0];
        if (!R[0]) {
            for (i = 1; i < dep; ++i) {
                int x = (stk[i] - 1) / 9 / 9 + 1;
                int y = (stk[i] - 1) / 9 % 9 + 1;
                int v = (stk[i] - 1) % 9 + 1;
                ans[x][y] = v;
            }
            return 1;
        }
        IT(i, R, 0) if (siz[i] < siz[c]) c = i;
        remove(c);
        IT(i, D, c) {
            stk[dep] = row[i];
            IT(j, R, i) remove(col[j]);
            if (dance(dep + 1)) return 1;
            IT(j, L, i) recover(col[j]);
        }
        recover(c);
        return 0;
    }
} solver;
int GetId(int row, int col, int num) { return (row - 1) * 9 * 9 + (col - 1) * 9 + num; }
void Insert(int row, int col, int num) {
    int dx = (row - 1) / 3 + 1;
    int dy = (col - 1) / 3 + 1;
    int room = (dx - 1) * 3 + dy;
    int id = GetId(row, col, num);
    int f1 = (row - 1) * 9 + num; // task 1
    int f2 = 81 + (col - 1) * 9 + num; // task 2
    int f3 = 81 * 2 + (room - 1) * 9 + num; // task 3
    int f4 = 81 * 3 + (row - 1) * 9 + col; // task 4
    solver.insert(id, f1);
    solver.insert(id, f2);
    solver.insert(id, f3);
    solver.insert(id, f4);
}
int main() {

    solver.build(729, 324);
    for (int i = 1; i <= 9; ++i) for (int j = 1; j <= 9; ++j) {
        cin >> ans[i][j];
        for (int v = 1; v <= 9; ++v) {
            if (ans[i][j] && ans[i][j] != v) continue;
            Insert(i, j, v);
        }
    }

    double START, END;
    START = clock();

    solver.dance(1);
    for (int i = 1; i <= 9; ++i)
    {
        for (int j = 1; j <= 9; ++j)
            cout << ans[i][j] << ' ';
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
5 ms
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
4 ms
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
6 ms
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
7 ms
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
5 ms
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
5 ms
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
6 ms
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
4 ms
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
7 ms
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
4 ms

*/