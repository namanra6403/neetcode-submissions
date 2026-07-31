class Solution {
public:

    string encode(vector<string>& strs) {
        string statement;
        for(auto s : strs) {
            statement = statement + "?" + s;
        }
        statement = statement + "?";
        cout << statement;
        return statement;
    }

    vector<string> decode(string s) {
        vector<string> statement; 
        string one_word;

        for(int i = 0; i < s.size(); i++) {
            if(s[i] != '?') {
            one_word += s[i];
            cout << one_word << endl;
            }
            else if (s[i] == '?') {
                statement.push_back(one_word);
                one_word = "";
            }
        }

        if (!one_word.empty()) {
            statement.push_back(one_word);  // Add last word if exists
        }

        statement.erase(statement.begin());

        return statement;
    }
};
