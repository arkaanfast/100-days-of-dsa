# Takes the following input :- number of items, a weights array, a value array, and the capacity of knap_sack

def knap_sack(n, w, v, c):

    if n == 0 or w == 0:
        return 0

    if w[n - 1] > c:
        return knap_sack(n - 1, w, v, c)

    else:
        return max(v[n - 1] + knap_sack(n - 1, w, v, c - w[n - 1]), knap_sack(n - 1, w, v, c))



val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knap_sack(n, wt, val, W)) 

