class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        map_ ={}
        
        for i in range(len(list1)):
            if not list1[i] in map_:
                map_[list1[i]] = i
                
        the_mins = []
        the_min = len(list1)+len(list2)
        for i in range(len(list2)):
            if list2[i] in map_:
                if i +map_[list2[i]] < the_min:
                    the_mins=[]
                    the_mins.append(list2[i])
                    the_min = i +map_[list2[i]]
                elif i +map_[list2[i]] == the_min:
                    the_mins.append(list2[i])
                    
        return the_mins
            
        