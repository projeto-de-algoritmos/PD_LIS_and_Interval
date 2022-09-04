import bisect
from email import message

class WeightedIntervalScheduling(object):
    def __init__(self, I):
        self.I = sorted(I, key=lambda tup: tup[2])  # (key = lambda tup : tup[1])
        self.OPT = []
        self.solution = []

    def previous_intervals(self):
    
        start = [task[1] for task in self.I]
        finish = [task[2] for task in self.I]
        p = []

        for i in range(len(self.I)):
            idx = bisect.bisect(finish, start[i]) - 1
            p.append(idx)
        
        print(p)

        return p

    def find_solution(self, j):
    
        if j == -1:
            return

        else:
            if (self.I[j][3] + self.compute_opt(self.p[j])) > self.compute_opt(j - 1):
                self.solution.append(self.I[j])
                self.find_solution(self.p[j])

            else:
                self.find_solution(j - 1)

    def compute_opt(self, j):
        if j == -1:
            return 0

        elif (0 <= j) and (j < len(self.OPT)):
            return self.OPT[j]

        else:
            return max(
                self.I[j][3] + self.compute_opt(self.p[j]), self.compute_opt(j - 1)
            )

    def weighted_interval(self):
        if len(self.I) == 0:
            return 0, self.solution

        self.p = self.previous_intervals()

        for j in range(len(self.I)):
            opt_j = self.compute_opt(j)
            self.OPT.append(opt_j)

        self.find_solution(len(self.I) - 1)

        return self.OPT[-1], self.solution[::-1]

def replaceTime(I):
    J = []
    for itens in I:
        itens0 = itens[0]
        itens1 = str(itens[1])
        itens2 = str(itens[2])
        itens1 = itens1.replace("."," ")
        itens1 = itens1[6:8]+'/'+itens1[4:6]+'/'+itens1[0:4]
        itens2 = itens2.replace("."," ")
        itens2 = itens2[6:8]+'/'+itens2[4:6]+'/'+itens2[0:4]

        itens3 = itens[3]
        J.append((itens0,itens1,itens2,itens3))

    print
    print(J)
    return J 

def resolve(I):
    print('entrouresolve')
    J = []
    for itens in I:
        print(itens[1])
        itens0 =  itens[0]
        itens1 = float(itens[1])
        print(itens[1])
        itens2 = float(itens[2])
        itens3 = float(itens[3])
        J.append((itens0,itens1,itens2,itens3))
        
    return J   

      
def removeQuotation(list):
    J = []
    for itens in list:
        itens = itens.replace("-","")
        J.append(itens)

    print(J)
    return J

    
    


