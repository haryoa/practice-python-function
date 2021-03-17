from typing import List, Tuple
import pandas as pd


def load_all_annotation() -> Tuple[List[str], List[str], List[str]]:
    """
    Load semua anotasi yang ada pada file `anotasi_latihan.csv`
    Working Directory Kamu harus berada pada foldernya untuk bisa menggunakan ini.
    
    Returns
    -------
    Tuple[List[str], List[str], List[str]]
        Return tuple berupa anotasi original, anotasi aji, dan anotasi ridho
    """
    df = pd.read_csv("anotasi_latihan.csv")
    return df.ori.tolist(), df.aji.tolist(), df.ridho.tolist()
