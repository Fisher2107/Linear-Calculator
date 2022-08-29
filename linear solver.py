# What this code does:
# Write a simple linear equation that only includes the '+' and '-' symbols, and the unknown varibale is x.
# This code will solve for x 

class Solve:
    def __init__(self,equation):
        self.equation = list(equation)
        
    def equationtidy(self):
        equationtidy=[]
        for i in self.equation:
            if ' ' != i:
                equationtidy.append(i)
        return equationtidy
    
    def seperate(self):
        global equationleft,equationright
        for i in range(len(self.equationtidy())):
            if '=' == self.equationtidy()[i]:
                equationleft = self.equationtidy()[:i]
                equationright = self.equationtidy()[i+1:]
                break
        return [equationleft,equationright]

    
    def symbolfinder(self):
        global symbollistleft,symbollistright
        symbols = ['+','-']
        symbollistleft , symbollistright = [] , []
        symbollist = [symbollistleft,symbollistright]
        for i,j in enumerate(self.seperate()):
            for s,t in enumerate(j):
                if t in symbols:
                    symbollist[i].append(s)
        return symbollist
    
    def identify(self):
        allist=[]
        for i,symbollists in enumerate(self.seperate()):
            smalllist=[]
            for j in range(len(symbollists)):
                if j==0:
                    minilist=[]
                    minilist.append(self.seperate()[i][j])
                elif j in self.symbolfinder()[i]:
                    if minilist[0]!= '+' and minilist[0]!='-':
                        minilist.insert(0,'+')
                    smalllist.append(minilist)
                    minilist=[]
                    minilist.append(self.seperate()[i][j])
                else:
                    minilist.append(self.seperate()[i][j])
                    
            if minilist[0]!= '+' and minilist[0]!='-':
                minilist.insert(0,'+')
            smalllist.append(minilist)
            allist.append(smalllist)
        return allist

    
    def simplify(self):
        allist = self.identify()
        
        leftintegers , rightintegers = [] , []
        leftcoefficents, rightcoefficents = [] , []
        
        for i,leftright in enumerate(allist):
            for j in leftright:
                coefficent=0
                jwithoutx = []
                #identifing whether it is a coef or int
                #also removes x from coef after idetifing since we know it has an x
                for k in j:
                    if 'x' == k:
                        coefficent=1
                    else:
                        jwithoutx.append(k)
                #accounting for the special case of just writng x which is assumed to be 1x
                if jwithoutx==['-']: jwithoutx=['-','1']
                elif jwithoutx==['+']: jwithoutx=['+','1']
                    
                if coefficent:
                    if i==0:
                        leftcoefficents.append(jwithoutx)
                    else:
                        rightcoefficents.append(jwithoutx)
                else:
                    if i==0:
                        leftintegers.append(j)
                    else:
                        rightintegers.append(j)
        
    
        def numbify(bringtoside,leaveside):
            outputlist=[]
            outputnumber=0
            for i in bringtoside:
                outputlist.append(i)
            for i in leaveside:
                reverse=[]
                for j in i:
                    if '+' == j:
                        reverse.append('-')
                    elif '-' == j:
                        reverse.append('+')
                    else:
                        reverse.append(j)
                outputlist.append(reverse)
            
            for i in range(len(outputlist)):
                outputnumber += int(''.join(outputlist[i]))
            
            return outputnumber
        
        global intright, coefleft
        intright = numbify(rightintegers,leftintegers)
        coefleft = numbify(leftcoefficents,rightcoefficents)
        
        return f'{coefleft} x = {intright}'
    
    
    def solve(self):
        return f'x = {intright/coefleft}'

        
problem = Solve(input())

#print(problem.equation)
#print(problem.equationtidy())
#print(problem.seperate())
#print(problem.symbolfinder())
print(problem.identify())
print(problem.simplify())
print(problem.solve())
