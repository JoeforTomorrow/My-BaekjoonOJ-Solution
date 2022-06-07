#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <functional>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <bitset>

#define xx first
#define yy second
#define all(x) (x).begin(), (x).end()

using namespace std;
using i64 = long long int;
using ii = pair<int, int>;
using ii64 = pair<i64, i64>;

i64 gcd(i64 a, i64 b) {
	while(b != 0) {
		i64 r = a % b;
		a = b;
		b = r;
	}
	return a;
}

i64 lcm(i64 a, i64 b) {
    return a * b / gcd(a, b);
}

int     main()
{
    int n;
    scanf("%d", &n);
    
    vector<ii64> v(n);
    for (int i = 0; i < n; i++) {
        scanf("%lld", &v[i].yy);
        v[i].xx = 1;
    }
    
    i64 a = v[0].xx, b = v[0].yy;
    for (int i = 1; i < n; i++) {
        i64 lcmv = lcm(v[i].yy, b);
        v[i].xx = lcmv / v[i].yy * v[i].xx;
        a = lcmv / b * a + v[i].xx;
        b = lcmv;
    }
    
    i64 gcdv = gcd(a, b);
    
    printf("%lld/%lld\n", b/gcdv, a/gcdv);

    return 0;
}