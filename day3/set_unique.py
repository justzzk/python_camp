#列表元素去重
#1.使用set，集合具有去重的特性,但是结果可能乱序
#使用集合去重要求元素不可变并且可哈希，字典的元素可变并且不可哈希
ini_list=[1,2,3,4,5,6,7,6,5,4,3,2,1]
print('uni_list:%s'%set(ini_list))
#只有当列表中元素是可哈希时可以set(),若元素是字典时则set报错

#2.另定义一个列表或集合，遍历列表中元素，使之唯一的出现在新的列表或集合中
dic_list=[
          {'name':'albert','age':18,'sex':'male'},
          {'name':'alex','age':73,'sex':'male'},
          {'name':'alex','age':20,'sex':'female'},
          {'name':'albert','age':18,'sex':'male'},
          {'name':'albert','age':18,'sex':'male'},
]

#可处理
new_list=[]
for i  in  dic_list:
    if i not in new_list:
        new_list.append(i)
print('new_list:%s'%new_list)

#4定义函数，可同时处理可哈希和不可哈希的列表
#问题：yield的作用；lambda的使用
def uniq(items,key=None):
    s=set()
    for item in items:
        val=item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(uniq(dic_list,key=lambda dic:(dic['name'],dic['age'],dic['sex']))))






