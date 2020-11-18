import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(16,8))
sns.lineplot(x='iteration', y='train_episode_returns', hue='agent', data=experimental_data[GAME])
#sns.tsplot(data=experimental_data[GAME], time='iteration', unit='run_number', condition='agent', value='train_episode_returns', ax=ax)
plt.title(GAME)
plt.show()
