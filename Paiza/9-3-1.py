#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")

get_ipython().system('jupyter nbconvert --to python 9-3-1.ipynb')


# In[ ]:





# In[ ]:





# In[ ]:




