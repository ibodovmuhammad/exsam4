from datetime import datetime, timedelta
a = input()
a= datetime.strptime(a, '%Y-%m-%d')
b = a - timedelta(days=5)
print(b)