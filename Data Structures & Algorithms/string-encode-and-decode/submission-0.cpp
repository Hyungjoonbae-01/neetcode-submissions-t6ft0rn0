class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        for(int i=0;i<strs.size();i++){
            encodedString+= to_string(strs[i].length()) + "#" + strs[i];
        }
        cout<<encodedString;
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        while(s.size() !=0){
            int pos = s.find('#');
            string c = s.substr(0, pos);
            int length = stoi(c);
            string word = s.substr(pos+1, length);
            s.erase(0, length+pos+1);
            strs.push_back(word);
        }
        return strs;
    }
};
