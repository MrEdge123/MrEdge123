# 计算64位hash
def hash64(str) :
    return (hash(str) ** 2) % (1 << 64) 

# 计算vec的simhash
def simhash(vec) :
    cnt = [0] * 64
    for key in vec :
        val = hash64(key)
        pos = 0
        while val > 0 :
            if val & 1 : cnt[pos] += vec[key]
            else : cnt[pos] -= vec[key]
            val = val >> 1
            pos += 1
    
    pos = 0
    ans = 0
    while pos < 64 :
        ans = ans << 1
        if cnt[pos] > 0 : ans += 1
        pos += 1

    return ans

# 对比simhash
def cmp_simhash(simhash1, simhash2) :
    pos = 0
    diff = 0
    while pos < 64 :
        bit1 = simhash1 & 1
        bit2 = simhash2 & 1
        if bit1 != bit2 : diff += 1
        simhash1 = simhash1 >> 1
        simhash2 = simhash2 >> 1
        pos += 1
    
    return (64.0 - diff) / 64

if __name__ == "__main__" :
    vec1 = {"我": 1, "今天": 1, "去": 1, "上学": 1, "了": 1}
    vec2 = {"我": 1, "今天": 1, "去":1, "运动": 1, "1": 1, "小时": 1}

    simhash1 = simhash(vec1)
    simhash2 = simhash(vec2)

    print("{0:064b}".format(simhash1))
    print("{0:064b}".format(simhash2))

    print("{0:.2f}".format(cmp_simhash(simhash1, simhash2)))
