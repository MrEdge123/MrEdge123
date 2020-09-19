import jieba  #导入结巴分词库

'''
需要写的函数: return_type funtion(type:parameter)

dict init_vec(list:words) : 根据words, 初始化词频向量的结构(字典形式)
void gen_vec(list:words, dict:vec) : 根据words, 生成词频向量vec
num cal_cos(dict:vec1, dict:vec2) : 计算vec1和vec2的余弦相似度

'''

org_paper = "我今天要去上学"
chk_paper = "我昨天跑步了"

text = org_paper + chk_paper
