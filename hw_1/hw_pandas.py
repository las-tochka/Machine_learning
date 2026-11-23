import pandas as pd

df = pd.read_csv('student_performance.csv')

# 1. Среднее кол-во времени, выделяемое на сон студентами
mean_sleep = df['Sleep_Hours'].mean()
print(f"Среднее количество часов на сон: {mean_sleep:.2f}")

# 2. Внеклассные активности студентов, процент
count_yes = (df['Extracurricular_Activities'] == 'Yes').sum()

total_students = len(df)
percentage = (count_yes / total_students) * 100
print(f"Процент студентов с активностями: {percentage:.2f}%")

# 3. Экзамены и гендерное неравенство
mean_scores = df.groupby('Gender')['Exam_Score'].mean()
# print(mean_scores)
if mean_scores.get('Female', 0) > mean_scores.get('Male', 0):
    print("Ответ: Да, в среднем девушки сдают экзамены лучше.")
else:
    print("Ответ: Нет, в среднем мужчины сдают экзамены не хуже (или лучше).")

# 4. 75 и 25 перцентили времени сна
q25 = df['Sleep_Hours'].quantile(0.25)
q75 = df['Sleep_Hours'].quantile(0.75)
print(f"25-й перцентиль (Q1): {q25}")
print(f"75-й перцентиль (Q3): {q75}")

# 5. Правда ли, что те, кто спит больше (75 перцентиль и выше)
# сдает экзамен лучше, чем студенты с недосыпом (25 перцентиль и меньше)
q75 = df['Sleep_Hours'].quantile(0.75)
q75_mean = df[df['Sleep_Hours'] >= q75]['Exam_Score'].mean()
q25 = df['Sleep_Hours'].quantile(0.25)
q25_mean = df[df['Sleep_Hours'] <= q25]['Exam_Score'].mean()
if q25_mean < q75_mean:
    print("Ответ: Да, в среднем люди с недосыпом сдают экзамены хуже.")
else:
    print("Ответ: Нет, в среднем высыпающиеся люди не сдают экзамены лучше")

# 6. Влияет ли физическая акичвность на экзамен?
mean_scores = df.groupby('Physical_Activity')['Exam_Score'].mean()
print(mean_scores)
best_pair = max(mean_scores.items(), key=lambda x: x[1])
print(f"Лучшая активность: {best_pair[0]}, балл: {best_pair[1]:.2f}")

# 7. Влияние образоования родителей
mean_scores = df.groupby('Parental_Education_Level')['Exam_Score'].mean()
sorted_mean_scores = sorted(mean_scores.items(), key=lambda x: x[1])
# print(sorted_mean_scores, '\n',  mean_scores)
checked_val = ['Postgraduate', 'College']
if sorted_mean_scores[-1][0] in checked_val and sorted_mean_scores[-2][0] in checked_val:
    print("Да, образование родителей влияет на оценки")
else:
    print("Нет, образование родителей не влияет на оценки")

# 8. Влияние участия родителей
mean_scores = df.groupby('Parental_Involvement')['Exam_Score'].mean()
sorted_mean_scores = sorted(mean_scores.items(), key=lambda x: x[1])
for level, score in sorted_mean_scores:
    print(f'Люди с уровнем {level} учестия родителей в среднеи получили такую {score} оценку')

# 9. "Доход решает :)"
mean_scores = df.groupby('Family_Income')['Exam_Score'].mean()
high_score = mean_scores.get('High', 0)
other_scores = mean_scores.drop('High', errors='ignore').mean()
if high_score > other_scores:
    print("Да, доход решает")
else:
    print("Нет, упорство важнее")

# Сдать без денег и интернета
target_students = df[(df['Family_Income'] == 'Low') & (df['Internet_Access'] == 'No')]
passed = (target_students['Exam_Score'] > 70).sum()
total = len(target_students)
share = (passed / total) * 100
print(f"Всего студентов Low + No Internet: {total}")
print(f"Из них сдали > 70: {passed}")
print(f"Доля: {share:.2f}%")