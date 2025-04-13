'''
Audrey Palmer
Desmond Frimpong
Samuel Offei

edit_distance.py
'''


def bottom_up_iterative(string1, string2) :
    '''
    bottom up : solve parts to combine for complete solutions
    '''

    len1 = len(string1)
    len2 = len(string2)

    dp_table = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

    for i in range(len1 + 1) :
        dp_table[i][0] = i * 2  # deleting all characters from string1

    for j in range(len2 + 1) :
        dp_table[0][j] = j * 2  # inserting all characters into string1

    for i in range(1, len1 + 1) :
        for j in range(1, len2 + 1) :

            if string1[i - 1] == string2[j - 1] :
                dp_table[i][j] = dp_table[i - 1][j - 1]  # no cost, characters match

            else :
                replace_cost = dp_table[i - 1][j - 1] + 3
                insert_cost  = dp_table[i][j - 1] + 2
                delete_cost  = dp_table[i - 1][j] + 2

                dp_table[i][j] = min(replace_cost, insert_cost, delete_cost)

    return dp_table[len1][len2]

    

def top_down_recursive(string1, string2) :
    '''
    top down : divide and conquer the problem
    '''
    if len(string1) == 0 :
        return len(string2) * 2
    
    if len(string2) == 0 :
        return len(string1) * 2
    
    if string1[-1] == string2[-1]:

        return top_down_recursive(string1[:-1],string2[:-1])
    
    replace_cost = 3 + top_down_recursive(string1[:-1],string2[:-1])
    delete_cost = 2 + top_down_recursive(string1[:-1],string2)
    insert_cost = 2 + top_down_recursive(string1,string2[:-1])
    
    return min(replace_cost, delete_cost, insert_cost)




"""
Bender's recursive solution. Hopefully we can modify it for the 
memoized solution
"""
def editDistance(S, T):
    # Base case
    if len(S) == 0:
        return 2 * len(T)
    if len(T) == 0:
        return 2 * len(S)
    
        
    if S[-1] == T[-1]:
        return editDistance(S[:len(S) - 1], T[:len(T) - 1])
    else:
        return min(
            3 + editDistance(S[:len(S) - 1], T[:len(T) - 1]),
            2 + editDistance(S[:len(S) - 1], T[:len(T)]), 
            2 + editDistance(S[:len(S)], T[:len(T) - 1])
        )
        

if __name__ == "__main__" :

    string1 = "analysis"
    string2 = "algorithms"

    bu = bottom_up_iterative(string1, string2)  
    td =top_down_recursive(string1, string2)

    print("the correct answer is 18")
    print(bu)
    print(td)

