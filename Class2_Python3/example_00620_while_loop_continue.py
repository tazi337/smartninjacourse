counter = 0
while True:
    counter += 1
    if counter == 10:
        break
    elif counter % 2 == 0:
        continue
    else:
        print(counter)
