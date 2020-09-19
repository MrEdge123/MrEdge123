import jieba  #导入结巴分词库
import math   #导入数学库

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

    return up / (len1 * len2)

vec1 = {"我": 2, "昨天": 3, "今天": 1, "去": 1, "上学": 1, "跑步": 0}
vec2 = {"我": 0, "昨天": 0, "今天": 4, "去": 4, "上学": 2, "跑步": 0}

ans = cal_cos(vec1, vec2)
print(ans)