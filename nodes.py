import subprocess
import requests
import os

class Console:
    
    def __init__(self):
        
        print('init')
    
    @classmethod
    def INPUT_TYPES(s):
        
        return {
            
            'required': {
                
                'image' : ('IMAGE',),
                'run': (['enabled', 'disabled'],),
                'civit_ai_model_url' : ('STRING', {'multiline' : False, 'default' : 'https://civitai.com/api/download/models/501240'}),
                'civit_ai_model_name' : ('STRING', {'multiline' : False, 'default' : 'realisticVisionV60B1_v51HyperVAEeeee.safetensors'}),
                'civit_ai_model_path' : ('STRING', {'multiline' : False, 'default' : 'models/checkpoints'})
                             
            }
            
        }
        
    RETURN_TYPES = ('IMAGE',)
    
    FUNCTION = 'execute'
    
    CATEGORY = 'Alper Category'
    
    def execute(self, image, run, civit_ai_model_url, civit_ai_model_name, civit_ai_model_path):
                
        if run == 'enabled':
                            
            print('Downloading ...')
            
            response = requests.get(civit_ai_model_url, stream = True)

            if response.status_code == 200:
                
                path = os.path.abspath(f'{civit_ai_model_path}/{civit_ai_model_name}')
                
                print(path)
                
                with open(path, 'wb') as file:
                    
                    for chunk in response.iter_content(1024):
                        
                        file.write(chunk)
        
        return (image, )
