class Solution {
    public int[] productExceptSelf(int[] nums) {
        int arr[] = new int[nums.length];
        int n = nums.length;
        int left = 1, right = 1;
        for(int i = 0; i < n; i++){
            arr[i] = left;
            left = left*nums[i];
        }
        for(int i = n-1; i>=0; i--){
            arr[i] = arr[i]*right;
            right = right*nums[i];
        }
        return arr;
    }
}