
import time
sortedList = [1,2,4,25, 32, 36, 39, 76, 83, 104, 105]
def binary_search(l,value):
    low = 0
    high = len(l)-1
    print (f"looking for {value} in the list.")
    time.sleep(2)
    while low <= high:
        mid = (low+high)//2
        if l[mid] > value:
            print (f"middle number is {l[mid]}")
            time.sleep(2)
            high = mid-1
            print("lower!")
            print (l[low:high+1])
            time.sleep(2)
                    
        elif l[mid]< value:
            print (f"middle number is {l[mid]}")
            time.sleep(2)
            low = mid+1
            print ("higher!")
            print (l[low:high+1])
            time.sleep(2)
                        
        else:
            return (f"{value} was found at location {mid}")
    return (f"{value} is not here")

print (binary_search(sortedList,9))
 