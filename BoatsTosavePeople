class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        r=len(people)-1
        l=0
        count=0
      
        while l<=r:
            if people[l]+people[r]<=limit:
                count+=1
                l+=1
                r-=1
            else:
                count+=1
                r-=1
            
        return count
