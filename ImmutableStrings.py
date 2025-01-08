s1 = 'Kodnest'
s1=s1.upper()
print(s1)


'''
1.Once we declare the string we cannot modify it. if we try to modify the string it will create new string

2.If new string does not have any refernce variable then it will be removed.

3. Python Internally uses String Interning.

4. String Interning is the process of checking string intern pool before creating any new project.

5. whenever we want to create new object , python first will check string intern pool, wether that object already exist or not.

6. When Object already exist in the string intern records then address of existing object will be reused.



'''