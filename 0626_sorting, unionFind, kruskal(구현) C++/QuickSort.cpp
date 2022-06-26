#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int arr[6] = { 3, 6, 2, 1, 5, 8 };
    sort(arr, arr + 6, less<int>()); // 오름차순
    sort(arr, arr + 6, greater<int>()); // 내림차순

    string str = "kevinchoi";
    sort(str.begin(), str.end()); // 오름차순
    sort(str.begin(), str.end(), greater<char>());  // 내림차순

    string brr[4] = { "a", "j", "d", "e" }
    sort(brr, brr+4);
    sort(brr, brr+4, grater<string>());

    vector<int>vect= { 6, 3, 4, 6, 5, 2, 1, 9 };
    sort(vect.begin(), vect.end());
    sort(vect.begin(), vect.end(), greater<int>());

    vector<vector<int>>t={ {1, 2}, {3, 2}, {6, 2} }
    sort(t.begin(), t.end());
    sort(t.begin(), t.end(), greater<vector<int>>());

    pair<int, int>p;
    vector<pair<int, int>>pp = { {1, 2}, {3, 2}, {6, 2} };

    return 0;
}