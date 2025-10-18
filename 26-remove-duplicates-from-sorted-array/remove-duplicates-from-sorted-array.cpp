#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        unordered_set<int> unique_set(nums.begin(), nums.end());
        nums.assign(unique_set.begin(), unique_set.end());
        sort(nums.begin(),nums.end());
        return nums.size();
    }
};