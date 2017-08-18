

layer_structure = [
    {
        'layers': ['conv'],
        'weights': [64],
        'names': ['conv1_1'],
        'filter_size': [3],
        'activation': ['relu'],
        'activation_target': ['post'],
        'wd_target': ['pre'],
        'wd_type': [None],
    },
    {
        'layers': ['pool'],
        'weights': [None],
        'names': ['pool1'],
        'filter_size': [None]
    },
    {
        'layers': ['conv'],
        'weights': [64],
        'names': ['conv2_1'],
        'filter_size': [3],
        'normalization': ['lrn'],
        'normalization_target': ['post'],
        'activation': ['relu'],
        'activation_target': ['post'],
        'wd_target': ['pre'],
        'wd_type': [None],
    },
    {
        'layers': ['pool'],
        'weights': [None],
        'names': ['pool2'],
        'filter_size': [None]
    }
]