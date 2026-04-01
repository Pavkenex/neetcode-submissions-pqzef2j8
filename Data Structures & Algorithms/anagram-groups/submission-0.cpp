#include<array>
#include<map>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        
        map<std::array<int,26>, vector<string>> values;

        for(const string value:strs){
            std::array<int,26> temp={0};
            for(const char& character: value){
                temp[character - 'a']++;
            }

            values[temp].push_back(value);

        }

        for(const auto& val: values){
            result.push_back(val.second);
        }
        return result;
    }
};
