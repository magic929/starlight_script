import json
import numpy as np
import sys

def kill_boss_team(boss, damages, ids):
    n = len(damages)
    state = np.zeros((n+1, boss+1))
    dp = np.zeros(boss+1)

    for i, value in enumerate(damages):
        for j in range(boss, value - 1, -1):
            tmp = dp[j - value] + value
            if tmp > dp[j]:
                dp[j] = tmp
                state[i][j] = 1
    
    print(state)
    print(dp)
    result = []
    j = boss
    for i in range(n, -1, -1):
        if state[i][j] == 1:
            result.append(ids[i])
            j = j - damages[i]
    
    return result


def load_json(file):
    with open(file, 'r', encoding='utf8') as f:
        data = json.load(f)
    
    boss = data['boss']
    damages, ids = [], []
    for item in data['team']:
        damages.append(item['damage'])
        ids.append(item['id'])
    
    return boss, damages, ids



if __name__ == "__main__":
    boss, damages, ids = load_json(sys.argv[1])
    result = kill_boss_team(boss, damages, ids)
    print(result)
