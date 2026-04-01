class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
     //napravi mapu: frequency->number
    map<int,int> frequencyMap;
    for(int num: nums){
        frequencyMap[num]++;
    }

    vector<pair<int,int>> arr;

    for( const auto& val:frequencyMap)

    arr.push_back({val.second, val.first});
    sort(arr.rbegin(), arr.rend());

    vector<int> result;
    for(int i=0;i<k;i++){
        result.push_back(arr[i].second);
    }
    return result;
    }
    
};
