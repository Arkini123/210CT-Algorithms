def increasing_sequence_of_numbers(d):
    'Return one of the increasing sequence of list d'
    l = []
    for i in range(len(d)):
        l.append(max([l[j] 
for j in range(i)
    if l[j][-1] < d[i]]or [[]], key=len) 
                  + [d[i]])
    return max(l, key=len)
 
if __name__ == '__main__':
    for d in [[5,4,7,5,2,8], [9, 2, 5, 8, 4, 5, 3, 7, 3, 6, 1, 6, 7, 9, 5, 1]]:
        print('A ascending order of the sub-sequence of %s is %s' % (d, increasing_sequence_of_numbers(d)))
