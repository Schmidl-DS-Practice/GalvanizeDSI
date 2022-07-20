def pytha_trip_1000(a,b):
    for i in range(2, a):
        for j in range(2, b):
            c = (i**2 + j**2)**0.5
            if i + j + int(c) == 1000:
                return int(i*j*c), i, j, c
    return 'could not find it'

print(pytha_trip_1000(201, 376))