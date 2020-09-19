import jieba  #导入结巴分词库
import math   #导入数学库

'''
需要写的函数: return_type funtion(type:parameter)

dict init_vec(list:words) : 根据words, 初始化词频向量的结构(字典形式)
void gen_vec(list:words, dict:vec) : 根据words, 生成词频向量vec
num cal_cos(dict:vec1, dict:vec2) : 计算vec1和vec2的余弦相似度

'''

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

#根据words, 生成词频向量vec
def gen_vec(words, vec) :
    for word in words :
        if (word in vec) :
            vec[word] = vec[word] + 1

#计算vec的长度
def cal_len(vec) :
    ans = 0
    for key in vec :
        ans += vec[key] * vec[key]
    return math.sqrt(ans)

#计算vec1和vec2的余弦相似度
def cal_cos(vec1, vec2) :
    up = 0
    for key in vec1 :
        up += vec1[key] * vec2[key]
    
    len1 = cal_len(vec1)
    len2 = cal_len(vec2)

    if len1 == 0 or len2 == 0 : return 0

    return up / (len1 * len2)

'''

dict init_vec(list:words) : 根据words, 初始化词频向量的结构(字典形式)
void gen_vec(list:words, dict:vec) : 根据words, 生成词频向量vec
num cal_cos(dict:vec1, dict:vec2) : 计算vec1和vec2的余弦相似度

'''

org_paper = "我今天要去上学"
chk_paper = "我昨天跑步了"

text = org_paper + chk_paper

vec_struct = init_vec(jieba.cut(text))

vec1 = vec_struct.copy()
vec2 = vec_struct.copy()
gen_vec(jieba.cut(org_paper), vec1)
gen_vec(jieba.cut(chk_paper), vec2)

for key in vec1 :
    print(key + ":" + repr(vec1[key]) + " " + repr(vec2[key]))

ans = cal_cos(vec1, vec2)

print("similarity:" + repr(ans))