/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head){
    if(head == NULL)
        return NULL;
    struct ListNode * odd = head, *even = head->next, *evenh = head->next;
    
    while(even && even->next){
        odd->next = odd->next->next;
        even->next = even->next->next;
        odd=odd->next;
        even = even->next;
    }
    odd->next = evenh;
    return head;
}