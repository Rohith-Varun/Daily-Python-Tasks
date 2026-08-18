class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        dire = deque()
        radiant = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        while len(dire) > 0 and len(radiant) > 0:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r+len(senate))
            else:
                dire.append(d+len(senate))
        return 'Radiant' if len(radiant)>0 else 'Dire'

