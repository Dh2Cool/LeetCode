class Solution {
    public int[] twoSum(int[] nums, int target) {
        int pos[] = new int[2];
        HashMap<Integer, Integer> table = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(table.containsKey(target - nums[i])){
                pos[0] = i;
                pos[1] = table.get(target - nums[i]);
            }
            else{
                table.put(nums[i], i);
            }
        }
        return pos;
    }
}