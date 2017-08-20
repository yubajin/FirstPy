class OldStyle:
    hobby = 'Play Computer'
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def self_introduction(self):
        print ('My name is %s,\nMy hobby is %s' %(self.name, self.hobby))
        
class NewStyle(object):
    hobby = 'Play Computer'
    
    def __init__(self, name, description, prote):
        self.name = name
        self._description = description
        self.__prote = prote
    
    @classmethod
    def get_hobby(cls):
        return cls.hobby
    
    @property
    def get_description(self):
        return self._description
    
    def self_introduction(self):
        print ('My name is %s,\nMy hobby is %s' %(self.name, self.hobby))
    
class BackendNewStyle(NewStyle):
    
    def __init__(self,name,description,prote,language):
        super(BackendNewStyle, self).__init__(name,description,prote)
        self.language = language
        
if __name__=='__main__':
    '''
    old = OldStyle('old','Old style class')
    print (old)
    print (type(old))
    print (dir(old))
    print ('-----------------------------------------')
    '''
    new = NewStyle('new','New style class','prote')
    print (new)
    print (type(new))
    print (dir(new))
    print (new.__dict__)
    '''
    
    
    print ('This is the attribute access way----------')
    print ('name:',new.name)
    print ('description:',new._description,',or access by method of get_description:',new.get_description)
    print ('prote:',new._NewStyle__prote)
    print ('This is the attribute access way----------')
    
    
    print ('This is advancefunc @classmethod:',NewStyle.get_hobby())
    
    oldStyle = OldStyle('oldStyle','this is oldstyle')
    backendNewStyle = BackendNewStyle('newStyle','this is newStyle',3,'Chinese')
    oldStyle.self_introduction()
    backendNewStyle.self_introduction()
    
    print('dir(backendNewStyle):',dir(backendNewStyle))
    print('backendNewStyle.__dict__:',backendNewStyle.__dict__)
    print('type(backendNewStyle:',type(backendNewStyle))
    print('isinstance(backendNewStyle,NewStyle):',isinstance(backendNewStyle,NewStyle))
    '''
    