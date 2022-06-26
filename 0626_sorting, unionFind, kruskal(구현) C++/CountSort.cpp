#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int arr[7] = { 3, 9, 1, 2, 1, 3, 4 };
    int bucket[11] = { 0 };
    for (int x = 0; x < 7; x++)
    {
        bucket[arr[x]]++;
    }
    for (int x = 1; x < 11; x++)
    {
        bucket[x] += bucket[x-1];
    }
    int result[11] = { 0 };
    for (int x = 0; x < 7; x++)
    {
        int t = arr[x];
        result[bucket[t--]] = t;
    }

    return 0;
}