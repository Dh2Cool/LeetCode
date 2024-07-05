/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int arr[] = new int[2];
        ArrayList<Integer> pos = new ArrayList();
        if(head.next.next == null){
            arr[0] = -1;
            arr[1] = -1;
            return arr;
        }
        int i = 1;
        ListNode prev = head;
        ListNode curr = head.next;
        ListNode nex = curr.next;
        while(nex != null){
            if((curr.val < prev.val && curr.val < nex.val) || (curr.val > prev.val && curr.val > nex.val)){
                pos.add(i);
            }
            i++;
            prev = prev.next;
            curr = curr.next;
            nex = nex.next;
        }
        if(pos.size() < 2){
            arr[0] = -1;
            arr[1] = -1;
            return arr;
        }
        int min = 10000000;
        int max = pos.get(pos.size() - 1) - pos.get(0);
        for(int j = 1; j < pos.size(); j++){
            if(pos.get(j) - pos.get(j-1) < min)
                min = pos.get(j) - pos.get(j - 1);
        }
        arr[0] = min;
        arr[1] = max;
        return arr;
    }
}