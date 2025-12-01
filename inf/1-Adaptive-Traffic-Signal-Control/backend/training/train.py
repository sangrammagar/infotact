# Minimal training loop skeleton for DQN -- uses synthetic data for demo.
import numpy as np
from dqn import build_dqn

def synthetic_env_step(state, action):
    # simple random transition for demo
    next_state = np.clip(state + np.random.randint(-2,3,size=state.shape), 0, 50)
    reward = -next_state.sum()  # lower sum is better
    done = False
    return next_state, reward, done

def main():
    state_dim = 5
    action_dim = 2
    model = build_dqn(state_dim, action_dim)
    state = np.zeros(state_dim)
    for step in range(100):
        q = model.predict(state.reshape(1,-1), verbose=0)[0]
        action = int(np.argmax(q))
        next_state, reward, done = synthetic_env_step(state, action)
        # placeholder training call
        target = q
        target[action] = reward
        model.fit(state.reshape(1,-1), target.reshape(1,-1), epochs=1, verbose=0)
        state = next_state
    model.save('dqn_model.h5')
    print('Training complete (demo).')

if __name__ == '__main__':
    main()
