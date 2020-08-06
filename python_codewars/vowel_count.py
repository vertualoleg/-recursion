vowel = ['a','e','i','o','u']
string = input("enter string:")
def vowel_count(string,vowel):
    count = 0
    for char in string:
        for same in vowel:
            if char == same:
                count += 1 
    return count
vowel_count(string,vowel)
