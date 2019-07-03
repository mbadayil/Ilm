def isNumber(s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            float(s) + 10
            return True
        except:
            return False



print(isNumber(10))
