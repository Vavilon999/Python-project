class Polynomial:

    def __init__(self,*c):

        if len(c) == 1 and isinstance(c[0], list):
            self.c = c[0].copy()

        elif len(c) == 1 and isinstance(c[0], dict):
            data = c[0]

            if not data:
                self.c = [0]
            else:
                maxd = max(data.keys())
                self.c = [0] * (maxd + 1)
            
            for d, ct in data.items():
                self.c[d] = ct

        elif len(c) == 1 and isinstance(c[0], Polynomial):
            self.c = c[0].c.copy()
        else: 
            self.c = list(c)
        if len(self.c) == 0:
            self.c = [0]

        while len(self.c) > 1 and self.c[-1] == 0:
            self.c.pop()

    def __repr__(self):
        return f"Polynomial {self.c}"

    def __str__(self):

        p = []
        
        for d in range(len(self.c) - 1, -1, -1):
            ct = self.c[d]
            if ct == 0:
                continue
            abs_ct = abs(ct)
            if d == 0:
                t = str(abs_ct)
            elif d == 1:
                if abs_ct == 1:
                    t = "x"
                else:
                    t = f"{abs_ct}x"
            else: 
                if abs_ct == 1:
                    t = f"x^{d}"
                else:
                    t = f"{abs_ct}x^{d}"
            if len(p) == 0:
                if ct < 0:
                    p.append("-" + t) 
                else:
                    p.append(t)
            else:
                if ct < 0:
                    p.append(" - " + t)
                else:
                    p.append(" + " + t)
        if len(p) == 0:
            return "0"
        return "".join(p)

    def __eq__(self,o):
        if isinstance(o, (int, float)):
            o = Polynomial(o)
        if not isinstance(o, Polynomial):
            return NotImplemented
        return self.c == o.c

    def __add__(self, o):
        if isinstance(o, (int, float)):
            o = Polynomial(o)

        if not isinstance(o, Polynomial):
            return NotImplemented

        result = []

        for d in range(max(len(self.c), len(o.c))):
            a = self.c[d] if d < len(self.c) else 0
            b = o.c[d] if d < len(o.c) else 0
            result.append(a + b)

        return Polynomial(result)
    def __radd__(self,o):
        return self + o

    def __neg__(self):
        return Polynomial([-ct for ct in self.c])

    def __sub__(self, o):
        return self + (-Polynomial(o))

    def __rsub__(self, o):
        return Polynomial(o) - self

    def __call__(self,x):
        r = 0
        for i, ct in enumerate(self.c):
            r += ct * x ** i
        return r
    
    def degree(self):
        return len(self.c) - 1

    def der(self, d = 1):
        c = self.c.copy()
        if d < 0:
            return False 
        o = 0
        while d > o:

            if len(c) == 1:
                return Polynomial(0)
            
            nc = []

            for i in range(1,len(c)):
                nc.append(c[i] * i)
            c = nc 
            o += 1
        return Polynomial(c)

    def __mul__(self,o):
        if isinstance(o, (int, float)):
            return Polynomial([t * o for t in self.c])
        if not isinstance(o, Polynomial):
            return NotImplemented
        result = [0] * (len(self.c) + len(o.c) - 1)
        for i, a in enumerate(self.c):
            for j, b in enumerate(o.c):
                result[i + j] += a * b
        return Polynomial(result)
    
    def __rmul__(self,o):
        return self * o
    
    def __iter__(self):
        self.i = 0
        return self
    
    def __next__(self):
        if self.i < len(self.c):
            result = (self.i,self.c[self.i])
            self.i += 1
            return result 
        else:
            return 0
