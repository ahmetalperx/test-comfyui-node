class Alper:
    
    @classmethod
    def INPUT_TYPES(cls):
        
        return {
            
            'required' : {
                
                'image' : ('IMAGE',)
                
            }
            
        }
    
    RETURN_TYPES = ()
    
    FUNCTION = 'node_function'
    
    CATEGORY = 'Alper Katagori'
    
    def node_function(self, image):
        
        return (image, )
