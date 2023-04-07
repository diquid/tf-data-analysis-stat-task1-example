import pandas as pd
import numpy as np


chat_id = 1234206085

def solution(x: np.array) -> float:
    return np.log(x - 451).mean()
