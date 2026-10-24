class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        all_days = [0,31,59,90,120,151,181,212,243,273,304,334,365]
        # [Jan, Feb, Mar, Apr, May, June, July, Aug, Sep, Oct, Nov, Dec]
        if int(arriveBob[:2])>int(leaveAlice[:2]):
            return 0
        else:
            arrive_Alice = all_days[int(arriveAlice[:2])-1]+int(arriveAlice[3:])
            leave_Alice = all_days[int(leaveAlice[:2])-1]+int(leaveAlice[3:])
            
            arrive_Bob = all_days[int(arriveBob[:2])-1]+int(arriveBob[3:])
            leave_Bob = all_days[int(leaveBob[:2])-1]+int(leaveBob[3:])

            alice_day = [x for x in range(arrive_Alice,leave_Alice+1)]
            bob_day = [x for x in range(arrive_Bob,leave_Bob+1)]
            st = set(alice_day).intersection(set(bob_day))
            return (len(st))