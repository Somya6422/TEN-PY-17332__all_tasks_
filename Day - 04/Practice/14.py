def area_circle(r):
    return 3.14 * r * r
def area_rectangle(l, w):
    return l * w
print("1.Circle 2.Rectangle")
choice = int(input("Choose: "))
if choice == 1:
    r = float(input("Radius: "))
    print(area_circle(r))
else:
    l = float(input("Length: "))
    w = float(input("Width: "))
    print(area_rectangle(l, w))
    
