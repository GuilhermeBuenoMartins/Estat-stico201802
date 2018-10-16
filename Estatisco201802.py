
# coding: utf-8

# In[1]:


#Nossos imports:
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


mPontos = np.array([30.1,24.6,27.3,19.5,30.1,24.3,15.1,19.3,23.7,21.8,25.7,25.1,27,24.2,20.3,25,22.1,22.1,13.1,21.1,17.8,27.8,21.8,27.4,16.1,19.2,23.8,20.8,18.7,14.3,17.9,21,23.1,26.4,12.6,20.4,24.8,18.9,18.4,21,16.3,13.3,17.6,25.2,20.2,26.7,25.1,18.7,21.4,18.9,18.2,22.1,10.8,22.5,17.6,18.3,14.5,16.7,25,18.8,14.2,21.5,19.6,7.3,17.1,20.7,18,20.1,19.1,18.8,24.2,24.3,9.8,18.5,21.6,18.8,16.1,17.7,17,16.7,15.6,22.7,18.2,14.9,16.1,19.2,15.2,20.8,19,22.8,11.1,15,16.5,15.2,14.3,12.1,20.3,18.6,18.5,14.6])

mRebotes = np.array([6.2,11.2,7.1,7.2,22.9,10,22.5,10.9,10.9,11.1,7.5,5.3,0,8.5,12.3,10.1,7.9,11.7,0,10.6,10,7,4.2,13.5,6.4,0,4.9,6.3,4.4,7.3,9.8,13.4,16.2,6.3,6.1,6.7,5.9,5.2,12.5,0,10.5,5.1,6.8,5.7,6.2,6.5,12.9,5.4,4.1,3,9.4,14,5.8,13.6,9.5,9.1,5.9,6.6,3,0,5.5,5.6,13.1,8.5,9.8,12.7,10.1,4.7,12.3,4.2,5.7,10.3,12.1,9.6,0,0,4.9,15.6,6,4.7,4.1,4.1,0,11,8.5,0,10.1,9.2,8.6,6.7,15,4.7,0,7.8,6.1,4.4,0,11.7,8.4,0])

mAproveitamento = np.array([49.7,55.9,49.6,52,54,49.6,44,58.2,0,48.5,44.9,47.4,50.6,49.5,51.6,47.5,54.1,38.4,51.8,49.7,48.3,44.2,43.1,0,45.2,48.9,0,0,49,55.4,50.4,40.4,43.6,0,0,40,45.6,41.5,45.2,46.6,52.1,52.1,46.1,37.0,42.5,50.1,47.6,0,40,39.5,50.3,50.9,51.8,46,51.1,53.7,49.5,45.4,46.4,45,50.7,43.5,52.1,52.7,47.9,58,51.4,43.9,58.2,44.1,54,51.8,42.4,52.2,46.7,46,45.6,49.9,48.3,50.2,50.4,38.4,0,43.2,49.4,0,44.6,45.2,40.5,52.3,42.1,43.2,40.2,50.3,56,44.1,45.6,44.6,48.8,0])


# In[3]:


############ Media Pontos ######################
QuantPontos=len(mPontos)
SomaPontos=0

for i in range(0,QuantPontos):
    SomaPontos=SomaPontos+mPontos[i]


MediaPontos=SomaPontos/QuantPontos


# In[4]:


############ Media Rebotes ######################
QuantRebotes=len(mRebotes)
SomaRebotes=0

for i in range(0,QuantRebotes):
    SomaRebotes=SomaRebotes+mRebotes[i]


MediaRebotes=SomaRebotes/QuantRebotes


# In[5]:


############ Media Aproveitamento ######################

QuantAproveitamento=len(mAproveitamento)
SomaAproveitamento=0

for i in range(0,QuantAproveitamento):
    SomaAproveitamento=SomaAproveitamento+mAproveitamento[i]


MediaAproveitamento=SomaAproveitamento/QuantAproveitamento


# In[6]:


##################### Mediana Pontos ################
OrdemPontos= sorted(mPontos)

if (QuantPontos%2==0):
	PosicaoPontos = int(QuantPontos/2)

	MedianaPontos=(OrdemPontos[PosicaoPontos]+OrdemPontos[PosicaoPontos + 1])/2


else :

	PosicaoPontos = int(QuantPontos/2)
	MedianaPontos=OrdemPontos[PosicaoPontos]


# In[7]:


##################### Mediana Rebotes ################
OrdemRebotes= sorted(mRebotes)

if QuantRebotes%2==0 :
	PosicaoRebotes = int(QuantRebotes/2)

	MedianaRebotes=(OrdemRebotes[PosicaoRebotes]+OrdemRebotes[PosicaoRebotes + 1])/2


