import jieba  #导入结巴分词库

'''
需要写的模块: return_type module(type:parameter)

bool check_chinese(str:word) : 检查word是否为中文词语
dict init_vec(list:words) : 根据words, 初始化词频向量的结构(字典形式)
dict gen_vec(list:words) : 根据words, 生成词频向量
num cal_cos(dict:vec1, dict:vec2) : 计算vec1和vec2的余弦相似度

'''

org_paper = "我今天要去上学"
chk_paper = "我昨天跑步了"

text = org_paper + chk_paper
