#To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

def open_or_senior(data):
    answer = []
    for person in data:
        if person[0]>=55 and person[1]>7:
            answer.append("Senior")
        else:
            answer.append("Open")
    return answer
