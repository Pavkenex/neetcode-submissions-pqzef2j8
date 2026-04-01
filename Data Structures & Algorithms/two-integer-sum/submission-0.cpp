#include<unordered_map>
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> result;
        unordered_map<int, int> differenceMap;

        for(int i=0; i< nums.size();i++)
        {
            int difference = target - nums[i];
            if(differenceMap.count(difference)>0)
            {
                if(differenceMap[difference] < i){
                    result.push_back(differenceMap[difference]);
                    result.push_back(i);
                }else
                {
                    result.push_back(i);
                    result.push_back(differenceMap[difference]);
                }

                return result;
            }

            differenceMap[nums[i]]=i;
        }

        
    }
};
