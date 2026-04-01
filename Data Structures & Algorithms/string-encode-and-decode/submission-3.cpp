class Solution {
public:

    string encode(vector<string>& strs) {
        if(strs.empty()){return "";}
        string words="#";
        string sizes="";
        for(string s: strs){
          sizes+= to_string(s.length()) + ',';
          words+=s;
        }   
        return sizes+words;
    }

    vector<string> decode(string s) {

        if(s.empty()){
            return {};
        }
        vector<string> decoded;
        vector<int> sizes;
       
        int i =0;
        while(s[i]!='#'){
            string curr ="";
            while(s[i]!=','){
                curr+=s[i];
                i++;
            }
            sizes.push_back(stoi(curr));
            i++;
        }
        i++;
        for(int size:sizes){
            decoded.push_back(s.substr(i,size));
            i+=size;
        }
          return decoded;
    }
};
