'''
    usage of string
'''
codes =[
    "'Python,java,c'.split(',')",
    #"'Python\n\n\n'.strip()",
    "'Python\n'.rstrip()",
    "'*Python'.lstrip('*')",
]
for code in codes:
    print('>>>',code)
    print(eval(code))
