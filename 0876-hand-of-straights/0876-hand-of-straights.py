class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        
        if len(hand)%groupSize!=0:
            return False

        count ={}
        for n in hand:
            count[n] = 1+count.get(n,0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            print(first)
            for i in range(first,first+groupSize):
                if i not in count:
                    return False
                count[i] -=1
                if count[i] ==0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True