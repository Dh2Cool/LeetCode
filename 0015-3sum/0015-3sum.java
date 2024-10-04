class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> ans = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            int j = i+1;
            int k = nums.length-1;
            while(j<k){
                if(nums[j]+nums[k]==nums[i]*-1){
                    // List<Integer> temp = new ArrayList<>();
                    // temp.add(i);
                    // temp.add(j);
                    // temp.add(k);
                    // ans.add(temp);
                    ans.add(Arrays.asList(nums[i], nums[j], nums[k]));
                    j++;
                    while(nums[j] == nums[j-1] && j<k)
                        j++;
                }
                else if(nums[j]+nums[k]<nums[i]*-1){
                    j++;
                }
                else if(nums[j]+nums[k]>nums[i]*-1)
                    k--;
            }
        }
        return ans;
    }
}