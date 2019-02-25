#集合间关系，合，交，差，对称差，==，父集，子集
python={'Abby',"Bonda",'Cindy','Doof','Eason'}
ai={'Manda','Nebular','Bonda','Eason','Peter'}

#与关系，两者皆有
print(python&ai)

#或关系，至少有其一
print(python|ai)

#差，只有Python
print(python-ai)

#对称差，只有一种
print(python^ai)

#从结果也可以看出集合中元素是没有排序的