#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from zipfile import ZipFile

class zipfile_extracting(ZipFile):
    
    def __init__(self, file_path, destination):
        self.file_path = file_path
        self.destination = destination
        
    def unzipping(self):
        with ZipFile(self.file_path, 'r') as zipped:
            zipped.extractall(self.destination)
            
            

