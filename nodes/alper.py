import subprocess

class Alper:
    
    @classmethod
    def INPUT_TYPES(cls):
    
        return {
            
            'required' : {
                
                'image' : ('IMAGE', ),
                'civit_ai_model_url' : ('STRING', {'multiline' : False, 'default' : 'https://civitai.com/api/download/models/501240'}),
                'model_name' : ('STRING', {'multiline' : False, 'default' : 'realisticVisionV60B1_v51HyperVAE.safetensors'}),
                'model_path' : (['checkpoints'],)
                
            }
            
        }
    
    RETURN_TYPES = ('IMAGE', )
    
    FUNCTION = 'node_function'
    
    CATEGORY = 'Alper Category'
    
    def node_function(self, image, civit_ai_model_url, model_name, model_path):
        
        paths = {
            'checkpoints' : '/mnt/private/models/checkpoints'
        }
        
        model_path = paths[model_path]
        
        model_name = f'v1/{model_name}'
        
        try:
            
            command = ['aria2c', '--console-log-level=error', '-c', '-x', '16', '-s', '16', '-k', '1M', civit_ai_model_url, '-d', model_path, '-o', model_name]
            
            subprocess.run(command, check = True)
            
            print(f"File downloaded successfully to {model_path}/{model_name}")
            
        except Exception as exception:
            
            print(f'An error occurred while downloading the file: {exception}')
            
        finally:
            
            return (image, )
