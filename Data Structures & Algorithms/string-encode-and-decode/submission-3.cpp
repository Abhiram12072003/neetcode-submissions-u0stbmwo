class Solution {
public:

    string encode(vector<string>& strs) {
        string ans = "";
        int x = strs.size();
        string s = "";
        for(int i=0; i<x; i++){
            s += to_string(strs[i].size()) + ',';
        }
        s += '#';
        for(auto ele: strs) s += ele;
        cout<<s<<endl;
        return s;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int x = s.length();
        vector<int> len;
        string si = "";
        int brk = 0;
        for(int i=0; i<x; i++){
            if(s[i] == '#'){
                brk = i;
                break;
            }
            if(s[i]==','){
                len.push_back(stoi(si));
                si = "";
            }
            else    si += s[i];
        }
        int k = brk + 1;
        for(int i=0; i<len.size(); i++){
            string tmp = "";
            int j = 0;
            while(j<len[i]){
                tmp += s[k];
                k++;
                j++;
            }
            ans.push_back(tmp);
        }
        return ans;
    }
};
