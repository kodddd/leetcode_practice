#include <vector>
#include <iostream>
using namespace std;
class Solution {
    public:
        int removeElement(vector<int>& nums, int val) {
            int left = 0, right = nums.size();
            while (left < right) {
                if (nums[left] == val) {
                    nums[left] = nums[right - 1];
                    right--;
                } else {
                    left++;
                }
            }
            return left;
        }
    };
    
Solution solution;
int main() {
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    int len = solution.removeElement(nums, val);
    for(int i = 0; i < nums.size(); i++) {
        cout << nums[i] << " ";
    }
    return 0;
}