

More questions on Django:==>

Django:->
Flow 
URLS flow
cmd & their meanings
DB related ques
Fetch database objall etc
SQLlite db table names created after migartion cmd...


Diff betw Flask & Django :-->

Create basic API using Flask

GET POST etc

REST API

Class meta in models

what is serialization:
-It removes python dependency
-To fit data into a bandwidth

Pegination:
pagination functionality provides the API with a way to limit the resulting records to a specified amount...! 

========================

Response req cycle


**SQL ALchemy  

SELF <- current obj refer ...

Out put format:--> CSV/JSON/












=========================== Python Basics ====================================

import os
os.system('cls')

Keywords =>
Identifiers => name of var/obj/class/func


Frozenset() ==>
frozenset is the same as set except the forzensets are immutable which means that elements from the frozenset cannot be added or removed once created. The order of elements is not guaranteed to be preserved.


Diff in v2 & v3: print() & xrange()


list comprehension


Dictn comprehension:
to merge multiple dict into one...
OR setdefault() func can also be used...


count():
>>>y = "i am Very good at Python"
>>> print(y.count('Python'))
1
--works in list & tuple as well


Diff Floor & ceil: 
ceil returns value > actual value
Floor return value < actual


Dict are ordered post v3.7.(3.6 and earlier it were unordered.)

###LIST

list.insert(index,items) 
list.append()
--both are similar just index needs to be pass
list.extend()
--extends list

lst.remove(item) --arg is must
lst.pop()
del lst[i]
lst.clear() --just to empty the list

to make sorting case-INsesitive
p.sort(key= str.lower)


##TUPLE
thistuple = ("apple",)
--Remember comma

addition is possible: tpl1+tupl2
multiplication is possible: tpl1 = tupl2 * 2
del tuple1


##SET

SET immutable but new item can be added...
set1.add('item1')

set1.update(list/tuple2)

remove(itm)
discard(itm)
clear()
pop() will work but not sure which one ele will remove from last position.

s3 = s1.union(s2)

intersection() --items which are in both sets
intersection_update()
symmetric_difference() --item which are not in both sets
symmetric_difference_update()
difference()	---(A-B)
difference_update()

##DICTIONARY

.keys()
.values()
.items()


##To generate smthg,yield will store value:

def Generator():
    for i in range(6):
        yield i+1

t = Generator()
for i in t:
    print(i)
=====================================================================================

emunerate()

range() <-- its an iterable obj.

x = y[:]  <-- same as copy not just reference of variable


while creating list/tuple/set using constructor set((iterator)).. pass the iterator...!!


namespace:

__init__:


Signals: Sender & receiver...

Lazy Loading/Caching:
Django querysets are said to be lazily loaded and cached. Lazy loading means that until you perform certain actions on the queryset, such as iterating over it, the corresponding DB query won't be made. Caching means that if you re-use the same queryset, multiple DB queries won't be made.


imlement our own filetr in Template:
Create templatetag folder in app. 

anstract model: 
Don't repeat urself. Class Meta: abstract = True


which template engine is used: 


can we use multiple db in Djnago

DRF

***************************************************************************
Adv Py:

##
Converting dict to set/tuple/list: Only Keys will be added. 
e.g. {'1':'a', '2':'b'} ==>  [1,2]

##
>>y = {}
>>type(y)
>><class 'dict'>

##
>>> d1 = {'a':111, 'b':222, 'c':'333'}
>>> d2 = {'x':000, 'y':999, 'z':'444'}
>>> d3 = {**d1, **d2}
>>> d3
{'a': 111, 'b': 222, 'c': '333', 'x': 0, 'y': 999, 'z': '444'}


>>from sys import getsizeof
print(getsizeof(a))
>>import timeit
timeit.timeit(stmt, setup, timer, number)
