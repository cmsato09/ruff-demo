import os
import json

def calculate_value(x, y):
    """Calculate a value."""
    z = x + y
    temp_value = x * 2
    return z

def process_data(data_list):
    results = []
    
    for i in range(len(data_list)):
        item = data_list[i]
        if item != None:
            results.append(item * 2)
    
    return results

process_data([1, 2, 3])
