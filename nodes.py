class Console:
    
    def __init__(self):
        
        print('init')
    
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            
            'required': {
                
                'image' : ('IMAGE',),
                "run": (['enabled', 'disabled'],),
                'console' : ('STRING', {'multiline' : True, 'default' : ''})
                             
            }
            
        }
        
    RETURN_TYPES = ('IMAGE',)
    
    FUNCTION = 'execute'
    
    CATEGORY = 'Alper Category'
    
    def execute(self, image, run, console):
        
        if run == 'enabled':
        
            print(eval(console))
            
        if run == 'disabled':
            
            pass
        
        return (image, )
