/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode* slow = head;
        ListNode* fast = head;
        
        int flag = false;
        if(head == NULL or head->next == NULL) return NULL;
        
        while(fast and fast->next){
            slow = slow->next;
            fast = fast->next->next;
            
            if(slow == fast){
                flag = true;
                break;
            }
        }
        
        if(flag == false) return NULL;
        ListNode* start = head;
        while(start != slow){
            start = start->next;
            slow = slow->next;
        }
        return start;
    }
};