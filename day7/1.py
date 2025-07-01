import pandas as pd
import numpy as np
data = {"col1":[3, np.nan,np.nan,2],"col2":[1.0,pd.NA,pd.NA,2.0]}
df = pd.DataFrame(data)
print(df)