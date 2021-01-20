from datetime import datetime as dt
import os
import pandas as pd
import glob
import zipfile
import numpy as np


class Outgassing:
    def __init__(self, Path):
        self.Path = Path
        self.ZipDir = self.Path+'RGA/'
        self.File = glob.glob(self.Path+'*.h5')[0]
    
    def OpenH5(self): 
        self.Data = {}
        self.Data['RGA'] = pd.read_hdf(self.File, key='RGA')
        self.Data['Temp'] = pd.read_hdf(self.File, key='Temp')



# if __name__ == "__main__":
    # Path = '/project/david_moore/aj487/Data_WL110/Outgassing_Setup/20201014/'
    # IO = DataIO(Path)
    # IO.Unzip()
    # Data = IO.GetRGAData(Size=100)
    # Temp = IO.GetTemperatureData()