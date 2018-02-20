list1=[1,2,3,4,5,6,7]
list2=[3,5]
print list(set(list1).intersection(list2))

def common_elements(list1,list2):
    return list(set(list1) & set(list2))
def common_ele(list1,list2):
    result=[]
    for x in list1:
        if x in list2:
            result.append(x)
    return result        
def common_elements_shortcut(list1,list2):
    return [x for x in list1 if x in list2]

print common_elements_shortcut(list1,list2)
print common_ele(list1,list2)
print common_elements(list1,list2)
print list(set(list1)-(set(list1)-set(list2)))
