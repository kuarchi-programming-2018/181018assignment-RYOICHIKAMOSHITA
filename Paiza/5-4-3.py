#!/usr/bin/env python
# coding: utf-8

# In[5]:


# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for key in points:
    sum+= points[key]
print(int(sum))


get_ipython().system('jupyter nbconvert --to 5-4-3.ipynb')


# In[ ]:




