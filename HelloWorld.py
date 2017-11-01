
print 'Hello World'

S = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
IDX =  '      0          1        2        3      4'
idx =  '     -5         -4       -3       -2     -1'
print ('S = %s'%S)

print ('[S[0], S[1], S[2]] = %s'%[S[0], S[1], S[2]])

n = 3
r = []

for i in range(n):
    r.append (S[i])

print ('r = %s'%r)

print '----------------------------------------------------'

print ('S = %s'%S)
print IDX
print idx
print 'param1:param2:1 stands for 1)from param1 to param2 2)and half close and half open'
print ('S[1:3] = %s'%S[1:3])
print ('S[-3:-1] = %s'%S[-3:-1])
print ('S[-2:5] = %s'%S[-2:5])
print ('S[0:-3] = %s'%S[0:-3])
print
print 'S[absence1:absence2:absence3]'
print 'absence1 stands for the 1st one%r, absence2 stands for the last one, absence3 stands for step 1'
print ('S[:1] = %s'%S[:1])
print ('S[-1:] = %s'%S[-1:])
print ('S[::] = %s'%S[::])
print
print 'S[::-1]'
print
print 'param1:param2:-1 still stands for 1)from param1 to param2 2)and half close and half open'
print 'step -1 stands for reversed order to access the array, i.e. from param1 to param2 should be from the later element to the former element'
print ('S[0:2:-1] = %s error'%S[0:2:-1])
print ('S[2:0:-1] = %s'%S[2:0:-1])
print ('S[-3:-1:-1] = %s error'%S[-3:-1:-1])
print ('S[-1:-3:-1] = %s'%S[-1:-3:-1])
print
print ('S = %s'%S)
print ('%s'%IDX)
print ('%s'%idx)
