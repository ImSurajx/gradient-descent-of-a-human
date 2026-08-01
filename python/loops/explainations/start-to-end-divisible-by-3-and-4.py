# start to end by user
start = int(input("enter start number: "))
end = int(input("enter end number: "))

store_start = start
while store_start <= end:
    if store_start % 3 == 0 and store_start % 4 == 0 :
        print(store_start)
    store_start += 1
