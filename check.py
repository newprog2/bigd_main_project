import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "watchlist.csv"

watchlist_df = pd.read_csv(FILE_PATH, dtype={"code": str})
print(watchlist_df["code"].tolist())

plt.rcParams["font.family"] = "Malgun Gothic"

prices = [10000, 23000, 46000, 73000, 28000]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)

for i, p in enumerate(prices):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("내 첫 그래프")
fig.savefig("my_first_chart.png")
