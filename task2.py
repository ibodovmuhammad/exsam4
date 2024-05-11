from datetime import datetime, timedelta
a = input()
a= datetime.strptime(a, '%Y-%m-%d')
b = a - timedelta(days=2)
c = a + timedelta(days=2)
print(b)
print(a)
print(c)


















