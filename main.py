import random
import time
import copy

# important note is that only 3rd gen doesn't affect the original input array

def main():
    
    
    def move_zeros(array):
        for e in array:
            if e == 0:
                array.remove(e)
                array.append(0)
        return array

    
    def move_zeros2(array):
        to_remove = []
        for e in array:
            if e == 0:
                to_remove.append(e)
        for e in to_remove:
            array.remove(e)
            array.append(0)
        return array

    
    def move_zeros3(array):
        temp = []
        zero = 0
        for e in array:
            if e != 0:
                temp.append(e)
            else:
                zero += 1
        return temp + [0] * zero
        
            
    n = 300000
    
    arr = [random.randint(0,9) for _ in range(n)]
    arr2 = copy.deepcopy(arr)
    arr3 = copy.deepcopy(arr)
    
    
    print("arrays are even:", arr == arr2 == arr3)
    
    start = time.time()
    x = move_zeros(arr)
    stop = time.time()
    print("Gen 1: ", t1 := round(stop-start), "s", sep="")
    
    
    start = time.time()
    y = move_zeros2(arr2)
    stop = time.time()
    print("Gen 2: ", t2 := round(stop-start), "s ", "(",  round(t1/t2, 2), " times faster)", sep="")
    

    start = time.time()
    z = move_zeros3(arr3)
    stop = time.time()
    print("Gen 3: ", t3 := round(stop-start, 4), "s ", "(",  round(t2/t3), " times faster)", sep="")
    
    print("arrays are even:", x == y == z)
    
    
if __name__ == "__main__":
    main()
    
    
# Out:
# arrays are even: True
# Gen 1: 113s
# Gen 2: 47s (2.4 times faster)
# Gen 3: 0.0118s (3983 times faster)
# arrays are even: True
