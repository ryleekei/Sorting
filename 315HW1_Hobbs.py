#ask for file, open it, and store into a list
input = input("Enter file name: \n")
file = open(input, "r")
text = file.readlines()

text.pop(0)
statsList = []
for i in range(len(text)):
    text[i] = text[i].rstrip("\n")
    text[i] = text[i].split(",")
    text[i][1] = int(text[i][1])
    statsList.append(text[i][1])
print("Input File:")
print(statsList)
print("\n")

  
def insertion_sort(array, count):
    for index in range(1, len(array)):
        i = index - 1
        value = array[index]  
        while i >= 0:          
            if value < array[i]: #value = array[i+1]
                count += 1
                array[i+1] = array[i] #move on to the next value in the list to compare
                array[i] = value  #shift value to i
                i -= 1 
                
            else:
                count += 1
                break  
        count += 1   
    return count


def QuickSort(l, r, array, count):
    if len(array) == 1: #cannot partition array because it only contains one value
       return 0
    
    if l < r :
            val, count = partition(l, r, array, count)
            count += QuickSort(l, val - 1, array, count)
            count += QuickSort(val, r, array, count) 
    return count

def partition(l, r, array, count):
    pivot, val = array[r], l 
    for i in range(l, r):
        count += 1
        if array[i] <= pivot:
            array[i], array[val] = array[val], array[i] #switch order
            val += 1
    array[val], array[r] = array[r], array[val]
    return val, count


#Merge Sort
def MergeSort(array, count):
    if len(array) > 1:
        m = len(array)//2
        l = array[:m]
        r = array[m:]
        
        count += MergeSort(l, count) + MergeSort(r, count)

        #Keep dividing each part in half
        MergeSort(r, count)
        MergeSort(l, count)
        
        i = 0   #main array iterator
        j = 0   #right iterator
        k = 0   #left iterator
        
        while k < len(l) and j < len(r):
            count += 1      
            if l[k] <= r[j]:
                count += 1
                array[i] = l[k]
                k += 1         
            else:
                array[i] = r[j]
                j += 1
            
            #next spot in array
            i += 1
        
        while k < len(l):
            array[i] = l[k]
            k += 1
            i += 1
        
        
        while j < len(r):
            array[i] = r[j]
            j += 1
            i += 1
    
    return count

Isort = statsList
insertion_sort(Isort, 0)
Icount = insertion_sort(Isort, 0)

print("Insertion Sort:")
print(Isort)

print("\n")
print("Number of Comparisons:")
print(Icount)  

Qsort = statsList
length = len(Qsort)
Qcount = QuickSort(0, length - 1, Qsort, 0)
QuickSort(0, length - 1, Qsort, 0)

print("\n")
print("Quick Sort:\n")
print(Qsort)
print("\n")

print("Number of Comparisons:")
print(Qcount)
print("\n")

Msort = statsList
MergeSort(Msort,0)


print("Merge Sort:\n")
print(Msort)
print("\n")
print("Number of Comparisons: ")
print(MergeSort(Msort, 0))