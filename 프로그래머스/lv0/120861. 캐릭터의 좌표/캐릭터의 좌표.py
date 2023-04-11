def solution(keyinput, board):
    bx = board[0] // 2
    by = board[1] // 2
    player = [0, 0]

    for i in keyinput:
        if i == "left" and player[0] != -bx:
            player = [x+y for x,y in zip(player, [-1, 0])]
        elif i == "right" and player[0] != bx:
            player = [x+y for x,y in zip(player, [1, 0])]
        elif i == "up" and player[1] != by:
            player = [x+y for x,y in zip(player, [0, 1])]
        elif i == "down" and player[1] != -by:
            player = [x+y for x,y in zip(player, [0, -1])]
    return player