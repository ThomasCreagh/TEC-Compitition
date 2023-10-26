import os,psutil
import random
process = psutil.Process(os.getpid())

#ram check before execution
mem = process.memory_info()[0] / float(2 ** 20)
print(f'ram used before :{mem:.2f} MB')

def pigeonhole_sort(a):
    # size of range of values in the list 
    # (ie, number of pigeonholes we need)
    my_min = min(a)
    my_max = max(a)
    size = my_max - my_min + 1
  
    # our list of pigeonholes
    holes = [0] * size
  
    # Populate the pigeonholes.
    for x in a:
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
  
    # Put the elements back into the array in order.
    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            a[i] = count + my_min
            i += 1
              
arr = list(range(999999))
random.shuffle(arr) 
pigeonhole_sort(arr)
          
mem = process.memory_info()[0] / float(2 ** 20)
print(f'ram used after :{mem:.2f} MB')