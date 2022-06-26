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
    vector<string>vect = {
        "AE",
        "BD",
        "FE",
        "CE",
        "DB",
        "CA"
    };

    int len = vect.size();
    int cnt = len;
    for (int x = 0; x < len; x++)
    {
        if (findboss(vect[x][0]) != findboss(vect[x][1]))
        {
            setunion(vect[x][0], vect[x][1]);
            cnt--;  // 전체 길이 - 그룹화 횟수
        }
    }
    cout << cnt;

    return 0;
}

