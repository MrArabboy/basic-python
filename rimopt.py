class RimRaqam :
    def __init__(self):
        self.number = int(input('Enter a number less than 5000 : '))
    
    def change(self):
        a1 = {0:'',1:'I',2:"II",3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
        a10 = {0:'',1:'X',2:"XX",3:'XXX',4:'XL',5:'L',6:'LX',7:'LXX',8:'LXXX',9:'XC'}
        a100 = {0:'',1:'C',2:"CC",3:'CCC',4:'CD',5:'D',6:'DC',7:'DCC',8:'DCCC',9:'CM'}
        a1000 = {1000:'M'}

        b = ''

        x1 = self.number // 1000    #1000 lar x1=4
        x2 = (self.number - x1 * 1000) // 100   #100 lar x2=8
        x3 = (self.number - int(str(self.number)[:2]) * 100) // 10  #10 lar x3=5 
        x4 = int(str(self.number)[-1])    #1 lar x4 = 7
        if self.number < 5000:
            if len(str(self.number)) == 4:
                b += a1000[1000] * x1  
                b += a100[x2]
                b += a10[x3]
                b += a1[x4]

            elif len(str(self.number)) == 3:
                x100 = int(str(self.number[0]))   
                x10 = int(str(self.number)[1])  #10 lar  
                b += a100[x100]
                b += a10[x10]
                b += a1[x4]

            elif len(str(self.number)) == 2:
                x10 = self.number//10
                b += a10[x10]  
                b += a1[x4]
            elif len(str(self.number)) == 1:
                b += a1[x4]
        else:
            b += 'Number must not be greater than 4999'

        return b
       
a = RimRaqam()
print(a.change())