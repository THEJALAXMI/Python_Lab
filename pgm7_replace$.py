s=input("Enter a word: ") 
c=s[0] #it extracts the first character of the input word
str1=s.replace(s[0],'$')	 #
r=c+str1[1:]
print (r )
