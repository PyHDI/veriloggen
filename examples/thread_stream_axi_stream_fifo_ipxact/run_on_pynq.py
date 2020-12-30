
# coding: utf-8

# In[1]:


from pynq import Overlay, allocate
import numpy as np


# In[2]:


bitfile = "thread_stream_axi_stream_fifo_ipxact.bit"
overlay = Overlay(bitfile)
overlay.ip_dict.keys()


# In[3]:


dma = overlay.axi_dma
blinkled = overlay.blinkled_0


# In[4]:


reduce_size = 8
read_size = 1024
write_size = read_size // reduce_size

src = allocate(shape=(read_size,), dtype=np.int32)
dst = allocate(shape=(write_size,), dtype=np.int32)
bias = allocate(shape=(write_size,), dtype=np.int32)

bias_addr = bias.physical_address


# In[5]:


src[:] = np.arange(read_size, dtype=np.int32)
dst[:] = np.zeros([write_size], dtype=np.int32)
bias[:] = np.ones([write_size], dtype=np.int32)
print(dst[-16:])


# In[6]:


dma.sendchannel.transfer(src)
dma.recvchannel.transfer(dst)

# read_size, write_size, reduce_size, offset
blinkled.write(2 * 4, read_size)
blinkled.write(3 * 4, write_size)
blinkled.write(4 * 4, reduce_size)
blinkled.write(5 * 4, bias_addr)

# start
blinkled.write(0 * 4, 1)

# busy wait
while True:
    busy = blinkled.read(1 * 4)
    if not busy:
        break


# In[7]:


print(dst[-16:])


# In[8]:


expected = np.sum(np.multiply(src, src).reshape([-1, reduce_size]), axis=-1) + bias
print(expected[-16:])


# In[9]:


diff_sum = np.sum(expected - dst)
print(diff_sum)

