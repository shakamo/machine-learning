domains = {
    'xgboosting': [
        {'name': 'eta', 'type': 'continuous', 'domain': (0.01, 0.3)},
        {'name': 'min_child_weigh', 'type': 'continuous', 'domain': (1, 10)},
        {'name': 'max_depth', 'type': 'continuous', 'domain': (3, 10)},
        {'name': 'gamma', 'type': 'continuous', 'domain': (0, 0.5)},
        {'name': 'subsample', 'type': 'continuous', 'domain': (0, 1)},
        {'name': 'colsample_bytree', 'type': 'continuous', 'domain': (0.5, 1)},
        {'name': 'n_estimators', 'type': 'continuous', 'domain': (100, 5000)},
        {'name': 'learning_rate', 'type': 'continuous', 'domain': (0.001, 0.3)}
    ],
    'xgboosting2': [
        {'name': 'eta', 'type': 'continuous', 'domain': (0.01, 0.3)},
        {'name': 'learning_rate', 'type': 'continuous', 'domain': (0.001, 0.3)}
    ],
    'xgboosting3': [
        {'name': 'eta', 'type': 'continuous', 'domain': (0.01, 0.3)},
        {'name': 'learning_rate', 'type': 'continuous', 'domain': (0.001, 0.3)},
        {'name': 'max_depth', 'type': 'continuous', 'domain': (3, 10)},
    ],
    'rbf': [
        {'name': 'C', 'type': 'continuous', 'domain': (1, 1100)},
        {'name': 'gamma', 'type': 'continuous', 'domain': (0.00005, 0.0015)}
    ],
    'linear': [
        {'name': 'learning_rate', 'type': 'continuous', 'domain': (0.00005, 0.1)},
    ]
}