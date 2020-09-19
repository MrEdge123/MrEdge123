import jieba  #导入结巴分词库

#检查word是否为中文词语
def check_chinese(word) :
    if len(word) == 0 : return False

    for ch in word :
        if ch < '\u4e00' or ch > '\u9fa5' :  #中文字符范围
            return False
    
    return True

words = ("", "wo", "我", "今天", "wo今天", "我jintian", "\n", ",,")

for word in words :
    print(word + ": " + ("True" if check_chinese(word) else "False"))
