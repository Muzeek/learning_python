'''
Created on 2015/03/31

@author: 2tacss
'''



from struct import pack, unpack




class BinFiler:    
    def __init__(self, file_dir, mode):
        self.__dir = file_dir
        self.__handle = None
        self.__mode = mode
        self.__list_mode = {'r', 'w', 'a', 'b', '+'}
        self.__data_len = {'u_char':1}
    
    
    def __enter__(self):
        if self.__dir is not None and self.__mode is not None:
            if self.__verify_mode() is True:
                self.__handle = open(self.__dir, self.__mode)
                return self.__handle
            else:
                self.__handle = None
        else:
            return None
            
            
    def __exit__(self, type, value, traceback):
        if self.__handle is not None:
            self.__handle.close()
        else:
            raw_input('__exit__')
    
    
    def __verify_mode(self):
        if 'b' in self.__mode:
            for arg_mode in self.__mode:
                for org_mode in self.__list_mode:
                    if org_mode == arg_mode:
                        break
            return True
        
        return False
    
    
    def __chdir(self, new_dir):
        if self.handle is not None:
            self.close_file()
            self.__dir = new_dir
            self.open_file()
    
    
    def open_file(self):
        if self.__dir is not None and self.__mode is not None:
            if self.__verify_mode() is True:
                self.__handle = open(self.__dir, self.__mode)
                return self.__handle
            else:
                self.__handle = None
        else:
            return None
    
    
    def close_file(self):
        if self.handler is not None:
            self.handle.close()
            return True
        else:
            return False
    
    
    def write_str(self, data):
        if self.__handle is not None:
            length = str(len(data))
            fmt = '<'+length+'s'
            self.__handle.write(pack(fmt, data))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    