alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Create the alphabet
def getindex(char,password):               #This function is used for getting the position of characters of the matrix(list of lists)
    for a in range(5):
        for b in range(5):
            if password[a][b]==char:
                return a,b
def playfaircipher(message, password): #This function is used for ciphering the message 
    n=0
    ciphertext=''
    while n<len(message):
        a1,b1=getindex(message[n],password) 
        a2,b2=getindex(message[n+1],password)
        if a1==a2:                  # for characters in the same row.
            b1+=1                   # column +1
            b2+=1                   # column +1
            ciphertext=ciphertext+password[a1][b1%5]+password[a2][b2%5]  
        elif b1==b2:                # for characters in the same column 
            a1+=1                   #row +1
            a2+=1
            ciphertext=ciphertext+password[a1%5][b1]+password[a2%5][b2]
        else:  # for charcters in a rectangle
            ciphertext=ciphertext+password[a2][b1]+password[a1][b2]
        n+=2
    print(ciphertext)
    pass
def checkthekey(key): #change the key to the password (MATRIX: list of lists)  
    alist=list(alphabet) #change it into list
    leftover=[]
    key=key.replace('X','KS') #Replace X by KS
    alist.remove('X')
    for char in key:
        if char not in leftover:
            leftover.append(char) #append the characters into password
            alist.remove(char)       #the leftover  
    KeyString=''.join(leftover+alist)
    password = [KeyString[i:i+5] for i in range(0, len(KeyString), 5)]
    return password
def getthemessage(msg):# chenge the forms of message
    msg=msg.replace('X','KS') 
    #Replace X by KS
    n=0
    msg1=list(msg) #Chenge it into a list
    while n<=len(msg1)-2:
        if msg1[n]==msg1[n+1]:  #if the next character is the same as before 
            msg1.insert(n+1,'Q')
        n+=2
    if len(msg1)%2==1:          #if length of message is odd
        msg1.append('Z')
    return msg1
userInput = input('What is you string?')
token=userInput.split(' ')      #split the input information to key and message
if len(token)==2:
    key=token[0]
    password=checkthekey(key)
    print(password)
    msg=token[1]
    message=getthemessage(msg)
    print(message)
    playfaircipher(message, password)
else:
    print('ERROR')