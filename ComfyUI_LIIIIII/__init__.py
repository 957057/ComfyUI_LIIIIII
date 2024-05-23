# 从py中引入一个类作为引用依据
# from py名称 import 类1，类2，类3
from .LIIIIII.LIIIIII import LIIIIII


# （必填）填写 import的类名称，命名需要唯一，key或value与其他插件冲突可能引用不了。这是决定是否能引用的关键。
# key(自定义):value(import的类名称)
NODE_CLASS_MAPPINGS = {
    # a000_example
    "LIIIIII": LIIIIII,

}


# （可不写）填写 ui界面显示名称，命名会显示在节点ui左上角，如不写会用类的名称显示在节点ui上
# key(自定义):value(ui显示的名称)
NODE_DISPLAY_NAME_MAPPINGS = {
    # a000_example
    "LIIIIII": "LIIIIII",

}


# 引入以上两个字典的内容
all = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']