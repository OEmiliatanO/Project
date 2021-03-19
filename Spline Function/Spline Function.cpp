#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

constexpr double datSeed = -1, datStep = 0.1;
constexpr int dataCnt = 21;
constexpr double st = datSeed, ed = datSeed + ((double)dataCnt - 1.0) * datStep, step = 0.001;
constexpr int Type = 0;

double f(double x)
{
    return 1 / (1 + 25 * x * x);
}
double df(double x)
{
    double dx = 10e-8;
    if (isnan(f(x + dx)) || isinf(f(x + dx)))
        return (f(x) - f(x - dx)) / dx;
    return (f(x + dx) - f(x)) / dx;
}
double ddf(double x)
{
    double dx = 10e-8;
    if (isnan(df(x + dx)) || isinf(df(x + dx)))
        return (df(x) - df(x - dx)) / dx;
    return (df(x + dx) - df(x)) / dx;
}

void setSample(vector<double>& v, vector<double>& u)
{
    v.clear(); u.clear();

    double x = datSeed;
    for (int i = 0; i < dataCnt; x += datStep, ++i)
        v.emplace_back(x), u.emplace_back(f(x));
}

vector<double> SampleX;
vector<double> SampleY;
vector<double> g;
vector<double> k;
vector<vector<double>> A;
vector<double> m;
int SampleN;

void bondType1_SetMat(vector<vector<double>>& A, vector<double>& k)
{
    k[0] = 6 * (SampleY[1] - SampleY[0] - df(SampleX[0])) / (g[1] * g[1]);
    k[SampleN] = 6 * ((SampleY[SampleN - 1] - SampleY[SampleN]) / g[SampleN] - df(SampleX[SampleN])) / g[SampleN];

    A.resize(SampleN + 1);
    for (int i = 0; i < SampleN + 1; ++i)
        A[i].resize(SampleN + 1);
    for (int i = 1; i < SampleN; ++i)
    {
        A[i][i - 1] = g[i] / (g[i] + g[i + 1]);
        A[i][i] = 2;
        A[i][i + 1] = g[i + 1] / (g[i] + g[i + 1]);
    }
    A[0][0] = 2, A[0][1] = 1, A[SampleN][SampleN] = 2, A[SampleN][SampleN - 1] = 1;
}
void bondType2_SetMat(vector<vector<double>>& A, vector<double>& k)
{
    k[1] -= (SampleX[0] - SampleX[1]) * ddf(SampleX[0]) / (SampleX[0] - SampleX[2]);
    k[SampleN - 1] -= (SampleX[SampleN - 1] - SampleX[SampleN]) * ddf(SampleX[SampleN]) / (SampleX[SampleN - 2] - SampleX[SampleN]);

    A.resize(SampleN + 1);
    for (int i = 0; i < SampleN + 1; ++i)
        A[i].resize(SampleN + 1);
    for (int i = 2; i < SampleN - 1; ++i)
    {
        A[i][i - 1] = g[i] / (g[i] + g[i + 1]);
        A[i][i] = 2;
        A[i][i + 1] = g[i + 1] / (g[i] + g[i + 1]);
    }
    A[1][1] = 2, A[1][2] = (SampleX[1] - SampleX[2]) / (SampleX[0] - SampleX[2]);
    A[SampleN - 1][SampleN - 1] = 2, A[SampleN - 1][SampleN - 2] = (SampleX[SampleN - 2] - SampleX[SampleN - 1]) / (SampleX[SampleN - 2] - SampleX[SampleN]);
}

