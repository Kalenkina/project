import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cleaned_activities.csv')

#1
# counts = df['action_type'].value_counts()
#
# plt.figure(figsize=(7,5))
# counts.plot(kind='bar')
#
# plt.title('Activity Distribution')
# plt.tight_layout()
#
# plt.savefig('activity_distribution.png')
# plt.show()

#2
# df['timestamp'] = pd.to_datetime(df['timestamp'])
#
# dau = (
#     df.groupby(df['timestamp'].dt.date)
#     ['user_id']
#     .nunique()
# )
#
# plt.figure(figsize=(10,5))
# plt.plot(dau.index, dau.values)
#
# plt.title('Daily Active Users')
# plt.xticks(rotation=45)
#
# plt.tight_layout()
# plt.savefig('dau.png')
# plt.show()

#3
df['timestamp'] = pd.to_datetime(df['timestamp'])

df['weekday'] = df['timestamp'].dt.day_name()
df['hour'] = df['timestamp'].dt.hour

heat = pd.crosstab(
    df['weekday'],
    df['hour']
)

plt.figure(figsize=(12,6))
sns.heatmap(heat)

plt.title('Activity Heatmap')
plt.tight_layout()

plt.savefig('heatmap.png')
plt.show()