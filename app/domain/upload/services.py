import os 
from app.domain.upload import config

def search_image(id):
    for name_image in os.listdir(config.UPLOAD_FOLDER):
        
        name = str(name_image)
        name = name.split('.')
        
        if name[0] == f'album{id}':
            return name_image
        
    return 'default.png'

    