/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* slow = head;
    struct ListNode* fast = head->next;
    while(1){
        
        if(fast != NULL){
            if(fast->next == NULL)
                return slow->next;
            else
                fast = fast->next->next;
        }
        else{
            return slow;
        }
        slow = slow->next;
    }
    
}