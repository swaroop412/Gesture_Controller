def fingers_up(lm):
    tips = [8, 12, 16, 20]
    return [lm[t].y < lm[t - 2].y for t in tips]

def detect_gesture(lm):
    fingers = fingers_up(lm)
    count = fingers.count(True)

    if fingers == [True, False, False, True]:
        return "ROCK"
    if fingers == [False, False, False, True]:
        return "PINKY"

    if count == 0:
        return "FIST"
    if count == 1:
        return "INDEX"
    if count == 2:
        return "TWO"
    if count == 3:
        return "THREE"
    if count == 4:
        return "FOUR"

    return None