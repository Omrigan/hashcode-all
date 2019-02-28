from read_write import Problem, Solution
import random

def computescore(x,y):
    a = x[1]
    b = y[1]
    return min(len(a&b), len(a-b), len(b-a))

iteration = 100

def solve_antonio_sampling(p : Problem, input ):
    s = Solution(p)
    myset = set(input)
    tail = myset.pop()
    head = myset.pop()
    s.add_any(head[0])
    s.add_any(tail[0])
    while (len(myset)>0):
        tmp_max_tail = -1
        selected_item_tail = None
        tmp_max_head = -1
        selected_item_head = None
        testset = random.sample(myset,min(iteration,len(myset)))
        for val in testset: 
            tmp_tail = computescore(tail,val)
            tmp_head = computescore(head,val)
            if (tmp_tail >= tmp_max_head):
                tmp_max_tail = tmp_tail
                selected_item_tail = val
            if (tmp_head >= tmp_max_head):
                tmp_max_head = tmp_head
                selected_item_head = val
        if tmp_max_tail > tmp_max_head:
            tail = selected_item_tail
            s.add_any(selected_item_tail[0])
            myset.remove(selected_item_tail)
        else:
            head = selected_item_head
            s.add_any_head(selected_item_head[0])
            myset.remove(selected_item_head)
    return s

def solve_antonio_sequential(p : Problem, input ):
    s = Solution(p)
    myset = set(input)
    current = myset.pop()
    s.add_any(current[0])
    while (len(myset)>0):
        tmp_max = -1
        selected_item = None
        testset = random.sample(myset,min(iteration,len(myset)))
        for i, val in enumerate(myset):
            if(i > 50):
                break
            tmp = computescore(current,val)
            if (tmp >= tmp_max):
                tmp_max = tmp
                selected_item = val
        current = selected_item
        s.add_any(selected_item[0])
        myset.remove(selected_item)
    return s

'''
if __name__ == "__main__":
    p = Problem('input2019/a_example.txt')
    samplelist = [(None,frozenset({"a","b"})),(None,frozenset({"a","e","b"})),(None,frozenset({"f","g"})),(None,frozenset({"f","g","h"}))]
    #s = solve_antonio(p, p.result_images )
    s = solve_antonio(p, samplelist )
'''
