import jieba

str = "今天我要去上课"

print("/".join(jieba.cut(str)))
