import jieba  #导入结巴分词库

#检查word是否合法
def check(word) :
    if len(word) == 0 : return False

    ok = True
    for ch in word :
        if ch >= '\u4e00' and ch <= '\u9fa5' : ok = True #中文字符范围
        elif ch >= 'a' and ch <= 'z' : ok = True
        elif ch >= 'A' and ch <= 'Z' : ok = True
        elif ch >= '0' and ch <= '9' : ok = True
        else : return False

    return True

#根据words, 生成词频向量vec
def gen_vec(words) :
    vec = {}
    for key in words :
        if check(key) : vec[key] = 1

    return vec

if __name__ == "__main__" :
    words = ["我", " ", "\n", "去", "跑步", "我"]

    vec = gen_vec(words)
    for key in vec :
        print(key + ":", vec[key])