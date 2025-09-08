
# find largest and second largest from given list of numbers.
ip = [1, 2, 3, 6, 7]

if ip[0] > ip[1]:
    largest, second_largest = ip[0], ip[1]
else:
    largest, second_largest = ip[1], ip[0]

for x in ip[2:]:
    if x > largest:
        second_largest = largest
        largest = x
    elif second_largest < x < largest:
        second_largest = x

print("First (Largest):", largest)
print("Second (Second Largest):", second_largest if largest != second_largest else "No second largest")


print()
# ip=['sravani','sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
# op=[(('sravani','female'),('sravan','male'),('kumar','male'))

ip = ['Sravani','Sravan','kumar','kumari','lalitha','lalith','arjun','lakshmi','nandini']
op = tuple((name.lower(), "Female" if name.lower().endswith(("i","a")) else "Male")for name in ip)
print(op)