else :

	PosicaoRebotes = int(QuantRebotes/2)
	MedianaRebotes=OrdemRebotes[PosicaoRebotes]


# In[8]:


##################### Mediana Aproveitamento ################
OrdemAproveitamento= sorted(mAproveitamento)

if QuantAproveitamento%2==0 :
	PosicaoAproveitamento = int(QuantAproveitamento/2)

	MedianaAproveitamento=(OrdemAproveitamento[PosicaoAproveitamento]+OrdemAproveitamento[PosicaoAproveitamento + 1])/2


else :

	PosicaoAproveitamento = int(QuantAproveitamento/2)
	MedianaAproveitamento=OrdemAproveitamento[PosicaoAproveitamento]


# In[13]:


##################### Desvio Padrão Pontos ################
SomaDPPontos=0
SubDPPontos=0

for j in range(0,QuantPontos):
    SubDPPontos= ((mPontos[j]-MediaPontos)**2)
    SomaDPPontos=SomaDPPontos+SubDPPontos
    

DivPontos=SomaDPPontos/QuantPontos

RaizPontos= DivPontos ** 0.5


# In[14]:


##################### Desvio Padrão Rebotes ################
SomaDPRebotes=0
SubDPRebotes=0

for j in range(0,QuantRebotes):
    SubDPRebotes= ((mRebotes[j]-MediaRebotes)**2)
    SomaDPRebotes=SomaDPRebotes+SubDPRebotes
    
   
DivRebotes=SomaDPRebotes/QuantRebotes

RaizRebotes= DivRebotes ** 0.5


# In[15]:


##################### Desvio Padrão Aproveitamento ################
SomaDPAproveitamento=0
SubDPAproveitamento=0

for j in range(0,QuantAproveitamento):
    SubDPAproveitamento= ((mAproveitamento[j]-MediaAproveitamento)**2)
    SomaDPAproveitamento=SomaDPAproveitamento+SubDPAproveitamento
   
DivAproveitamento=SomaDPAproveitamento/QuantAproveitamento

RaizAproveitamento= DivAproveitamento ** 0.5


# In[16]:


################Resultados#####################

print("--------------------Pontos------------------------")
print("A Média dos Pontos é: ",MediaPontos )
print("A Mediana dos Pontos é: ",MedianaPontos )
print("O Desvio Padrão dos Pontos é: ",RaizPontos )

print("\n\n--------------------Rebotes--------------------")
print("A Média dos Rebotes é: ",MediaRebotes )
print("A Mediana dos Rebotes é: ",MedianaRebotes )
print("O Desvio Padrão dos Rebotes é: ",RaizRebotes )

print("\n\n-------------------Aproveitamento--------------")
print("A Média dos Aproveitamentos é: ",MediaAproveitamento )
print("A Mediana dos Aproveitamentos é: ",MedianaAproveitamento )
print("O Desvio Padrão dos Aproveitamentos é: ",RaizAproveitamento )


# In[17]:


#Gráficos 3D:
#Gráfico 1:
axes = Axes3D(plt.figure())
axes.set_title('Média dos Rebotes em relação a Média dos Pontos')
axes.set_xlabel('Média de Pontos')
axes.set_ylabel('Média de Rebotes')
axes.set_zlabel('Id do Jogador')
axes.scatter(mPontos, mRebotes, range(0,100), c='blue')
plt.show()


# In[18]:


#Gráfico 2:
axes = Axes3D(plt.figure())
axes.set_title('Média dos Aproveitamentos em relação a Média dos Pontos')
axes.set_xlabel('Média dos Pontos')
axes.set_ylabel('Média dos Aproveitamentos')
axes.set_zlabel('Id do Jogador')
axes.scatter(mPontos, mAproveitamento, range(0,100), c='red')
plt.show()


# In[19]:


#Gráfico 3:
fig, ax = plt.subplots()
ax.set_title('Distribuição de Frequência de X Média de Pontos')
ax.set_xlabel('Nº de Pontos')
ax.set_ylabel('Frequência')
plt.hist(mPontos,color="g")
plt.show()


# In[20]:


#Grafico 4:
fig, ax = plt.subplots()
ax.set_title('Distribuição de Frequência de Média de Rebotes')
ax.set_xlabel('Nº de Rebotes')
ax.set_ylabel('Frequência')
plt.hist(mRebotes,color="b")
plt.show()


# In[21]:


#Gráfico 5:
fig, ax = plt.subplots()
ax.set_title('Distribuição de Frequência de X Média de Aproveitamento')
ax.set_xlabel('Nº de Aproveitamento')
ax.set_ylabel('Frequência')
plt.hist(mAproveitamento,color="r")
plt.show()

