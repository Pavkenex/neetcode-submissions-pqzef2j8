#include <map>
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int> values;
        int size = nums.size();
        for(int i=0;i<nums.size();i++){
            if(values.count(nums[i])==0)
            {
                values[nums[i]]=1;
            }else{
                return true;
            }
        }
        return false;
    }
};