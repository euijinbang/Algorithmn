#include<iostream>
using namespace std;
int main()
{
    int arr[6] = { 4, 9, 11, 8, 6, 2 };

    int result[6]; //내림차순 정렬

    for (int y = 0; y < 6; y++)
    {
        result[y] = arr[y];

        for (int x = y; x > 0; x--)
        {
            if (result[x - 1] < result[x])
            {
                swap(result[x - 1], result[x]);
            }
            else break;
        }
    }

    for (int x = 0; x < 6; x++)
    {
        cout << result[x] << " ";
    }

    return 0;
}