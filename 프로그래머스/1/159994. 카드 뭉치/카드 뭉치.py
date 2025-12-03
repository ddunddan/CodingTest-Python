def solution(cards1, cards2, goal):
    
    while len(goal) > 0:
        matched = False
        
        if len(cards1) > 0:
            if cards1[0] == goal[0]:
                cards1.pop(0)
                goal.pop(0)
                matched = True
                
        if len(cards2) > 0:
            if cards2[0] == goal[0]:
                cards2.pop(0)
                goal.pop(0)
                matched = True
                
        if matched == False:
            return "No"
            
    
    return "Yes"
 