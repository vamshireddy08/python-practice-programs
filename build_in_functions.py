def count_match_index(l):
    inc=0
    for count,val in enumerate(l):
        if count==val:
            inc=inc+1 
    print inc 

count_match_index([0,2,2,1,5,5,6,10])    


def d_list(l):
    d={}
    for count,ele in enumerate(l):
        d[ele]=count 
    print d    

d_list(['a','b','c'])    


def concatenate(l1,l2,connector):
    con=[]
    ans=[]
    con.append(connector)
    l=len(l1)
    con=con*l
    list= zip(l1,con,l2)
    for ele in list:
        ans.append(''.join(ele))
    print ans
concatenate(['A','B'],['a','b'],'-')    


def word_lengths(phrase):

    list=phrase.split(' ')
    lengths= map(lambda word:len(word) , list)
    print lengths

word_lengths("how long are the words in this phrase")    

def digits_to_num(digits):
    print    reduce(lambda x,y:x*10 +y ,digits)
digits_to_num([3,4,3,2,1]) 

def filter_words(word_list,letter):
    print filter(lambda x: x[0]==letter ,word_list)

l=['hello','are','cat','hi','dog','ham','go','to','heart' ]
filter_words(l,'h')
