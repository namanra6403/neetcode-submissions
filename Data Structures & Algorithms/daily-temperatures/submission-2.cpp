class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> result(temperatures.size(), 0);
        stack<pair<int, int>> nums; // pair: {temp, index}

        for(int i = 0; i < temperatures.size(); i++) {
            int a = temperatures[i];
            while(!(nums.empty()) && a > nums.top().first) {
                auto val = nums.top();
                nums.pop();
                result[val.second] = i - val.second;
            }
            nums.push({a, i});
        }
        return result;
    }
};
