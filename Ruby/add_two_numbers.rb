def add_two_numbers(l1, l2)
    node1, node2, node3, list3, carry = l1, l2, nil, nil, 0
    
    while node1 || node2
        node1 ? (value1 = node1.val; node1 = node1.next) : (value1 = 0)
        node2 ? (value2 = node2.val; node2 = node2.next) : (value2 = 0)
        
        sum = value1 + value2 + carry
        carry, digit = sum.divmod(10)
        
        n = ListNode.new(digit)
        node3 ? (node3.next = n; node3 = n) : (node3 = n; list3 = node3) 
    end
     node3.next = ListNode.new(carry) if carry.nonzero?
    list3
    
end