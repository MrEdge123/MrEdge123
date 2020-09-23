import jieba          # 导入结巴模块
import sys            # 导入命令行参数模块

# 导入自定义模块
from module.gen_vec import gen_vec
from module.simhash import simhash
from module.simhash import cmp_simhash

'''

dict init_vec(list:words) : 根据words, 初始化词频向量的结构(字典形式)
void gen_vec(list:words, dict:vec) : 根据words, 生成词频向量vec
num simhash(dict:vec) : 根据vec, 计算simhash签名
num cmp_simhash(num:simhash1, num:simhash2) : 计算simhash1和simhash2的海明距离

'''

# 主函数
def main() :
    org_file = open(sys.argv[1], "r", encoding="utf-8")
    chk_file = open(sys.argv[2], "r", encoding="utf-8")
    out_file = open(sys.argv[3], "w", encoding="utf-8")

    org_paper = org_file.read()
    chk_paper = chk_file.read()

    # 得到词频向量
    vec1 = gen_vec(jieba.lcut(org_paper, cut_all=True))
    vec2 = gen_vec(jieba.lcut(chk_paper, cut_all=True))

    # 计算simhash签名
    simhash1 = simhash(vec1)
    simhash2 = simhash(vec2)

    print("{0:064b}".format(simhash1))    
    print("{0:064b}".format(simhash2))

    # 计算相似度
    ans = cmp_simhash(simhash1, simhash2)

    print("similarity:{0:.2f}".format(ans))
    out_file.write("{0:.2f}".format(ans))

    org_file.close()
    chk_file.close()
    out_file.close()

main()
