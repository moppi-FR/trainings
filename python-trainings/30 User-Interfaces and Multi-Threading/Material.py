#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#create class
class Material:
    def __init__ (self, mat_id, mat_name, unit, minimum, maximum):
        self.Material_Id = mat_id
        self.Material_Name = mat_name
        self.Unit = unit
        self.Minimum = minimum
        self.Maximum = maximum

