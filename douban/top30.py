import urllib, time, json

time_start = time.time()
data = []
for i in range(1):
    print 'request movie:', i
    id = 1764796 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    d = urllib.urlopen(url).read()
    data.append(d)
    print i, time.time() - time_start
data1 = json.loads(data[0])
print data1
print 'data:', len(data1)
for i in data1:
    print i, data1[i]