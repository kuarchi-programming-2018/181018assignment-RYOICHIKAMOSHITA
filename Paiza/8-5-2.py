#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    # この下に、合計得点を戻り値として返すsumメソッドを記述する
    def sum(self):
        return self.kokugo + self.sansu
        
yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")

get_ipython().system('jupy')

