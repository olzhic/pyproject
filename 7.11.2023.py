flowers = {}

while(True):
    goods = input("Tovar: ")
    if goods == "q":
        break
    count = int(input("Kolichestvo: "))
    flowers.setdefault(goods, 0)
    flowers[goods] += count

print(flowers)

for goods, quant in flowers.items():
    print(f"Tovary:  {goods} -- {quant}")