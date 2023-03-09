class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> all;
        vector<int> partial;
        vector<bool> bitmask(nums.size(), true);
        bt(nums, bitmask, partial, all);
        return all;
    }
private:
    void bt(vector<int>& nums, vector<bool>& bitmask, vector<int>& partial, vector<vector<int>>& all){
        if(partial.size() == nums.size())
            all.push_back(partial);
        else{
            for(int i = 0; i < bitmask.size(); i++){
                if(bitmask[i]){
                    partial.push_back(nums[i]);
                    bitmask[i] = false;
                    bt(nums, bitmask, partial, all);
                    partial.pop_back();
                    bitmask[i] = true;
                }
            }
        }
    }
};