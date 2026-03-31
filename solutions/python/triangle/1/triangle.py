def equilateral(sides):
    a,b,c = sides
    if ((a + b > c) and (b + c > a) and (a + c > b) and (a > 0 and b > 0 and c > 0) ):    
        if a==b==c:
            return True
        else:
            return False     
    else:
            return False
    


def isosceles(sides):
     
    a,b,c = sides
    if ((a + b > c) and (b + c > a) and (a + c > b) and (a > 0 and b > 0 and c > 0)):
        
        if ((a==b and a!=c) or (a==c and a!=b) or (b==c and  c!=a) or (a==b==c)):
            return True
        else:
            return False
    else:
            return False
        
    


def scalene(sides):
    a,b,c = sides
    if ((a + b > c) and (b + c > a) and (a + c > b) and (a > 0 and b > 0 and c > 0) ): 
        if (a!=b and b!=c and c!=a):
            return True
        else:
            return False   
    else:
            return False
    
