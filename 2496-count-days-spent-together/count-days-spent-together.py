class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_of_year(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            # Sum up days of previous months + current day
            return sum(days_in_months[:month - 1]) + day
        
        # Convert all 4 dates into day-of-year integers
        alice_arrive = date_to_day_of_year(arriveAlice)
        alice_leave = date_to_day_of_year(leaveAlice)
        bob_arrive = date_to_day_of_year(arriveBob)
        bob_leave = date_to_day_of_year(leaveBob)
        
        # Find the intersection of the two date ranges
        overlap_start = max(alice_arrive, bob_arrive)
        overlap_end = min(alice_leave, bob_leave)
        
        # Calculate total overlapping days
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        
        return 0