class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        List<Integer> ans = new ArrayList<Integer>();
        for(int i : nums){
            if(!map.containsKey(i)){
                map.put(i, 0);
            }
            map.put(i, map.get(i) + 1);
        }
        List<Integer> freq[] = new ArrayList[nums.length + 1];
        for(int i = 0; i < freq.length; i++)
            freq[i] = new ArrayList<>();
        for(Map.Entry<Integer, Integer> entry : map.entrySet()){
            int frequency = entry.getValue();
            freq[frequency].add(entry.getKey());
        }
        int res[] = new int[k];
        int idx = 0;
        for(int i = freq.length - 1; i>=0; i--){
            for(int num : freq[i]){
                res[idx++] = num;
                if(idx == k)
                    return res;
            }
        }
        return new int[0];
    }
}