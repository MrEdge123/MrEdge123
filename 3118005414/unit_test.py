import jieba  #导入结巴分词库

#检查word是否为中文词语
def check_chinese(word) :
    if len(word) == 0 : return False

    for ch in word :
        if ch < '\u4e00' or ch > '\u9fa5' :
            return False
    
    return True

