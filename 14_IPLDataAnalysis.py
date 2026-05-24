#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np

#Seasons
Seasons = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
Sdict = {"2010":0,"2011":1,"2012":2,"2013":3,"2014":4,"2015":5,"2016":6,"2017":7,"2018":8,"2019":9}

#Players
Players = ["Sachin","Rahul","Smith","Sami","Pollard","Morris","Samson","Dhoni","Kohli","Sky"]
Pdict = {"Sachin":0,"Rahul":1,"Smith":2,"Sami":3,"Pollard":4,"Morris":5,"Samson":6,"Dhoni":7,"Kohli":8,"Sky":9}

#Salaries
Sachin_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Rahul_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
Smith_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Sami_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Pollard_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Morris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Samson_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Dhoni_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Kohli_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Sky_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]
#Matrix
Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, Sami_Salary, Pollard_Salary, Morris_Salary, Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])

#Games 
Sachin_G = [80,77,82,82,73,82,58,78,6,35]
Rahul_G = [82,57,82,79,76,72,60,72,79,80]
Smith_G = [79,78,75,81,76,79,62,76,77,69]
Sami_G = [80,65,77,66,69,77,55,67,77,40]
Pollard_G = [82,82,82,79,82,78,54,76,71,41]
Morris_G = [70,69,67,77,70,77,57,74,79,44]
Samson_G = [78,64,80,78,45,80,60,70,62,82]
Dhoni_G = [35,35,80,74,82,78,66,81,81,27]
Kohli_G = [40,40,40,81,78,81,39,0,10,51]
Sky_G = [75,51,51,79,77,76,49,69,54,62]
#Matrix
Games = np.array([Sachin_G, Rahul_G, Smith_G, Sami_G, Pollard_G, Morris_G, Samson_G, Dhoni_G, Kohli_G, Sky_G])

#Points
Sachin_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Rahul_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
Smith_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Sami_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Pollard_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Morris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Samson_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Dhoni_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Kohli_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Sky_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]
#Matrix
Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, Sami_PTS, Pollard_PTS, Morris_PTS, Samson_PTS, Dhoni_PTS, Kohli_PTS, Sky_PTS])             
                  


# In[68]:


Salary


# In[34]:


Games


# In[69]:


Points


# In[70]:


mydata = np.arange(0,20)
print(mydata)


# In[71]:


np.reshape(mydata,(4,5))


# In[72]:


mydata


# In[73]:


Mat1 = np.reshape(mydata,(5,4),order = 'c')
Mat1


# In[74]:


Mat1[4,3]


# In[76]:


Mat1[3,3]


# In[77]:


Mat1[-3,-1]


# In[80]:


Mat2 = np.reshape(Mat1,(5,4),order = 'f')
Mat2


# In[81]:


Mat2[4,3]


# In[82]:


Mat2[0,2]


# In[83]:


Mat2[0:2] #this is only for rows starts from 0 and ends at 1st row


# In[84]:


Mat2[1:2]


# In[85]:


Mat2


# In[86]:


Mat2[-2,-3]


# In[87]:


Mat2


# In[88]:


Mat2[0:2]


# In[89]:


Mat2[:,2]


# In[90]:


Mat2[:,2].reshape(-1,1)


# In[91]:


Mat2[:,3].reshape(-1,1)


# In[96]:


Mat3 = np.reshape(mydata, (5,4), order = 'C')
Mat3


# In[93]:


Mat2 #F shaped


# In[97]:


Mat3 #C shaped


# In[100]:


a1 = ['welcome','to','datascience']
a2 = ['Need','real', 'HardWork']
a3 = [1,2,3]
[a1,a2,a3] #Lists the datatype


# In[101]:


np.array([a1,a2,a3])


# In[102]:


Games


# In[103]:


Games[0]


# In[104]:


Games[5]


# In[105]:


Games[0:5]


# In[106]:


Games[0:2]


# In[107]:


Games[1:2]


# In[108]:


Games[2]


# In[109]:


Games[2,8]


# In[111]:


Games


# In[110]:


Games[-3:-1]


# In[112]:


Points


# In[113]:


Points[0]


# In[114]:


Points[6,1]


# In[115]:


Points[3:6]


# In[116]:


Points[-6,-1]


# In[117]:


dict1={'key1':'val1','key2':'val2','key3':'val3'}


