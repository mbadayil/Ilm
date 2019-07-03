class Solution:

    def add(self, number):
        list1.append(number)

    def find(self, fnum):
        i,j=0,len(self.number)
        while j>0:
            if fnum in self.number:
                return True
            elif self.number[i]+self.number[j]==fnum:
                return True
            elif self.number[i]+self.number[j]>fnum:
                j-=1
            else:
                i+=1
