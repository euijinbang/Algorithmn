# 1. 해시테이블을 리스트로 만든다
hash_table = [0 for i in range(8)]
print(hash_table)

# 2. 데이터로부터 키를 구한다.
def get_key(data):
    return hash(data) % 8

print(get_key('AA'))

# 3. 해시테이블에 data의 키를 인덱스로 잡고, value를 저장한다.
def save_data(data, value):
    hash_address = get_key(data)
    hash_table[hash_address] = value


save_data('jenny', '01040249304')
save_data('john', '01040243404')
print(hash_table)

# 4. 데이터를 읽는다.
def read_data(data):
    hash_address = get_key(data)
    return hash_table[hash_address]

print(read_data('jenny'))




