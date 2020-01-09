#!/bin/bash/python
###### Script that encrypts and decrypts stuff
lookup_table = {'a' : 'z', 'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v', 
        'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q', 
        'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l', 
        'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 't' : 'g', 
        'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'} 

def atbash(message): 
    cipher = '' 
    for letter in message: 
        # checks for space 
        if(letter != ' ' and letter.islower()): 
            #adds the corresponding letter from the lookup_table 
            cipher += lookup_table[letter] 
        elif (letter == ' '):
            # adds space 
            cipher += ' '
        else:
            cipher += letter  
    return cipher 
  
# Driver function to run the program 
def main(): 
    #encrypt the given message 
    message = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
    print(atbash(message)) 
      
    #decrypt the given message 
    message = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
    print(atbash(message)) 
  
  
# Executes the main function 
if __name__ == '__main__': 
    main() 
