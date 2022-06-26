#include<iostream>
using namespace std;

int arr[200];

char findboss(char member)
{
    if (arr[member] == 0) return member;
    char boss = findboss(arr[member]);
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
    setunion('A', 'B');
    setunion('E', 'F');
    setunion('B', 'F');
    setunion('C', 'D');
    setunion('F', 'A');

    char input1, input2;
    cin >> input1 >> input2;
    if (findboss(input) == findboss(input2))
    {
        cout << "같은그룹";
    }
    else cout << "다른그룹";
}

