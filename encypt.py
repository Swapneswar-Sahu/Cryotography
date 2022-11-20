def encrypt(content, key):
    result = ''
    key = key % 10
    for letter in content:
        num = ord(letter)
        num = num + key
        result += chr(num)
    return result
    
fname = input('Enter the file name: ')
key = int(input('Enter the key: '))
fp = open(fname, 'r')
content = fp.read()
fp.close()
new_content = encrypt(content, key)
fp = open(fname, 'w')
fp.write(new_content)
fp.close()