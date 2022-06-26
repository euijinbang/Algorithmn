#include<iostream>
#include<vector>
using namespace std;

struct node {
    char a;
    char b;
    int cost;
};

vector<node>arr = {
    {'A', 'B', 5},
    {'A', 'C', 3},
    {'A', 'D', 2},
    {'A', 'E', 6},
    {'B', 'C', 7},
    {'B', 'E', 8},
    {'C', 'D', 4},
    {'C', 'E', 2}
};

char findboss(char target)
{
    if (arr[target] == 0) return target;
    char boss = findboss(arr[target]);

    // 효율성 - arr 보스를 재귀탔던 곳에 모두 갱신
    arr[target] = boss;

    return boss;
}

void setunion(char a, char b)
{
    char aboss = findboss(a);
    char bboss = findboss(b);
    if (aboss == bboss) return; // 보스 같으면 유니온 필요x
    arr[bboss] = aboss;
}

char brr[200];
bool compare(node front, node back) // cost 순으로 정렬
{
    front.cost < back.cost;
}
int main() {
    int n = arr.size();

    sort(arr.begin(), arr.end(), compare);

    int sum = 0;
    int cnt = 0;

    for (int x = 0; x < n; x++)
    {
        if(findboss(arr[x].a) != findboss(arr[x].b))
        {
            setunion(arr[x].a, arr[x].b);
            sum +-= arr[x].cost;
            cnt++;
            if (cnt == 4) break;
        }
    }

    cout << sum;

    return 0;
}




