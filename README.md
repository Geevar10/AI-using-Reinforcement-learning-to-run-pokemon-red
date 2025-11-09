# Train RL Agents to Play Pokémon Red — Enhanced Edition 🎮🔥  
**By Geevar P Kocheril**  

This repository builds upon the original [PokemonRedExperiments](https://github.com/pwhiddy/pokemonredexperiments) project, extending its training framework to achieve **faster convergence**, **refined agent behavior**, and **improved exploration efficiency** using enhanced reinforcement learning (RL) techniques.

---

## 🚀 Overview

This project continues the work of training RL agents to play *Pokémon Red* autonomously using **Stable Baselines 3**, **PyBoy**, and a refined training setup.  
I have optimized and extended the **V2 training script** to improve the model’s learning speed, reduce memory usage, and enable longer, more stable runs — allowing the agent to progress further in the game world (up to Cerulean and beyond).

---

## ✨ My Improvements (Geevar’s Additions)

- ⚡ **Optimized training loop** — reduced overhead and improved episode management  
- 🧠 **Fine-tuned hyperparameters** — faster convergence and more stable reward curves  
- 🧭 **Refined exploration reward function** — smoother progression with coordinate-based incentives  
- 💾 **Checkpoint system** — enables easy resume and fine-tuning of pretrained weights  
- 📊 **Improved TensorBoard logging** — better visibility of episode rewards and frame rates  
- 🧩 **Optional broadcast streaming** — share progress globally using the built-in stream wrapper  
- 🔁 **Support for continuous training** — extend pretrained models seamlessly with new sessions  

---

## 🧱 Base Setup (Unchanged from Original)

Follow these steps to set up and run the environment.  
Python 3.10+ is recommended.

### 1️⃣ Prepare the ROM

Copy your legally obtained Pokémon Red ROM into the base directory and rename it:

```bash
PokemonRed.gb
```

Verify with:
```bash
shasum PokemonRed.gb
```
Expected SHA1:  
`ea9bcae617fdf159b045185467ae58b2e4a48b9a`

---

### 2️⃣ Install Dependencies

Move into the desired directory (V2 recommended):

```bash
cd v2
pip install -r requirements.txt
```

For MacOS:
```bash
pip install -r macos_requirements.txt
```

---

### 3️⃣ Run Pretrained Model Interactively

```bash
python run_pretrained_interactive.py
```

Controls:  
- Arrow Keys: Move  
- `A`: `a` key  
- `B`: `s` key  

Pause the AI by editing:
```
agent_enabled.txt
```

---

## 🧠 Training the Model — Enhanced V2

The enhanced V2 agent uses a **coordinate-based exploration reward**, **optimized PPO training**, and **refined frame handling** for better stability and learning.

### Run Training

```bash
python baseline_fast_v2.py
```

This version:
- Trains faster with reduced memory usage  
- Supports checkpoint saving and resume  
- Reaches farther game states  
- Streams to the live map by default  

---

## 🌍 Training Broadcast

Stream your local training session to a **shared global Pokémon map** using:

```python
env = StreamWrapper(
    env,
    stream_metadata = {
        "user": "Geevar_P_Kocheril",
        "env_id": "PokemonRed_Enhanced",
        "color": "#0077ff",
        "extra": "Training V2 Optimized Agent"
    }
)
```

View or host your broadcast:  
🔗 [https://github.com/pwhiddy/pokerl-map-viz/](https://github.com/pwhiddy/pokerl-map-viz/)

---

## 📈 Tracking Progress

Each training session logs:
- Frame captures  
- Model checkpoints  
- TensorBoard metrics  

Launch TensorBoard:

```bash
tensorboard --logdir .
```

Visit:  
👉 `http://localhost:6006`

Enable Weights & Biases logging by setting:
```python
use_wandb_logging = True
```

---

## 📊 Results and Observations

After fine-tuning, the enhanced agent:
- Achieves faster reward gain per frame  
- Navigates to Cerulean City more efficiently  
- Demonstrates smoother battle decision-making  
- Maintains higher stability during long sessions  

These improvements make training significantly more efficient and reproducible for further experimentation.

---

## 🧩 Supporting Libraries

- [PyBoy](https://github.com/Baekalfen/PyBoy) — Game Boy Emulator API  
- [Stable Baselines 3](https://github.com/DLR-RM/stable-baselines3) — RL Framework  
- [pokerl-map-viz](https://github.com/pwhiddy/pokerl-map-viz) — Multiplayer Visualization  

---

## 📜 Citation

If you build upon this work, please cite the original paper and this enhancement.

### Original Work:
[**Pokemon Red via Reinforcement Learning (2025)**](https://arxiv.org/abs/2502.19920)
```bibtex
@misc{pleines2025pokemon,
  title={Pokemon Red via Reinforcement Learning},
  author={Marco Pleines and Daniel Addis and David Rubinstein and Frank Zimmer and Mike Preuss and Peter Whidden},
  year={2025},
  eprint={2502.19920},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```

### Extended Work (Geevar P Kocheril, 2025)
> Enhanced training scripts and optimization for faster, more stable agent performance.

---
