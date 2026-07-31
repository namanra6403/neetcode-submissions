class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> indexes;
        int maxArea = 0;

        for(int i = 0; i <= n; i++) {
            while(!(indexes.empty()) && (i == n || (heights[indexes.top()] >= heights[i]))) {
                int h = heights[indexes.top()];
                indexes.pop();
                int w = indexes.empty() ? i : i - indexes.top() - 1;
                maxArea = max(maxArea, w * h);
            }
            indexes.push(i);
        }
        return maxArea;
    }
};
