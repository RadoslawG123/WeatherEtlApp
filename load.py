import pandas as pd

def load(data, fileName):
    df = pd.DataFrame(data)
    df.to_csv(fileName, index=False)