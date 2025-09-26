import os 
from app.domain.upload import config

def search_image(id):
    for name_image in os.listdir(config.UPLOAD_FOLDER):
        
        name = str(name_image)
        name = name.split('.')
        
        if f'album{id}' in name[0]:
            return name_image
        
    return 'default.png'

def delete_image(id):
    image = search_image(id)
    
    if image != 'default.png':
        os.remove(os.path.join(config.UPLOAD_FOLDER, image))

    