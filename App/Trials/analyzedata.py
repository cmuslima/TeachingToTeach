'''This file takes in data from the state selection experiment (importance advising)
and then returns the states that the agent selected as the important state'''
import pickle
from scipy.io import savemat


file= 'episode_0_user_99a012b9-6104-47a9-bf64-859ed55a1a5f'

def get_data(file):
    print('here')
    objects = []
    with (open(file, "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break

    SA_feedback_dict = dict() #this will store the feedback given at a specific state, and action pair
    S_feedback_dict = dict() #this will store the feedback given at a specific state
    for i in range(len(objects)):
        state = tuple(objects[i]['S'])
        action = objects[i]['A']
        reward = objects[i]['reward']
        temp = {(state, action): reward}
        SA_feedback_dict.update(temp)
        temp = {state: reward}
        S_feedback_dict.update(temp)
        
    return SA_feedback_dict,S_feedback_dict

def rewarded_states(feedback_dict): #this is a function which retreives the states where feedback was provided 
    keys = list(feedback_dict.keys())
    length = len(keys)
    states = list()
    for i in keys:
        if feedback_dict.get(i) != None:
            states.append(i)
    
    return states

SA_feedback_dict, S_feedback_dict = get_data(file)

states_w_feedback = rewarded_states(S_feedback_dict)

print(states_w_feedback)
