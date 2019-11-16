nums=(55,44,33,22)
print(nums[:2])

print(max(min(nums[:2]),abs(-42)))


score1={1:3,2:4,3:6,4:1}
m=max(score1,key=score1.get)
print(m)