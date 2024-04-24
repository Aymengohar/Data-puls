import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('student performance.csv')
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df['reading_score'].corr(df['writing_score']))
print(df.describe())
# calculate the total test_prepration_course
total_math_score = df['math_score'].sum()
print("Total_Math_Score:",total_math_score)
# calculate average reading score
avg_reading_score = df['reading_score'].mean()
# filter data for writing score
product_a_data = df[df['reading_score'] =='writing_score']
print("Data for writing_score:")

print(product_a_data)
# plot a bar graph of score
product_score = df.groupby('race_ethnicity')['reading_score'].mean()
product_score.plot(kind='bar',rot=0,color='red')
plt.title('average reading_score by ethnicity')
plt.xlabel('race_ethnicity')
plt.ylabel('reading_score')
plt.grid(True)
plt.show()
# plot the scatter graph
plt.figure(figsize=(8,6))
plt.scatter(df['reading_score'],df['writing_score'],color='red',marker='o')
plt.title('average reading writing score')
plt.xlabel('reading_score')
plt.ylabel('writing_score')
plt.grid(True)
plt.show()
plt.figure(figsize=(8,6))
plt.scatter(df['race_ethnicity'],df['writing_score'],color='red',marker='o')
plt.title('average writing_score by ethnicity')
plt.xlabel('race_ethnicity')
plt.ylabel('writing_score')
plt.grid(True)
plt.show()
# plot a bar graph of score
product_score = df.groupby('race_ethnicity')['reading_score']
product_score.plot(kind='bar',rot=0,color='red')
plt.title('manually reading_scores by ethnicity')
plt.xlabel('race_ethnicity')
plt.ylabel('reading_score')
plt.grid(True)
plt.show()
