import jieba  #导入结巴分词库

#检查word是否为中文词语
def check_chinese(word) :
    if len(word) == 0 : return False

    for ch in word :
        if ch < '\u4e00' or ch > '\u9fa5' :  #中文字符范围
            return False
    
    return True

#根据words, 初始化词频向量的结构(字典形式)
def init_vec(words) : 
    vec = {}
    for word in words :
        if check_chinese(word) :
            vec[word] = 0
    return vec

words = ["我", "今天", "wo", "\n", "", "去", "上学", " "]
vec = init_vec(words)
for key in vec :
    print(key + ":", vec[key])