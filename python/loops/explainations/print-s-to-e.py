# start to end by user
start = int(input("enter start number: "))
end = int(input("enter end number: "))

store_start = start
while store_start < end:
    print(store_start, end=" ")
    store_start += 1
