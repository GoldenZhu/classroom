class Medals:
    def __init__(self, name, **kwargs):
        self.name = name
        self.medal = kwargs
    def add(self, type):
        for i in self.medal:
            if i == type:
                self.medal[i] += 1
                print 'The number of medals has increased %s'%i
                return
    def info(self):
        str = self.name + ': '
        for k in self.medal:
            str += '%s:%d '%(k, self.medal[k])
        print str
        return str
    def total(self):
        sum = 0
        for j in self.medal:
            sum += self.medal[j]
        print 'the total amount of %s medals is %d'%(self.name, sum)
        return sum

c = Medals('China', G=26, S=18, C=26)
c.info()
c.total()

usa = Medals('USA', G=46, S=37, C=38)
usa.info()
usa.total()

uk = Medals('UK', G=27, S=23, C=17)
uk.info()
uk.total()

rus = Medals('RUS', G=19, S=18, C=19)
rus.info()
rus.total()

def getObj(x):
    obj = {}
    obj[x.name] = x.medal
    return obj

obj1 = getObj(c)
obj2 = getObj(usa)
obj3 = getObj(uk)
obj4 = getObj(rus)
print obj1
print obj2
print obj3
print obj4

medalsList = []
medalsList.append(obj1);
medalsList.append(obj2);
medalsList.append(obj3);
medalsList.append(obj4);
print medalsList

# for i in medalsList:
#     for k in medalsList.length - i: