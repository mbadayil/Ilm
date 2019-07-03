matrix=[
  [ 1, 2, 3, 4,5 ],
  [ 6, 7, 8, 9,10],
  [ 11, 12, 13,14,15],
  [ 16, 17, 18,19,20]
]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        res = []
        if len(matrix) == 0:
            return res

        colBegin = 0
        colEnd = len(matrix[0])-1
        rowBegin = 0
        rowEnd = len(matrix)-1

        while colBegin <= colEnd and rowBegin <= rowEnd:
            #left to right
            for i in range(colBegin,colEnd+1):
                res.append(matrix[rowBegin][i])

            rowBegin+=1
            for i in range(rowBegin,rowEnd+1):
                res.append(matrix[i][colEnd])

            colEnd-=1
            if rowBegin <= rowEnd:
                for i in range(colEnd,colBegin-1,-1):
                    res.append(matrix[rowEnd][i])

            rowEnd-=1
            if colBegin <= colEnd:
                for i in range(rowEnd,rowBegin-1,-1):
                    res.append(matrix[i][colBegin])

            colBegin+=1

        return res
