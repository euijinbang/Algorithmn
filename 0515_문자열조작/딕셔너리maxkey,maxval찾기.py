a_dictionary = {"a": 1, "b": 2, "c": 3}

"""
get key with max value
"""
max_key = max(a_dictionary, key=a_dictionary.get)
print(max_key)

"""
get max value
"""
max_value = max(a_dictionary.values())
print(max_value)