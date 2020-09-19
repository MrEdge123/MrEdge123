import jieba  #导入结巴分词库

#根据words, 初始化词频向量的结构(字典形式)
def init_vec(words) : 
    vec = {}
    for word in words :
        vec[word] = 0
    return vec

words = ["我", "今天", "去", "上学"]
vec = init_vec(words)
for key in vec :
    print(key + ":", vec[key])