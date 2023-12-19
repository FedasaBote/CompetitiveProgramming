class Bitset:

    def __init__(self, size: int):
        self.bits =["0"]*size
        self.ones_count = 0
        self.size = size
        self.flipped = "0"

    def fix(self, idx: int) -> None:
        if self.bits[idx]=="0" and self.flipped =="0":
            self.bits[idx]="1"
            self.ones_count +=1
            
        elif self.bits[idx]=="1" and self.flipped == "1":
            self.bits[idx]="0"
            self.ones_count +=1

    def unfix(self, idx: int) -> None:
        if self.bits[idx]=="1"  and self.flipped =="0":
            self.bits[idx]="0"
            self.ones_count -=1
        elif self.bits[idx] =="0" and self.flipped =="1":
            self.bits[idx] ="1"
            self.ones_count -=1

    def flip(self) -> None:
        if self.flipped=="0":
            self.flipped ="1"
        else:
            self.flipped ="0"
        
        self.ones_count = self.size - self.ones_count
        

    def all(self) -> bool:
        return self.ones_count == self.size
        

    def one(self) -> bool:
        return self.ones_count > 0

    def count(self) -> int:
        return self.ones_count

    def toString(self) -> str:
        ans =[]
        if self.flipped =="1":
            ans = ["0" if i=="1" else "1" for i in self.bits]
        else:
            ans = self.bits
        return "".join(ans)
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()