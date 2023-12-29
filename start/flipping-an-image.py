class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        for img in image:
            l = 0
            r = len(img)-1
            
            while l<=r:
                if img[l] == img[r]:
                    if img[l]==0:
                        img[l] =1
                        img[r] =1
                    else:
                        img[l] =0
                        img[r] =0
                        
                l+=1
                r-=1
        return image
        