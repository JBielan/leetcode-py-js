class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_order = []
        while l1:
            l1_order.append(l1.val)
            l1 = l1.next

        l2_order = []
        while l2:
            l2_order.append(l2.val)
            l2 = l2.next

        l1_num = int(''.join(map(str, l1_order[::-1])))
        l2_num = int(''.join(map(str, l2_order[::-1])))

        res_num = l1_num + l2_num

        res_list = [int(x) for x in str(res_num)][::-1]

        res = ListNode(res_list[0])
        res2 = res

        for i in range(1, len(res_list)):
            res2.next = ListNode(res_list[i])
            res2 = res2.next

        return res