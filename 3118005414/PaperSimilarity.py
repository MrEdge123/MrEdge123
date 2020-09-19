import jieba  #导入结巴分词库

'''
需要写的函数: return_type funtion(type:parameter)

bool check_chinese(str:word) : 检查word是否为中文词语
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



org_paper = "我今天要去上学"
chk_paper = "我昨天跑步了"

text = org_paper + chk_paper
