class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> res = new HashSet<>();

        for(int i = 0; i<nums.length; i++)
            res.add(nums[i]);
        int longest = 0;
        for(int i = 0; i < nums.length; i++){
            if(!res.contains(nums[i] - 1)){
                int length = 1;
                while(res.contains(nums[i]+length))
                    length++;
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}