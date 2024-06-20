##Control statements
##simple if
##if-else
##Nested if
##elif


##if
##print('python')
##print('hello world')
##a=10
##b=20
##if a<b:
##    print('a is less then b')
##    print('thankyou')
##print('hello universe')

##s=input('enter the string:')
##if len(s)>5:
##    print(s[::-1])

##s=input('enter the string:')
##if 'A'<=s[0]<='Z' or 'a'<=s[0]<='z':
##    print('hello world')

##s=input('enter the string:')
##if s.startswith('h'):
##    print('hello world')

##s=input('enter the value:')
##if 'A'<=s[0]<='Z' or 'a'<=s[0]<='z':
##    print('chethu')

##s=input('enter the value:')
##if s.isalpha():
##    print('chethu')

##s=input('enter the value:')
##if s.isupper():
##    print('chethu')

##s=input('enter the value:')
##if s.islower():
##    print('chethu')

##s=input('enter the value:')
##if s.isdigit():
##    print('chethu')
    

##s=input('enter the value:')
##if 5<len(s)<8:
##    print('hello world')


##if else
##s=input('enter the value:')
##if s[-1] in 'AEIOUaeiou':
##               print('vowel')
##else:
##    print('not an vowel')

##s=input('enter the value:')
##if len(s)%2==0:
##    print(s[0::2])
##else:
##    print(s[1::2])

##s=input('enter the value:')
##if s.isupper() and s.isalpha():
##    print(len(s))
##else:
##    print(list(s))

##s=input('enter the value:')
##if s.startswith('A'):
##    print(s[::-1])
##else:
##    print(s[0])

##s=input('enter the value:')
##if s[0] in'AEIOUaeiou':
##    print('it is a vowel')
##else:
##    print('not an vowel')

##s=input('enter the value:')
##if s.startswith(s[-1] in 'AEIOUaeiou'):
##               print('vowel')
##else:
##    print('not an vowel')

##s='python3 hello2 world4'
##3+2+4==9
##result=0
##for i in 3:
##    if i.isdigit():
##        result+=int(i)
##print(result)

##l=[10,20,30,40,10,20,15,20,15]
##for i in l:
##    if l.count(i)>1:
##        print(i)

##l=[1,2,3,4,5,6,7,8]
##for i in l:
##    if i%2==0:
##        print(i)

##l=['apple','google','facebook','yohoo']
##for i in l:
##    if i[-1] in 'AEIOUaeiou':
##        print(i)

##l=['apple','google','facebook','yohoo','king','word']
##for i in l:
##    if len(i)%2==0:
##        print(i)


##l=[10,True,'hello',10.5,'100',10+20j]
##for i in l:
##    if type(i) in (int,float,bool,complex):
##        print(i)

##l=[1,2,3,4,5,6,7,8]
##for i in l:
##    if i%2==0:
##        print(i)
##        break

##l=input('enter the valie:')
##for i in l:
##    if i[0] in 'AEIOUaeiou':
##        print(i)
##        break

##l=[1,2,3,4,5,6,7,8]
##for i in l:
##    pass

##l=['apple','google','facebook','yohoo','king','word']
##for i in l:
##    if type(i)==str:
##        print(ord(i[0]))

##l=['apple','google','facebook','yohoo','king','word']
##for i in l:
##    if len(i)%2==0:
##        print(i[::-1])
##    else:
##        print(len(i))

##for i in range(1,31):
##    if i%3==0:
##        print(i)

##l=[10,15,30,10,30,40,50]
##for i in l:
##    if l.count(i)==1:
##        print(i)


##s=input('enter the value:')
##count=0
##i=0
##while i<len(s):
##    if s[i].isupper():
##        count+=1
##    i+=1
##print(count)


##s=set()
##for i in range(10,0,-1):
##    s.add(i)
##print(s)
####comprehension
##o={i for i in range(10,0,-1)}
##print(o)


##l=[10,10.5,False,'jk']
##s=set()
##for i in l:
##    if type(i) in (int,float,bool,complex):
##        s.add(type(i))
##    else:
##        s.add(len(i))
##print(s)
####comprehension
##o={type(i) if type(i) in (int,float,bool,complex) else len(i) for i in l}
##print(o)

##l=['miller','king','steve','google','amazon','adams']
##s=set()
##for i in l:
##    if len(i)%2==0:
##        s.add(i[::-1])
##    else:
##        s.add(len(i))
##print(s)
####comprehension
##o={i[::-1] if len(i)%2==0 else len(i) for i in l}
##print(o)

