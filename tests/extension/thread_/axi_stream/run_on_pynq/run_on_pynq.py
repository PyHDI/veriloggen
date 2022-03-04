
# coding: utf-8

# In[1]:


from pynq import Overlay, allocate
import numpy as np


# In[2]:


bitfile = "axi_stream.bit"
overlay = Overlay(bitfile)
overlay.ip_dict.keys()


# In[3]:


dma = overlay.axi_dma_0
blinkled = overlay.blinkled_0


# In[4]:


size = 1024
src = allocate(shape=(size,), dtype=np.int32)
dst = allocate(shape=(size,), dtype=np.int32)


# In[5]:


src[:] = np.arange(size, dtype=np.int32)
dst[:] = np.zeros([size], dtype=np.int32)


# In[6]:


print(dst[-16:])


# In[7]:


# size
blinkled.saxi.write(2 * 4, size)

# start
blinkled.saxi.write(0 * 4, 1)

dma.sendchannel.transfer(src)
dma.recvchannel.transfer(dst)

# busy wait
while True:
    busy = blinkled.saxi.read(1 * 4)
    if not busy:
        break


# In[8]:


print(dst[-16:])


# In[9]:


expected = src + [1]
print(expected[-16:])


# In[10]:


diff_sum = np.sum(expected - dst)
print(diff_sum)

