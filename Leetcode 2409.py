class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day_number(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))          
            return sum(days_in_months[:month - 1]) + day        
        a_arrive = date_to_day_number(arriveAlice)
        a_leave = date_to_day_number(leaveAlice)
        b_arrive = date_to_day_number(arriveBob)
        b_leave = date_to_day_number(leaveBob)       
        overlap_start = max(a_arrive, b_arrive)
        overlap_end = min(a_leave, b_leave)        
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1        
        return 0
