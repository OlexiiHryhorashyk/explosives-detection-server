image_endpoint_form = {
    'responses': {
        200: {
            'description': 'Explosives detection performed on uploaded image',
            'content': {
                'image/png': {
                    'schema': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }
        },
        400: {
            'description': 'No file part or no file selected '
        }
    },
    'parameters': [
        {
            'name': 'image',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Image file detect explosives on'
        }
    ],
    'tags': ['Image Detection']
}

video_endpoint_form = {
    'responses': {
        200: {
            'description': 'Video feed for explosives detection in real time',
            'content': {
                'multipart/x-mixed-replace': {
                    'schema': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }
        }
    },
    'tags': ['Video Detection']
}