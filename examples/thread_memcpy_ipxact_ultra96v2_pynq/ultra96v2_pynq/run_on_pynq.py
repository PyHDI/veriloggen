
# coding: utf-8

# In[1]:


from pynq import Overlay, allocate
import numpy as np


# In[2]:


bitfile = "thread_memcpy_ipxact.bit"
overlay = Overlay(bitfile)
overlay.ip_dict.keys()


# In[3]:


memcpy = overlay.memcpy_0


# In[4]:


num_words = 1024 * 128

a = allocate(shape=(num_words,), dtype=np.int32)
b = allocate(shape=(num_words,), dtype=np.int32)

a_addr = a.physical_address
b_addr = b.physical_address


# In[5]:


a[:] = np.random.randint(-20, 20, (num_words,), dtype=np.int32)
b[:] = np.zeros((num_words,), dtype=np.int32)
print(b[-16:])


# In[6]:


copy_bytes = a.nbytes

# copy_bytes, a_offset, b_offset
memcpy.write(2 * 4, copy_bytes)
memcpy.write(3 * 4, a_addr)
memcpy.write(4 * 4, b_addr)

# start
memcpy.write(0 * 4, 1)

# busy wait
while True:
    busy = memcpy.read(1 * 4)
    if not busy:
        break


# In[7]:


print(b[-16:])


# In[8]:


expected = a
print(expected[-16:])


# In[9]:


diff_sum = np.sum(expected - b)
print(diff_sum)

