import math

import pandas as pd
import json
import os
import random
# 动态获取路径
dir = os.path.dirname(__file__) # 当前脚本目录
last1 = os.path.basename(dir) # 最后一个目录
last2 = os.path.basename(os.path.dirname(dir)) # 倒数第二个目录
gategory=f"{last2}👾👾👾/{last1}" # 动态获取的当前文件夹路径
class LIIIIII:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "path": ("STRING", {
                    "multiline": True,
                    "default": "Hello World!"
                }),
                "skip_line": ("INT", {
                    "default": 0,
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
            },
        }

    CATEGORY = gategory
    OUTPUT_NODE = True
    # INPUT_IS_LIST = True
    RETURN_NAMES = ("text",)
    RETURN_TYPES = ("INT",)
    FUNCTION = "LIIIIII_func"

    def LIIIIII_func(self, path, skip_line):
        with open(os.path.normpath(path), "r") as f:
            lines = f.readlines()[skip_line:]
            path = path.replace('prompt', 'prompt1')
            with open(os.path.normpath(path), "w") as ff:
                ff.writelines(lines)
        hs = random.random()
        return (hs,)


