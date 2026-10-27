import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")
df = pd.read_csv('student_perfomance.csv')
# раскомментировать во всем, кроме последнего
# plt.figure(figsize=(10, 6))

# 1. Распределение часов сна
# sns.histplot(data=df, x='Sleep_Hours', color='skyblue', discrete=True, stat='count', alpha=0.6)
# counts = df['Sleep_Hours'].value_counts().sort_index()
# plt.plot(counts.index, counts.values, color='red', marker='o', linestyle='-', linewidth=2, label='Полигон частот')

# plt.title('Распределение часов сна (Полигон частот)', fontsize=14)
# plt.xlabel('Часы сна', fontsize=12)
# plt.ylabel('Количество студентов', fontsize=12)
# plt.legend()
# plt.show()

# 2. Постройте гистограмму распределения количества часов
# sns.histplot(data=df, x='Hours_Studied', hue='Gender', 
#              multiple='dodge', bins=15, kde=True, palette='Set2')

# plt.title('Распределение часов обучения среди мальчиков и девочек', fontsize=14)
# plt.xlabel('Количество часов обучения в неделю', fontsize=12)
# plt.ylabel('Количество студентов', fontsize=12)
# plt.grid(True, alpha=0.3)

# plt.show()

# 3. Как зависит результат конечного экзамена от результата первого экзамена
# sns.regplot(data=df, x='Previous_Scores', y='Exam_Score', 
#             scatter_kws={'color': 'blue'}, 
#             line_kws={'color': 'red'})

# plt.title('Зависимость конечного балла от первого экзамена', fontsize=14)
# plt.xlabel('Балл за первый экзамен (Previous_Scores)', fontsize=12)
# plt.ylabel('Балл за конечный экзамен (Exam_Score)', fontsize=12)
# plt.grid(True, alpha=0.3)

# plt.show()

# 4. Постройте box plot отображающий распределение количества сна детей
# df['Score_Category'] = df['Exam_Score'].apply(lambda x: 'Выше 85' if x > 85 else 'Ниже 85')
# sns.boxplot(data=df,
#     x='Score_Category',
#     y='Sleep_Hours',
#     hue='Score_Category',
#     palette='Set2', 
#     legend=False   )
# plt.title('Распределение часов сна в зависимости от балла за экзамен', fontsize=14)
# plt.xlabel('Результат экзамена', fontsize=12)
# plt.ylabel('Количество часов сна', fontsize=12)
# plt.grid(True, alpha=0.3)

# plt.show()

# 5. Правда ли, что количество посещаемых занятий
# с репетитором в месяц напрямую влияет на балл в конечном экзамене?
# sns.regplot(data=df, x='Tutoring_Sessions', y='Exam_Score', 
#             scatter_kws={'color': 'blue'},
#             line_kws={'color': 'red'})

# plt.title('Зависимость балла экзамена от занятий у репетитора', fontsize=14)
# plt.xlabel('Количество посещенных занятий', fontsize=12)
# plt.ylabel('Балл за экзамен', fontsize=12)
# plt.grid(True, alpha=0.3)

# plt.show()

# 6. Как физическая активность влияет на успеваемость
# mean_scores = df.groupby('Physical_Activity')['Exam_Score'].mean().reset_index()

# sns.lineplot(data=mean_scores, x='Physical_Activity', y='Exam_Score', 
#              marker='o', color='blue', linewidth=2, markersize=8)

# plt.title('Средний балл за экзамен в зависимости от физической активности', fontsize=14)
# plt.xlabel('Уровень физической активности', fontsize=12)
# plt.ylabel('Средний балл за экзамен', fontsize=12)
# plt.show()

# 7. Постройте HeatMap где ось X - процент посещаемость,
# Y - количество занятий с репетитором, а Z - балл за итоговый экзамен

# df['Attendance_Bin'] = pd.cut(df['Attendance'], 
#                               bins=[0, 60, 70, 80, 90, 100], 
#                               labels=['0-60%', '60-70%', '70-80%', '80-90%', '90-100%'])

# heatmap_data = df.pivot_table(index='Tutoring_Sessions', 
#                               columns='Attendance_Bin', 
#                               values='Exam_Score', 
#                               aggfunc='mean')

# plt.figure(figsize=(12, 8))

# sns.heatmap(data=heatmap_data, cmap='YlGnBu', annot=True, fmt='.1f',
#             linewidths=.5, cbar_kws={'label': 'Средний балл'})

# plt.title('Средний балл за экзамен в зависимости от посещаемости и занятий с репетитором', fontsize=14)
# plt.xlabel('Процент посещаемости', fontsize=12)
# plt.ylabel('Количество занятий с репетитором', fontsize=12)

# plt.show()