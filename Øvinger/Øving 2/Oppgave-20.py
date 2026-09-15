def sort(stack1, stack2, stack3):
    while not stack1.empty():
        min = None
        current = None

        while not stack1.empty():
            # Pusher første tall til stack 3, lagrer dette som minst
            if min == None:
                min = stack1.pop()
                stack3.push(min)
                continue

            current = stack1.pop()

            if current < min: 
                min = current

            stack3.push(current)

        min_moved = False
        current = None

        while not stack3.empty():
            val = stack3.pop()

            if val == min and not min_moved: 
                stack2.push(val)
                min_moved = True
            else: 
                stack1.push(val)

    while not stack2.empty():
        stack1.push(stack2.pop())
