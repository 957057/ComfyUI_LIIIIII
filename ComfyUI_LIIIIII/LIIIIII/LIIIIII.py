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
                "Path": ("STRING", {
                    "multiline": True
                }),
                "skip_line": ("INT", {
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
    RETURN_NAMES = ("path1", 'Int')
    RETURN_TYPES = ("STRING", "INT")
    FUNCTION = "LIIIIII_func"

    def LIIIIII_func(self, Path, skip_line):
        with open(os.path.normpath(Path), "r") as f:
            lines = f.readlines()[skip_line:]
            path1 = Path.replace('prompt', 'prompt1')
            with open(os.path.normpath(path1), "w") as ff:
                ff.writelines(lines)
        hs = random.random()
        # return {"ui": {"path1":(os.path.normpath(path),)}, "result": (os.path.normpath(path),)}
        return (path1, hs)

    @classmethod
    def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
        hs = random.random()
        
        return hs
