def quicksort(m):
    """Best = Average = O(n log(n)), Worst = O(n^2)"""
    #base case: empty list
    if not m:
        return []
    
    #choose the pivot as first element of the list
    pivot = m[0]
    
    #grab everything < pivot, starting at element after pivot
    less = [x for x in m[1:] if x < pivot]
    
    #grab everything >= pivot, starting at element after pivot
    more = [x for x in m[1:] if x >= pivot]
    
    #recursively sort less and more
    Sless = quicksort(less)
    Smore = quicksort(more)
    
    #build the full list again
    return Sless + [pivot] + Smore

def selection_sort(m):
    """Best = Worst = Average = O(n^2)"""
    for i in range(0, len(m)):
        mnIndex = i
        #find the min
        for j in range(i+1,len(m)):
            if m[j] < m[mnIndex]:
                mnIndex = j
        
        #swap
        m[i],m[mnIndex] = m[mnIndex], m[i]
        
    return m

def merge_sort(m):
    """Best = Worst = Average = O(n log(n))"""
    #base case, list of 1 element or empty
    if(len(m) <= 1):
        return m
    
    #middle is floor of len(m)/2
    middle = len(m)//2
    
    #split list in half
    left = m[:middle]
    right = m[middle:]
    
    #recursively sort left and right
    Sleft = merge_sort(left)
    Sright = merge_sort(right)
    
    return _merge(Sleft, Sright)

def _merge(a, b):
    """Merge two sorted lists into one sorted list"""
    c = []
    
    #dequeue the smaller element of a and b
    #then enqueue that element to c
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    
    #append the rest of the nonempty list to c        
    if(len(a) == 0):
        c += b
    else:
        c += a
    
    return c

def bubble_sort(m):
    """Best = O(n), Worst = Average = O(n^2)"""
    for i in range(len(m)-1, -1, -1):
        for j in range(i):
            if m[j] > m[j+1]:
                m[j], m[j+1] = m[j+1], m[j]
                
    return m

def insertion_sort(m):
    """Best = O(n), Worst = Average = O(n^2)"""
    #key starts at 1
    #if we don't need to swap, increment the key
    for key in range(1, len(m)):
        #swap and decrement the key
        while 0 < key and m[key] < m[key-1]:
            m[key], m[key-1] = m[key-1], m[key]
            key -= 1
            
    return m