import json;
import pandas as pd;
import os; 

def write(data, category, name):
    data = json.dumps(data);

    path = f'data/{category}';

    isExist = os.path.exists(path);
    if(not isExist): os.makedirs(path);
        
    with open(f'{path}/{name}.json', 'w') as file:
        file.write(data);
    
    df = pd.read_json(data);
    
    df.to_csv(f'{path}/{name}.csv');

    df.index = df.index.rename('no');
    df.index = df.index + 1;

    df.to_excel(f'{path}/{name}.xlsx');
    
    print(f'Result   : {path}\n');
