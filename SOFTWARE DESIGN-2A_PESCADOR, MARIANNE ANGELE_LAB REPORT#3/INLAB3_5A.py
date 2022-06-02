def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  
def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'Marianne')
insert(HashTable, 25, 'Angele')
insert(HashTable, 20, 'Martinez')
insert(HashTable, 9, 'Pescador')
insert(HashTable, 21, 'BSCpe')
insert(HashTable, 21, '2A')
  
display_hash (HashTable)