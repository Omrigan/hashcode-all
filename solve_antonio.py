from read_write import Problem, Solution
import random

def computescore(x,y):
    a = x[1]
    b = y[1]
    return min(len(a|b), len(a-b), len(b-a))

def solve_antonio(p : Problem, input ):
    s = []
    myset = set(input)
    current = myset.pop()
    #s.append(current[0])
    s.append(current)
    #for i in range(0,len(input)-1):
    while (len(myset)>0):
        #print(len(myset),current)
        #print(s)
        #print(myset)
        tmp_max = -1
        selected_item = None
        for val in myset:
            tmp = computescore(current,val)
            print(tmp)
            if (tmp >= tmp_max):
                tmp_max = tmp
                selected_item = val
        current = selected_item
        #s.append(selected_item[0])
        s.append(selected_item)
        myset.remove(selected_item)
    return s

if __name__ == "__main__":
    p = Problem('input2019/a_example.txt')
    samplelist = [(None,frozenset({"a","b"})),(None,frozenset({"a","e","b"})),(None,frozenset({"f","g"})),(None,frozenset({"f","g","h"}))]
    #s = solve_antonio(p, p.result_images )
    s = solve_antonio(p, samplelist )
    print(str(s))
    print("done")
