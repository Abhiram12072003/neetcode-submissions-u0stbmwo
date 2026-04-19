class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1 = 0, cnt2 = 0, a = 0, b = 0;
        int n = nums.size();
        int chk = n/3;
        vector<int> answer;
        for(int i=0; i<n; i++){
            if(cnt1==0){
                a = nums[i];
                cnt1 = 1;
            }
            else if(nums[i] != a && cnt2==0){
                b = nums[i];
                cnt2 = 1;
            }
            else if(nums[i] == a){
                cnt1++;
            }
            else if(nums[i] == b){
                cnt2++;
            }
            else{
                cnt1--;
                cnt2--;
            }
        }
        cnt1=0, cnt2=0;
        for(int i=0; i<n; i++){
            if(nums[i] == a)    cnt1++;
            if(nums[i] == b)    cnt2++;
        }
        if(cnt1>chk)    answer.push_back(a);
        if(cnt2>chk)    answer.push_back(b);
        return answer;
    }
};