void bondType1(vector<vector<double>>& A, vector<double>& m, vector<double>& k)
{
    vector<double> l, d, u, w;
    l.resize(SampleN + 1); d.resize(SampleN + 1); u.resize(SampleN + 1), w.resize(SampleN + 1);

    d[0] = A[0][0], u[0] = A[0][1] / d[0], w[0] = k[0] / d[0];
    for (int i = 1; i <= SampleN; ++i)
    {
        l[i] = A[i][i - 1];
        d[i] = A[i][i] - l[i] * u[i - 1];
        if (i < SampleN)
            u[i] = A[i][i + 1] / d[i];
        w[i] = (k[i] - l[i] * w[i - 1]) / d[i];
    }

    m[SampleN] = w[SampleN];
    for (int i = SampleN - 1; i >= 0; --i)
    {
        m[i] = w[i] - m[i + 1] * u[i];
    }
}
void bondType2(vector<vector<double>>& A, vector<double>& m, vector<double>& k)
{
    vector<double> l, d, u, w;
    l.resize(SampleN + 1); d.resize(SampleN + 1); u.resize(SampleN + 1), w.resize(SampleN + 1);

    d[1] = 2, u[1] = A[1][2] / d[1], w[1] = k[1] / d[1];
    for (int i = 2; i < SampleN; ++i)
    {
        l[i] = A[i][i - 1];
        d[i] = 2 - l[i] * u[i - 1];
        if (i < SampleN - 1)
            u[i] = A[i][i + 1] / d[i];
        w[i] = (k[i] - l[i] * w[i - 1]) / d[i];
    }

    m[SampleN - 1] = w[SampleN - 1];
    for (int i = SampleN - 2; i >= 1; --i)
    {
        m[i] = w[i] - m[i + 1] * u[i];
    }
    m[0] = ddf(SampleX[0]);
    m[SampleN] = ddf(SampleX[SampleN]);
}

double s(double x)
{
    if ((x < SampleX[0]) || (x > *SampleX.rbegin()))
        return 0.0;

    int i = 1;
    while (x > SampleX[i]) ++i;
    double res = 0.0;
    res = (x - SampleX[i]) * (x - SampleX[i]) * (x - SampleX[i]) * m[i - 1] + (SampleX[i - 1] - x) * (SampleX[i - 1] - x) * (SampleX[i - 1] - x) * m[i];
    res /= (6 * g[i]);
    res += ((SampleY[i - 1] - SampleY[i]) / g[i] + g[i] * (m[i] - m[i - 1]) / 6) * x;
    res += SampleY[i] - (g[i] * g[i] * m[i]) / 6 - ((SampleY[i - 1] - SampleY[i]) / g[i] + (m[i] - m[i - 1]) * g[i] / 6) * SampleX[i];

    return res;
}

int main()
{
    setSample(SampleX, SampleY);

    SampleN = SampleX.size() - 1;

    g.resize(SampleN + 1);
    for (int i = 1; i <= SampleN; ++i)
        g[i] = SampleX[i - 1] - SampleX[i];

    k.resize(SampleN + 1);
    for (int i = 1; i < SampleN; ++i)
        k[i] = ((SampleY[i - 1] - SampleY[i]) / g[i] + (SampleY[i + 1] - SampleY[i]) / g[i + 1]) * 6 / (g[i] + g[i + 1]);

    m.resize(SampleN + 1);

    bondType1_SetMat(A, k);
    bondType1(A, m, k);

    fstream fs;
    fs.open("function1.txt", ios::out);

    for (double x = st; x <= ed; x += step)
    {
        fs << f(x) << endl;
        fs << s(x) << endl;
    }
    fs.close();


    bondType2_SetMat(A, k);
    bondType2(A, m, k);

    fs.open("function2.txt", ios::out);

    for (double x = st; x <= ed; x += step)
    {
        fs << f(x) << endl;
        fs << s(x) << endl;
    }
    fs.close();

    fs.open("xy.txt", ios::out);

    fs << SampleN + 1 << endl;
    for (int i = 0; i < SampleN + 1; ++i)
    {
        fs << SampleX[i] << endl;
        fs << SampleY[i] << endl;
    }
    fs.close();

    cout << st << " " << ed << endl;

    return 0;
}
