#include <unordered_set>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> values;
        int size = nums.size();
        for(int i=0;i<nums.size();i++){
            if(values.count(nums[i])==0)
            {
                values.insert(nums[i]);
            }else{
                return true;
            }
        }
        return false;
    }
};