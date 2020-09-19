import jieba  #导入结巴分词库

#根据words, 生成词频向量vec
def gen_vec(words, vec) :
    for word in words :
        if (word in vec) :
            vec[word] = vec[word] + 1

words = ["我", " ", "\n", "去", "跑步", "我"]
vec = {"我": 0, "今天": 0, "去": 0, "上学": 0}

gen_vec(words, vec)
for key in vec :
    print(key + ":", vec[key])
