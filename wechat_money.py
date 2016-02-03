#========================================
# author: changlong.zang
#   mail: zclongpop@163.com
#   date: Tue, 02 Feb 2016, 18:16:16
#========================================
import random, itertools
#--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
def wechat_money(money=10.0, people=5):
    '''
    '''
    #-
    if people < 1:
        return list()

    if people * 0.01 > money:
        return list()

    #-
    indexs     = [i    for i in range(people)]
    money_list = [0.01 for i in range(people)]
    overage_m  = money - 0.01 * people

    #-
    random.shuffle(indexs)
    for i in itertools.cycle(indexs):
        if round(overage_m, 2) <= 0.0:
            break

        random_m = round(random.uniform(0.0, overage_m), 2)
        money_list[i] += random_m
        overage_m     -= random_m

    #-
    return money_list


if __name__ == "__main__":
    m_lst = wechat_money(10, 12)
    for i, x in enumerate(m_lst):
        print '第{0}个红包被领取：{1:>5} 剩余：{2}'.format(i+1, x, sum(m_lst[i+1:]))