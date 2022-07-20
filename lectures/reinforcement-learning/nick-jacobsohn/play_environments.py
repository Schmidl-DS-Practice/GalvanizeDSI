import gym
import numpy as np
from IPython import display
import matplotlib.pyplot as plt
from gym.wrappers import Monitor
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
import matplotlib as mpl
plt.style.use("ggplot") # always make it pretty
mpl.rcParams['font.size'] = 16 # Frank was here
mpl.rcParams['figure.figsize'] = 10, 8

def play_discrete_epsgreedy_qlearning(env, num_episodes=150):
    """
    This is a basic function to play any gym environment that has a Discrete Observation Space
    The NN defined in here is super basic and is very likely bad out of the box (purposeful!)
    With some environments, a NN isn't even the right way to go. Think about your environments
    and their reward/done conditions to build somehting!
    """
    num_actions = env.action_space.n
    num_states = env.observation_space.n
    
    # create matrix of model-interpretable states
    obs_states = np.identity(num_states)
    
    # create the model
    model = Sequential()
    model.add(InputLayer(batch_input_shape=(1, num_states)))
    model.add(Dense(10, activation='tanh'))
    model.add(Dense(num_actions, activation='softmax'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    # now execute the q learning
    gamma = 0.95
    eps = 0.5
    decay_factor = 0.999
    r_avg_list = []
    for i in range(num_episodes):
        obs = env.reset()
        eps *= decay_factor
        if i % 25 == 0:
            print("Episode {} of {}".format(i, num_episodes))
        done = False
        reward_sum = 0
        while not done: 
            action = np.argmax(model.predict(obs_states[obs:obs + 1]))
            new_obs, reward, done, _ = env.step(action)
            target_q = reward + gamma * np.max(model.predict(obs_states[new_obs:new_obs + 1]))
            target_vec = model.predict(obs_states[obs:obs + 1])[0]
            target_vec[action] = target_q
            model.fit(obs_states[obs:obs + 1], target_vec.reshape(-1, num_actions), epochs=5, verbose=0)
            obs = new_obs
            reward_sum += reward
        r_avg_list.append(reward_sum)
    r_avg_list = np.array(r_avg_list)
    
    # The % successful episodes only makes sense for frozenlake!
    x = np.cumsum(r_avg_list)
    x = x/np.arange(1, num_episodes+1, 1)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x)
    ax.set_ylabel('% Sucessful Episodes') 
    ax.set_xlabel('Number of Episodes')
    plt.savefig("discrete_performance.png")
    
def play_box_epsgreedy_qlearning(env, num_episodes=150):
    """
    This is a basic function to play any gym environment that has a Box Observation Space
    The NN defined in here is super basic and is very likely bad out of the box (purposeful!)
    With some environments, a NN isn't even the right way to go. Think about your environments
    and their reward/done conditions to build somehting!
    """
    num_actions = env.action_space.n
    shape_states = env.observation_space.shape
    num_states = env.observation_space.shape[0]
    
    # create matrix of model-interpretable states
    obs_states = np.identity(num_states)
    
    # create the model
    model = Sequential()
    model.add(InputLayer(batch_input_shape=(1, num_states)))
    model.add(Dense(10, activation='tanh'))
    model.add(Dense(num_actions, activation='softmax'))
    model.compile(loss='mse', optimizer='adam', metrics=['mae'])
    # now execute the q learning
    gamma = 0.95
    eps = 0.5
    decay_factor = 0.999
    r_avg_list = []
    for i in range(num_episodes):
        obs = env.reset()
        eps *= decay_factor
        if i % 25 == 0:
            print("Episode {} of {}".format(i, num_episodes))
        done = False
        reward_sum = 0
        while not done: 
            obs = obs.reshape(1, -1)
            action = np.argmax(model.predict(obs))
            new_obs, reward, done, _ = env.step(action)
            new_obs = new_obs.reshape(1, -1)
            target_q = reward + gamma * np.max(model.predict(new_obs))
            target_vec = model.predict(obs)[0]
            target_vec[action] = target_q
            model.fit(obs, target_vec.reshape(-1, num_actions), epochs=5, verbose=0)
            obs = new_obs
            reward_sum += reward
        r_avg_list.append(reward_sum)
    r_avg_list = np.array(r_avg_list)
    x = r_avg_list
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(x)
    ax.set_ylabel('Reward Per Episode')
    ax.set_xlabel('Number of Episodes')
    plt.savefig("box_performance.png")
    
if __name__ == "__main__":
    frozenlake = gym.make("FrozenLake-v0") #discrete observation space
    cartpole = gym.make("CartPole-v1") #box observation space
    play_discrete_epsgreedy_qlearning(frozenlake, num_episodes=100)
    play_box_epsgreedy_qlearning(cartpole, num_episodes=100)