import subprocess

class AhmetAlper:
    
    @classmethod
    def INPUT_TYPES(cls):
    
        return {
            
            'required' : {
                
                'image' : ('IMAGE', ),
                'codes': ('STRING', {'multiline' : True, 'default' : ''})
                
            }
            
        }
    
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'node_function'
    
    CATEGORY = 'Alper Category'
    
    def node_function(self, image, code):
        
        command = code.split(' ')
        
        print(command)
                
        try:
                        
            subprocess.run(command, check = True)
            
            print(f"successfully to")
            
        except Exception as exception:
            
            print(f'An error occurred while downloading the file: {exception}')
            
        finally:
            
            return (image, )
