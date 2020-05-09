# %연산자를 이용한 풀이 

y, m, d = input().split(".")
print('%04d' % int(y), 
	  '%02d' % int(m), 
	  '%02d' % int(d), 
	  sep = ".")
