/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteMiddle(struct ListNode* head){
    double n = 1;
    struct ListNode* ptr = head;
    while(ptr->next != NULL){
        n++;
        ptr=ptr->next;
    }
    if(n == 1){
        return NULL;
    }
    int mid = n/2;
    n = 0;
    ptr=head;
    while(n < mid -1){
        ptr = ptr->next;
        n++;
    }
    ptr->next = ptr->next->next;
    return head;
}