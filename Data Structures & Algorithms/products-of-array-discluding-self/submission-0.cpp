class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int>results;
        for(int i=0;i<nums.size();i++){
            int result=1;
            for(int j=0;j<nums.size();j++){
                if(i!=j){
                    result*=nums[j];
                }
            }
            results.push_back(result);
        }
        return results;
    }
};
