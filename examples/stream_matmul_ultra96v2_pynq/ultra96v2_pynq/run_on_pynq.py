
# coding: utf-8

# In[1]:


from pynq import Overlay, allocate
import numpy as np


# In[2]:


bitfile = "stream_matmul.bit"
overlay = Overlay(bitfile)
overlay.ip_dict.keys()


# In[3]:


blinkled = overlay.blinkled_0


# In[4]:


matrix_size = 256

a = allocate(shape=(matrix_size, matrix_size), dtype=np.int32)
b = allocate(shape=(matrix_size, matrix_size), dtype=np.int32)
c = allocate(shape=(matrix_size, matrix_size), dtype=np.int32)

a_addr = a.physical_address
b_addr = b.physical_address
c_addr = c.physical_address


# In[5]:


a[:] = np.random.randint(-20, 20, (matrix_size, matrix_size), dtype=np.int32)
# matrix b should be transposed
b[:] = np.random.randint(-20, 20, (matrix_size, matrix_size), dtype=np.int32)
c[:] = np.zeros((matrix_size, matrix_size), dtype=np.int32)
print(c.reshape([-1])[-16:])


# In[6]:


# matrix_size, a_offset, b_offset, c_offset
blinkled.saxi.write(2 * 4, matrix_size)
blinkled.saxi.write(3 * 4, a_addr)
blinkled.saxi.write(4 * 4, b_addr)
blinkled.saxi.write(5 * 4, c_addr)

# start
blinkled.saxi.write(0 * 4, 1)

# busy wait
while True:
    busy = blinkled.saxi.read(1 * 4)
    if not busy:
        break


# In[7]:


print(c.reshape([-1])[-16:])


# In[8]:


expected = np.matmul(a, b.T)
print(expected.reshape([-1])[-16:])


# In[9]:


diff_sum = np.sum(expected - c)
print(diff_sum)

