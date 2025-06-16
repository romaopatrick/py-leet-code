x = [5, 6, -15, 2, 4, -1, 12, -8]

max_s = x[0]
s = x[0]

for i in range(1, len(x)):
    s = s + x[i] if s + x[i] > x[i] else x[i]
    
    if s > max_s:
        max_s = s
        
print(max_s)