# In[118]:


dict1


# In[119]:


dict1['key1']


# In[120]:


dict2 = {'Germany':'The Beauticul Country','France':2,'Spain':True}


# In[121]:


dict2


# In[124]:


dict2['Spain']


# In[125]:


dict2['Germany']


# In[126]:


dict2['France']


# In[127]:


Games


# In[128]:


Pdict


# In[129]:


Pdict['Sachin']


# In[130]:


Pdict['Dhoni']


# In[131]:


Games[0]


# In[132]:


Pdict['rahul']


# In[133]:


Games[1]


# In[134]:


Games[Pdict['Rahul']]


# In[135]:


Games[Pdict['Dhoni']]


# In[137]:


Points


# In[138]:


Salary


# In[139]:


Salary[2,4]


# In[140]:


Salary[Pdict['Sky'],Sdict['2019']]


# In[141]:


Salary[Pdict['Sachin'],Sdict['2010']]


# In[ ]:


Sdict


# In[36]:


Pdict


# In[38]:


Salary


# In[39]:


Salary/Games


# In[40]:


Salary//Games


# In[142]:


np.round(Salary/Games)


# In[41]:


Points


# In[42]:


Salary[2]


# In[43]:


Games[2]


# In[44]:


Points[2]


# In[45]:


Salary[0]


# In[46]:


Pdict


# In[47]:


# to ignore the os warnings error while visulize the graph
import warnings
warnings.filterwarnings('ignore')


# In[48]:


import matplotlib.pyplot as plt


# In[143]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[49]:


plt.plot(Salary[0])


# In[50]:


plt.plot(Salary[0],c='g')


# In[51]:


plt.plot(Salary[0],c='g',ls = '--')


# In[52]:


plt.plot(Salary[0],c='k',ls = ':')


# In[53]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=7,3 # 7 width,3 is height


# In[54]:


plt.plot(Salary[0],c='k',ls = '-.')


# In[55]:


plt.plot(Salary[0],c='k',ls = '--',marker = 'o')


# In[56]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7)
plt.xticks(list(range(0,10)),Seasons)
plt.show()


# In[57]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7)
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[59]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7)
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8)

plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[60]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7)
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8)
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8)
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[61]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])

plt.legend()
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[63]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])
plt.plot(Salary[3], c = 'cyan',ls ='-',marker ='v',ms=8,label = Players[3])

plt.legend()
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[64]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])
plt.plot(Salary[3], c = 'cyan',ls ='-',marker ='v',ms=8,label = Players[3])

plt.legend(loc= 'upper left',bbox_to_anchor=(0,0))
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[65]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])
plt.plot(Salary[3], c = 'cyan',ls ='-',marker ='v',ms=8,label = Players[3])

plt.legend(loc= 'lower left',bbox_to_anchor=(1,0))
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[66]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])
plt.plot(Salary[3], c = 'cyan',ls ='-',marker ='v',ms=8,label = Players[3])

plt.legend(loc= 'lower left',bbox_to_anchor=(1,1))
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical')
plt.show()


# In[67]:


plt.plot(Salary[0], c = 'black',ls ='--',marker ='o',ms=7,label = Players[0])
plt.plot(Salary[1], c = 'green',ls =':',marker ='d',ms=8,label = Players[1])
plt.plot(Salary[2], c = 'red',ls ='-.',marker ='^',ms=8,label = Players[2])
plt.plot(Salary[3], c = 'cyan',ls ='-',marker ='v',ms=8,label = Players[3])

plt.legend(loc= 'upper right',bbox_to_anchor=(1,0)) #to visualize the graph detail
plt.xticks(list(range(0,10)),Seasons,rotation ='vertical') # To alter the x axis values
plt.show()


# In[151]:


plt.plot(Salary[0],c='g',ls=':',marker='o',ms=7,label = Players[0])
plt.xticks(list(range(0,10)),Seasons,rotation='vertical')
plt.legend(loc='upper right',bbox_to_anchor=(0,0))
#plt.legend(loc= 'upper right',bbox_to_anchor=(1,0))
plt.show()


# In[153]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Salary[3], c='Purple', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Salary[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Salary[5], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Salary[6], c='Red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Salary[7], c='Red', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Salary[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Salary[9], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[ ]:




