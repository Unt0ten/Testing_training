from package_name import capitalize

if capitalize.capitalize('hello') != 'Hello':
    raise Exception('The function is not working properly!')

if capitalize.capitalize('') != '':
    raise Exception('The function is not working properly!')

print('All tests passed!')
