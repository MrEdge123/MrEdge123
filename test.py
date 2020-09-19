import jieba

org_paper = "wa我d今天要\nsf 去上学dd"

seq = jieba.cut(org_paper)

for word in seq :
    for i in range(len(word)) :
        if word[i] >= '\u4e00' and word[i] <= '\u9fa5' :
            print(word[i], end=" ")
    print("")
