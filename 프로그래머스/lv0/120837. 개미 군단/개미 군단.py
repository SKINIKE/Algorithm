def solution(hp):
    g_ant = divmod(hp, 5)
    s_ant = divmod(g_ant[1], 3)
    return g_ant[0] + s_ant[0] + s_ant[1]