trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]
dic_tree = {}

for tree in trees:
    if tree in dic_tree:
        dic_tree[tree]+=1
    else:
        dic_tree[tree] = 1
        
for specie,count in dic_tree.items():
    print(f'{specie}: {count}')



def counter(word):
    return len(word)

customer = (
    ('id','98698761'), 
    ('name', 'marry'), 
    ('surname', 'smith'), 
    ('rented_books', 3 )
    )
    
    
new = dict(customer)

print(new)

value = 10  

print(type(value) == 'int' and 0 < value < 20)

