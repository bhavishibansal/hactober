import math;
set1 = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
set2=[2,4,6,8,10]

def intersection(set1,set2):
    set3 = [value for value in set1 if value in set2]
    return set3
print("set1 intersection set2 : ", intersection(set1,set2))

def printPowerSet(set,size):
    sizeOfPower = (int) (math.pow(2, size));
    counter = 0;
    j = 0;
    for counter in range(0, sizeOfPower):
        for j in range(0, size):
            if((counter & (1 << j)) > 0):
                print(set2[j], end = ", ");
        print("");
printPowerSet(set2, len(set2));
