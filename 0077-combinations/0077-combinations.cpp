class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> all;
        vector<int> partial;
        bt(n, k, 1, partial, all);
        return all;
    }
private:
    void bt(int n, int k,int i, vector<int>& partial, vector<vector<int>>& all){
        if(k == 0){
            all.push_back(partial);
            return;
        }
        else{
            for(int j = i; j <= n ; j++){
                partial.push_back(j);
                bt(n, k-1, j+1, partial, all);
                partial.pop_back();
            }
        }
    }
};