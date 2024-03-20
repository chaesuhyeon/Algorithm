public class Merge_Two_Sorted_Lists {

  public static class ListNode {
      int val;
      ListNode next;
      ListNode() {}
      ListNode(int val) { this.val = val; }
      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
  }

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode listNode = new ListNode();
        

        while (list1 != null && list2 != null) {
            int val1 = list1.val;
            int val2 = list2.val;

            if (val1 > val2) {
                listNode = new ListNode(val2, new ListNode(val1));
            } else {
                listNode = new ListNode(val1, new ListNode(val2));
            }

            list1 = list1.next;
            list2 = list2.next;
        }

        return listNode;
    }

    public static void main(String[] args) {
        System.out.println(
                mergeTwoLists(
                        new ListNode(1, new ListNode(2, new ListNode(4)))
                        , new ListNode(1, new ListNode(3, new ListNode(4)))
                ));
//        System.out.println(
//                mergeTwoLists(new ListNode(), new ListNode())
//                        );

    }
}