##a='python3114'
##s=set()
##for i in a:
##    if i.isalpha():
##        s.add(ord(i))
##print(s)
####comprehension
##o={ord(i) for i in a if i.isalpha()}
##print(o)

##a='programming'
##s=set()
##for i in a:
##    if i not in 'AEIOUaeiou':
##        s.add(i)
##print(s)
####comprehension
##o={i for i in a if i not in 'AEIOUaeiou'}
##print(o)

##s=set()
##for i in range(0,101,2):
##    s.add(i)
##print(s)
####comprehension
##o={i for i in range(0,101,2)}
##print(o)

##s=input('enter the value:')
##count=0
##i=0
##while i<len(s):
##    if s[i].isupper():
##        count+=1
##    i+=1
##print(count)

##def check(a):
##    return a[0]
##print(check('chethu'))

##l=[10,10.5,'hello',10+20j,[3,3,4],(1,2,3)]
##d={}
##for i in l:
##    if type(i) in (int,float,bool,complex):
##        d[i]=type(i)
##    else:
##        d[i]=len(i)
##print(d)

##l=['chethu','manju','bharathi','manasa','jay','guru']
##print(sorted(l,key=len,reverse=True))

##s=' hai hello world welcome to python programming language and programming is fun'
##l=s.split()
##for i in s:
##    if s.count(i)==1:
##        res=sorted(i,key=len)
##        print(res[-1])


##with open('chethu.txt','w')as f:
##    line1='hello world\n'
##    line2='hello universe\n'
##    line3='python\n'
##    f.writelines([line1,line2,line3])

##with open('chethu.txt','a')as f:
##    f.write('welcome')

##def count(path):
##    with open(path,'r')as f:
##        line=f.readlines()
##        print(len(line))
##print(count('chethu.txt'))


##with open('chethu.txt','r')as f:
##    line=f.readlines()
##    for lineno,line in enumerate(line,start=1):
##        if lineno%2==0:
##            print(lineno)

##with open('chethu.txt','r')as f:
##    line=f.read()
##    print(line)
##    words=line.split()
##    count=0
##    for i in words:
##        if i[-1] in 'aeiouAEIOU':
##            count+=1
##            print(count)

##with open('dinga.txt','w')as f:
##    line1='hello world\n'
##    line2='hello universe\n'
##    line3='python\n'
##    f.writelines([line1,line2,line3])



##with open(r'C:\Users\Its MY PC\Downloads\sample.log','r+')as f:
##    content=f.readlines()
##    for lineno,line in enumerate(content,start=1):
##        print(lineno,line,sep="-")

##with open(r'C:\Users\Its MY PC\Downloads\sample.log','r+')as f:
##    content=f.readlines()
##    count=0
##    for i in content:
##        if len(i)>2 and i.split()[2]=='INFO':
##            count+=1
##    print(count)

##with open(r'C:\Users\Its MY PC\Downloads\sample.log','r+')as f:
##    content=f.readlines()
##    for i in content:
##        if len(i)>2 and len(i.split()[2])%2!=1:
##            print(i.split()[2])


##with open(r'C:\Users\Its MY PC\Downloads\sample.log','r+')as f:
##    content=f.readlines()
##    d={}
##    for i in content:
##        if len(i)>2:
##            d[i.split()[2]]=len(i.split()[2])
##    print(d)


##def sample():
##    yield 1
##    yield 2
##    yield 'hai'
##print(list(sample()))
##print(next(sample()))
##print(next(sample()))
##print(next(sample()))
##for i in sample():
##    print(i)

##num=[i for i in range(1,111111111111)]
##print(num)
####memory error

##num=(i for i in range(1,111111111111))
##for i in num:
##    print(i)

##s='hello'
##v=(i for i in s if i in 'aeiou')
##print(tuple(v))
##
##def vowel():
##    for i in s:
##        if i in 'aeiou':
##             yield i
##print(list(vowel()))


##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for line in lines:
##        print(line)

####1
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    count=0
##    for line in lines:
##        if len(line)>1 and line.split()[2]=='[ERROR]':
##            count+=1
##    print(count)

####2
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for i in lines:
##        if len(i)>1 and i.split()[2]=='[WARNING]':
##            print(' '.join(i.split()[4:]))

