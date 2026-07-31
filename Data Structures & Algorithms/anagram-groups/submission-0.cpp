class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> words; // ordered word -> original
        vector<vector<string>> final;

        for(int i = 0; i < strs.size(); i ++) {
            string x = strs[i];
            sort(x.begin(), x.end());
            words[x].push_back(strs[i]);
        }

        for(auto&pair : words) {
            final.push_back(pair.second);
        }
    return final;
    }
};
