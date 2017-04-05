largest = None
smallest = None
while True:
    num = raw_input("Enter a number or type done: ")
    try:
        if num == "done":
            break
        num = int(num)
    except:
        print "Invalid input"
        continue
    if smallest is None or largest is None:
        smallest = num
        largest = num
    elif num < smallest:
        smallest = num
    elif num > largest:
        largest = num

print "Maximum is", largest
print "Minimum is", smallest
