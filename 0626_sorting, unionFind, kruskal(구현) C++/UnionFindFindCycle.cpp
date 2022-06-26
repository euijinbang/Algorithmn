#include<iostream>
#include<vector>
using namespace std;

int arr[200];

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

int main()
{
    int n;
    cin >> n;
    for (int x = 0; x < n; x++)
    {
        int a, b;
        cin >> a >> b; // 간선 정보 입력
        if (findboss(a) == findboss(b)) // 보스가 같으면 cycle 존재
        {
            cout << "cycle 존재";
            return 0;
        }
        setunion(a, b);
    }
    cout << "cycle 없음";
    return 0;
}

