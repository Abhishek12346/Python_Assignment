class Numbers:

    def __init__(self):

        self.Value=int(input("Enter the Value=>"))
        print("-"*45)

    def CHkPrime(self):

        if self.Value < 1:
            return False
        
        for i in range(2,self.Value):
            if self.Value % i==0:
                return False
            
        return True
        print("-",*45)  

    def ChkPerfect(self):
        
        if self.Value <= 0:
            return False

        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i

        return total == self.Value
     
    
    def factors(self):
        print("-"*45)
        print("Factors are:")

        for i in range(1,self.Value + 1):
            if self.Value % i == 0:

                print(i)
               
    def sum_factors(self):
        total = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                total = total + i
        return total                   


N1=Numbers()
Result=N1.CHkPrime()
print("ChkPrime Numbers is=>",Result)

Perfect=N1.ChkPerfect()
print("Perfect Number is =>",Perfect)

Factors=N1.factors()
print("-"*45)

Sum=N1.sum_factors()
print("Sum of Factors=>",Sum)
