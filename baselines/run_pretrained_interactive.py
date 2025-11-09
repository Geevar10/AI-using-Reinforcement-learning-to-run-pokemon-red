# REMOVE all the gymnasium compatibility code and use simple imports
from os.path import exists
from pathlib import Path
import uuid
from red_gym_env import RedGymEnv
from stable_baselines3 import PPO
import numpy as np

if __name__ == '__main__':
    sess_path = Path(f'session_{str(uuid.uuid4())[:8]}')
    ep_length = 2**23

    env_config = {
        'headless': False,
        'save_final_state': True, 
        'early_stop': False,
        'action_freq': 24, 
        'init_state': 'has_pokedex_nballs.state',
        'max_steps': ep_length, 
        'print_rewards': True, 
        'save_video': False, 
        'fast_video': True, 
        'session_path': sess_path,
        'gb_path': 'PokemonRed.gb',
        'debug': False, 
        'sim_frame_dist': 2_000_000.0, 
        'extra_buttons': True
    }
    
    env = RedGymEnv(env_config)
    
    file_name = 'session_4da05e87_main_good/poke_439746560_steps'
    
    if exists(file_name + '.zip'):
        print('\nloading checkpoint')
        try:
            # Try loading with custom objects for compatibility
            model = PPO.load(file_name, env=env, custom_objects={
                'learning_rate': 0.0,
                'lr_schedule': lambda _: 0.0,
                'clip_range': lambda _: 0.0
            })
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Trying alternative loading method...")
            model = PPO.load(file_name, env=env)
    else:
        print(f"Model file not found: {file_name}")
        print("Running with random actions instead...")
        model = None
        
    obs, info = env.reset()
    
    while True:
        try:
            with open("agent_enabled.txt", "r") as f:
                agent_enabled = f.readlines()[0].startswith("yes")
        except:
            agent_enabled = False
            
        if agent_enabled and model is not None:
            action, _states = model.predict(obs, deterministic=False)
        else:
            action = 7  # pass action
            
        obs, rewards, terminated, truncated, info = env.step(action)
        env.render()
        
        if truncated or terminated:
            break
            
    env.close()