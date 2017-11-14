import urllib2

url1 = 'http://m.weather.com.cn/data3/city.xml'
content1 = urllib2.urlopen(url1).read()
provinces = content1.split(',')

# print content1
# print provinces

url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
   p_code = p.split('|')[0]
   print p_code
   url2 = url % p_code
   content2 = urllib2.urlopen(url2).read()
   print content2
   cities = content2.split(',')
