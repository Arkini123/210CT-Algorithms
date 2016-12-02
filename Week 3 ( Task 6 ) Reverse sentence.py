sentence = "Everything is awesome"

#('how','are','you'] are registered in 'first'
first = sentence.split()

# ['you','are','how] are registered in 'final'
final = first[::-1] 

''.join(final)

print (final)

