#include<iostream>
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0) return 0;
        set<int>na;
        int nc=0;
        int max=0;
        int previous=INT_MIN;

        for(int i=0; i<nums.size();i++){
            if(na.count(nums[i])>0) continue;

            na.insert(nums[i]);
        }
        
        for(int element: na){
            cout<<element;

            if(element != previous + 1){
                nc=0;
            }else{
                nc++;
            }
            previous = element;

             if(max<nc)
                    max=nc;

        }
        return max+1;
    }
};
