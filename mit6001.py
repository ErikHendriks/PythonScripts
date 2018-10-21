def sqrtBisec(x):
    '''
    Find square root of x with a
    divide and conquer approach.
    '''
    epsilon = 0.00000000001
    guesses = 0
    low = 0.0
    high = x
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        guesses += 1
        print(ans)
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print('guesses = ' + str(guesses))
    print(str(ans) + ' is close tot square root of ' + str(x))

def sqrtNewRaph(x):
    '''
    Find square root of x with the
    Newton/Raphson approach.
    '''
    epsilon = 0.1
    guess = x/2.0
    guesses = 0
    while abs(guess*guess - x) >= epsilon:
        guesses += 1
        guess = guess - (((guess**2) - x)/(2*guess))
    print('guesses = ' + str(guesses))
    print('square root of ' + str(x) + ' is about ' + str(guess))
          
def fib_iter(n):
    '''
    Assumes n is  int >= 0.
    Calculate fibonacci iterative in O(n) time.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0
        fib_ii = 1
        for i in range(n-1):
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii

def fib_recur(n):
    '''
    Assumes n is  int >= 0.
    Calculate fibonacci recursive in O(2n) time.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

testList1 = [1,2,3,475,82,73,192,5,8,13,21,5434]
testList2 = [13,23,33,475,82,733,1932,556,348,1333,213,543]
testList3 = ['foo', 'baz', 'quick', 'large', 'slow', 'bar', 'tiny']
def linear_search(L, e):
    '''
    Linear search on unsorted list.
    O(len(L)) for the loop * O(1)
    to test if e == L[i].
    Overall complexity is O(n) - where n is len(L).
    '''
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
        return found

def search(L, e):
    '''
    Linear search on sorted list.
    O(len(L)) for the loop * O(1)
    to test if e == L[i].
    Overall complexity is O(n) - where n is len(L).
    '''
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
    
def bisect_search1(L, e):
    '''
    O(log n) bisection search calls.
    O(n) for each bisection search call to copy list.
    -> O(n log n)
    -> O(n) for a tighter bound because length of list
    is halved each recursive call.
    '''
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1( L[:half], e)
        else:
            return bisect_search1( L[half:], e)

def bisect_search2(L, e):
    '''
    Pass list and index as parameter
    list never copies, just re-passed.
    Complexity O(log n).
    '''
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) -1)

def bubble_sort(L):
    '''
    Inner for loop is for doing the comparisons.
    Outer while loop is for doing multiple passes until
    no more swaps.
    O(n^2)(quadratic) where n is len(L)
    to do len(L)-1 comparisons and len(L)-1 passes.
    '''
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

def selection_sort1(L):
    '''
    
    '''
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1

def selection_sort2(L):
    '''

    '''
    for i in range(len(L) - 1):
        print(L)
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndex = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp

lis = ['zabc', 'kjas', 'uhags', 'anbdge', 'ckiahd', 'hskwm', 'aksjuduv']
def merge_sort(L):
    '''
    Divide list successively into halves.
    Depth-first such that conquer smallest pieces down
    one branch first before moving to larger pieces.
    At first recursion level, n/2 elements in each list
    O(n) + O(n) = O(n) where n is len(L).
    At second recursion level, n/4 elements in each list
    two merges -> O(n) where n is len(L).
    Each recursion level is O(n) where n is len(L).
    Dividing list in half with each recursive call
    O(log(n)) where n is len(L).
    Overall complexity is O(n log(n)) where n is len(L).
    '''
    if len(L) < 2:
        return L[:]
    else:
        half = len(L)//2
        left = merge_sort(L[:half])
        right = merge_sort(L[half:])
        return merge(left, right)

def merge(left, right):
    '''
    Left and right are two sublist which are sorted.
    Go through two lists, only one pass.
    Compare only smallest element in each sublist.
    O(len(left) + len(right)) copied elements.
    O(len(longer list)) comparisons.
    Linear in length of the list.

    '''
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def bisect_search2(L, e):
    '''
    Pass list and index as parameter
    list never copies, just re-passed.
    Complexity O(log n).
    '''
    def bisect_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) -1)
