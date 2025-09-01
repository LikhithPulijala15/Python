
# find largest and second largest from given list of numbers.
ip = [1,2,3,6,7]

if ip[0] < ip[1]:
    sm, smm = ip[0], ip[1]
else:
    sm, smm = ip[1], ip[0]
for x in ip[2:]:
    if x < sm:
        smm = sm
        sm = x
    elif sm < x < smm:
        smm = x
print("First:", sm)
print("Second:", smm if sm != smm else "No second smallest")

print()
# ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
# op=[(('sravani','female'),('sravan','male'),('kumar','male'))

ip = ['Sravani','Sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple((name.lower(), "Female" if name.lower().endswith(("i","a")) else "Male")for name in ip)
print(op)