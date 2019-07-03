# Definition for a  binary tree node
def romanNum(num):
    inputData=[1000,900,500,400,100,90,50,40,10,5,1]
    inputDict={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',5:'V',1:'I'}

    output=""

    for k in inputData:
        if num>=k:
            output+=num//k * inputDict[k]
            num=num%k
        elif num==0:
            break
    return output

print(romanNum(101))
