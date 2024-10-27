import pandas as pd
import json
import numpy as np
def write_data():
    df = pd.read_csv("Book1.csv")
    df = df.replace({np.nan:'None'})
    df_dict = df.to_dict(orient="records")
   

    with open("sim_data.json","w") as f:
        json.dump(df_dict,f,indent=4)
        
if __name__ == "__main__":
    write_data()