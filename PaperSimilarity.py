import jieba

str = "duibuqi, 今天我要去上课, keyi等ka一等ma"

print("/".join(jieba.cut(str)))
