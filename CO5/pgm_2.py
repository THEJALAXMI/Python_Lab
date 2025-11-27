f1=open('pgm_1.txt','r')
f2=open('pgm_2.txt','w')
content=f1.readlines()
print("Content\n", content)
for i in range(0,len(content)):
    if(i%2==0):
        f2.write(content[i])
    else:
        pass
f2.close()
f2=open('pgm_1.txt','r')
content1=f2.read()
print("\nodd lines\n\n",content1)
f2.close()
