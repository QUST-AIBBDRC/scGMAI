import numpy as np
from ZIFA import ZIFA
from ZIFA import block_ZIFA
import pandas as pd

table = np.array(X_test_reconstruct)
Z, model_params = block_ZIFA.fitModel(table, 5)
np.savetxt('output_ZIFA.csv', Z, fmt='%.2f')
