class Medals:
    def __init__(self, name, **kwargs):
        self.name = name
        self.medal = kwargs
    def add(self, type):
        for i in self.medal:
            if i == type:
                self.medal[i] += 1
                print 'The %s number of medals has increased to %d'%(i, self.medal[i])
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
# G for Golden, S for Silver, C for Copper.
c = Medals('China', G=26, S=18, C=26)
c.info()
c.total()
c.add('G')

usa = Medals('USA', G=46, S=37, C=38)
uk = Medals('UK', G=27, S=23, C=17)
rus = Medals('RUS', G=19, S=18, C=19)

def getObj(x):
    obj = {}
    obj['name'] = x.name
    dictMerged = dict(obj, **x.medal)
    return dictMerged

obj1 = getObj(c)
obj2 = getObj(usa)
obj3 = getObj(uk)
obj4 = getObj(rus)
# print obj1
# print obj2
# print obj3
# print obj4

medalsList = []
medalsList.append(obj1);
medalsList.append(obj2);
medalsList.append(obj3);
medalsList.append(obj4);
print medalsList

for i in range(len(medalsList)):
    for k in range(len(medalsList)):
        if k > i:
            if medalsList[i]['G'] < medalsList[k]['G']:
                obj = medalsList[i].copy()
                medalsList[i] = medalsList[k].copy()
                medalsList[k] = obj.copy()
print medalsList