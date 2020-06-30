# this is the function which takes your threshold (t1) and enemy threshold (t2) and the distribution based on a threshold
# it returns the probability of you winning
# this function by itself has linear runtime relative to the resolution


def p_win(t1, t2, dist):
    p_win = 0
    p_draw = 0
    p_less_than_now = 1
    for i in range(dist.res,t1,-1):
        p_less_than_now -= dist.get_dist(t2, i)
        p_draw += dist.get_dist(t1, i)*dist.get_dist(t2, i)        
        p_win += p_less_than_now * dist.get_dist(t1, i)
    p_draw +=dist.get_dist(t1, 0) * dist.get_dist(t2, 0)
    return p_win/(1-p_draw)
        
