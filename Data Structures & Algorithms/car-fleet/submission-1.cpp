class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;

        for(int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }
        sort(cars.rbegin(), cars.rend());

        vector<double> time;

        for(int i = 0; i < cars.size(); i++) {
            time.push_back((double)(target - cars[i].first)/ cars[i].second);
            if(time.size() >= 2 && time.back() <= time[time.size() - 2]) {
                time.pop_back();
            }
        }
        return time.size();
    }
};
