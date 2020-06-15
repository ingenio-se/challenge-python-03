import re
import string



def run():
    
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        message= f.readline()
    
    
    hidden=""   
    for f in re.findall("([a-z]+)", message):
        hidden += f
    
    print("The hidden message is :",hidden)

    
if __name__ == '__main__':
    run()
