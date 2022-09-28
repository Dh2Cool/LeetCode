/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    int count = 0;
    struct ListNode* ptr = head;
    while(ptr != NULL){
        count++;
        ptr = ptr->next;
    }
    if(count == 0 || count == 1)
        return NULL;
    int dn = count - n;
    if(count == n){
        head=head->next;
        return head;
    }
    ptr = head;
    while(dn > 1) {
        ptr = ptr->next;
        dn--;
    }
    struct ListNode* temp = ptr->next; //[ptr]->[temp]->[...]
    ptr->next = ptr->next->next;
    free(temp);
    return head;
}