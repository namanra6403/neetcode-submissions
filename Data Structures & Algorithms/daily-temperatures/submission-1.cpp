class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res;
        for(int i = 0; i < temperatures.size(); i++) {
            for(int j = i+1; j < temperatures.size(); j++) {
                if(temperatures[i] < temperatures[j]) {
                    res.push_back(j-i);
                    break;
                }
                if((j+1) == temperatures.size()) {
                    res.push_back(0);
                }
            }
            if((i+1) == temperatures.size()) {
                res.push_back(0);
            }
        }
        return res;
    }
};
