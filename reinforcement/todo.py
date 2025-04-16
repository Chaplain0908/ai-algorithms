'''
算法：
bandit_theory.py	实现 ε-greedy、UCB、Thompson Sampling，供 MCTS 使用或独立测试	⭐⭐（高）
mcts.py	实现 MCTS 四阶段逻辑（Selection, Expansion, Simulation, Backpropagation），可选调用 Bandit 策略	⭐⭐⭐（最高）
value_iteration.py	基于 MDP 的确定性策略学习算法	⭐⭐（高）
q_learning.py	基础 Q-Learning 算法（表格版本）	⭐（可稍后）

problems:
tic_tac_toe_game.py	与 minimax 兼容的井字棋环境，支持 MCTS 使用（复用即可）	⭐⭐⭐（最高）
gridworld_env.py	MDP/Q-learning 用的简单格子环境（含状态空间、奖励、动作）	⭐⭐（中）

demo:
run_mcts_tictactoe.py	演示 MCTS 玩井字棋全过程，适合对比 Minimax/AlphaBeta	⭐⭐⭐（最高）
run_bandit_demo.py	多臂赌博机实验，展示各策略选择次数/奖励变化曲线	⭐⭐（高）
run_value_iteration.py	GridWorld + value iteration 策略评估与策略收敛展示	⭐（中）

visualize:
bandit_plot.py	绘制不同 Bandit 策略的选择次数与累积奖励曲线	⭐⭐（中）
policy_heatmap.py	用于展示 GridWorld 中 learned policy（箭头或颜色格）	⭐（可稍后）

第一批落地的六个文件：
算法	algorithms/bandit_theory.py
算法	algorithms/mcts.py
环境	problems/tic_tac_toe_game.py（复用）
Demo	demos/run_mcts_tictactoe.py
Demo	demos/run_bandit_demo.py
可视化	visualize/bandit_plot.py
'''