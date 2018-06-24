import lib.puzzle as game
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

size = 2
episode = 1000
maxMove = 100 * size * size
Qtable = pd.DataFrame(columns=list(range(4)), dtype=np.float64)
learningRate = 0.05
gamma = 0.8
epsilon = 0.8

plt.ylabel('Steps')
plt.xlabel('Timesteps')
plt.title('Tearning curve')
seg = episode / 100

count = np.zeros(seg)

def frameListToString(frame):
    return ''.join(str(i) for i in frame)

def frameStringToList(frame):
    f = list()
    for i in range(0, len(frame)):
        f.append(int(frame[i]))
    return f

def checkExist(frame_):
    if frame_ not in Qtable.index:
        Qtable.loc[frame_] = [0 for n in range(4)]

def qLearn(frame_, action, reward):
    checkExist(frame_)
    predict = Qtable.loc[frame_, action]
    if game.isSolved(frameStringToList(frame)):
        target = reward
    else:
        target = reward + gamma * Qtable.loc[frame_, :].max()
    Qtable.loc[frame_, action] += learningRate * (target - predict)

def qAction(frame):
    checkExist(frameListToString(frame))
    if np.random.uniform() < epsilon:
        frame_ = frame_ = frameListToString(frame)
        stateAction = Qtable.loc[frame_, :]
        stateAction = stateAction.reindex(np.random.permutation(stateAction.index))
        action = stateAction.idxmax()
    else:
        action = np.random.randint(0, 4)
    while not game.movable(frame, action):
        qLearn(frameListToString(frame), action, -99)
        action = np.random.randint(0, 4)
    return action

if __name__ == "__main__":
    for e in range(episode):
        frame = game.createPuzzle(size)
        step = 0
        hisFrame = list()
        hisAction = list()
        while not game.isSolved(frame) and step < maxMove:
            step += 1
            action = qAction(frame)
            frame_ = frameListToString(frame)
            hisFrame.append(frame_)
            hisAction.append(action)
            frame = game.movePuzzle(frame, action)
        for i in range(0, len(hisFrame)):
            qLearn(hisFrame[i], hisAction[i], (maxMove - step))
        print("episode", e, " / ", episode, ',step : ', step)
        if e % seg == seg - 1:
            plt.plot(e + 1, np.average(count), 'r.')
        count[e % seg] = step
    print(Qtable)
plt.show()



