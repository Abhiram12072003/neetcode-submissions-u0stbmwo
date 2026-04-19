class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        vector<int> cnt(100000,0);
        int mn = *min_element(nums.begin(), nums.end());
        if(mn>1)    return 1;
        for(auto ele: nums){
            cnt[ele-mn]++;
        }
        int x = 0;
        for(int i=0; i<cnt.size(); i++){
            if(cnt[i]==0 && i+mn>0)   return i+mn;
        }
        return 100001;
    }
};