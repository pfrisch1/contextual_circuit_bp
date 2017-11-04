"""2D sep convolutional model for Allen data."""

layer_structure = [
    {
        'layers': ['conv'],
        'weights': [32],
        'names': ['sep_conv1_1'],
        'filter_size': [5],
        'activation': ['selu'],
        'activation_target': ['post'],
    },
    {
        'layers': ['pool'],
        'weights': [None],
        'names': ['pool2'],
        'filter_size': [None]
    },
    {
        'layers': ['fc'],
        'weights': [64],
        'names': ['fc1'],
        'flatten': [True],
        'flatten_target': ['pre'],
        # 'dropout': [0.5],
        # 'dropout_target': ['post'],
        # 'regularization_type': ['l2'],
        # 'regularization_target': ['post'],
        # 'regularization_strength': [1e-7]
    }
]
