class Solution {
    public int findTheWinner(int n, int k) {
        ArrayList<Integer> cpp = new ArrayList<Integer>();
        for(int i = 1; i <= n; i++)
            cpp.add(i);
        int i = 0;
        while(cpp.size() > 1){
            i = (i + k - 1)%cpp.size();
            cpp.remove(i);
        }
        return cpp.get(0);
    }
}