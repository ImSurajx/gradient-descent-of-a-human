# start to end by user
start = int(input("enter start number: "))
end = int(input("enter end number: "))

store_start = start
while store_start <= end:
    if store_start % 2 == 0:
        print(store_start)
    store_start += 1
