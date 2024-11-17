# seek function mein bytes se woh read karta hai, means the number of bytes we want 

with open('file.txt','r') as f:
    f.seek(7)

    data=f.read()
    print(data)