####3
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for i in lines:
##         if len(i)>1 and i.split()[2]=='[]'and len(i.split()[4:])>1:
##            print(' '.join(i.split()[:2]))

####4       
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    l=[' '.join(i.split()[4:]) for i in lines if len(i)>1 and i.split()[2]=='[INFO]']
##    print(l)

####5
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    d={}
##    for i in lines:
##        if len(i)>1 and len(i.split())>4 and i.split()[4]=='entering':
##            d[i.split()[1]]=i.split()[0]
##    print(d)

####6
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    d={}
##    for lineno,line in enumerate(lines,start=1):
##        if len(line)>1 and len(line.split())>4 and line.split()[2]=='[INFO]':
##            d[lineno]=' '.join(line.split()[4:])
##    print(d)

####7
##def sample(path):
##    with open(path,'r') as f:
##        lines=f.readlines()
##        for i in lines:
##            if len(i)>1 and len(i.split()[4:])>1:
##                print(i.split()[-1])
##res=sample(r"C:\Users\Its MY PC\Downloads\log.txt")
        
####8
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    g=(i.split()[4] for i in lines if len(i)>1 and len(i.split()[4:])>1 and len(i.split()[4])%2==0)
##    print(tuple(g))

###9
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for i in lines:
##        if len(i)>1 and len(i.split())>4 and i.split()[2]=='[]':
##            print(' '.join(i.split()[4:]))
                
###10
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for i in lines:
##        if len(i)>1 and i.split()[2]=='[]'and len(i.split()[4:])>1:
##            print(i.split()[0])

####11
##def sample(path):
##    with open(path,'r') as f:
##        lines=f.readlines()
##        count=0
##        for i in lines:
##            if len(i)<=1:
##                count+=1
##        return count
##print(sample(r"C:\Users\Its MY PC\Downloads\log.txt"))
                
###12
##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for line in lines:
##        if len(line)<=1:
##            print(line)
##            print(len(line))

##with open(r"C:\Users\Its MY PC\Downloads\log.txt",'r')as f:
##    lines=f.readlines()
##    for i in lines:
##        if len(i)>1 and len(i.split()[4:])>1 and len(i.split()[4])%2==0:
##            print(i.split()[4])
        
##def word(path):
##    with open(path,'r') as f:
##        lines=f.readlines()
##        for i in lines:
##            if len(i)>1 and len(i.split()[4:])>1 and len(i.split()[4])%2==0:
##                yield i.split()[4]
##res=word(r"C:\Users\Its MY PC\Downloads\log.txt")
##print(tuple(res))

##def greet():
##    return 'hai'
##a=greet()
##print(a)
##b=greet
##print(b())
##c=greet
##d=greet
##print(c)

##def sample(text):
##    return text.upper()
##def demo(t):
##    return t.lower()
##def greet(func):
##    result=func('Hai HEllo worLd')
##    return result
##print(greet(sample))
##print(greet(demo))


##def sample(x):
##    def demo(y):
##        return x+y
##    return demo
##new=sample(1)
##print(new(3))



##def sample(a):
##    def demo(b):
##        return a-b
##    return demo
##c=sample(100)
##print(c(73))

##from time import sleep
##def delay(func):
##    def inner(*args,**kwargs):
##        sleep(5)
##        res=func(*args,**kwargs)
##        return res
##    return inner
##@delay
##def greet():
##    return'hai hello'
##print(greet())

##def delay(func):
##    def inner(*args,**kwargs):
##        res=func(*args,**kwargs)
##        return res.upper()
##    return inner
##@delay
##def sample():
##    return 'hai hello world'
##
##print(sample())

##def delay(func):
##    def inner(*args,**kwargs):
##        res=func(*args,**kwargs)
##        return res[::-1]
##    return inner
##@delay
##def sample():
##    return 'hai hello world'
##
##print(sample())


##def delay(func):
##    def inner(*args,**kwargs):
##        res=func(*args,**kwargs)
##        return abs(res)
##    return inner
##@delay
##def sample(a,b):
##    return a-b
##
##print(sample(10,100))


d={}
def count_calls(func):
    def inner(*args, **kwargs):
        if func.__name__  not in d:
            d[func.__name__]= 1
        else:
            d[func.__name__]+=1
        result = func(*args, **kwargs)
        return result
    return inner
@count_calls
def sample():
    return 'hai'
@count_calls
def demo():
    return 'hello'
print(sample())
print(sample())
print(demo())
print(demo())
print(demo())
print(d) 


        


