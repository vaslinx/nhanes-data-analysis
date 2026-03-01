# NHANES Data Analysis Project
# Full data preparation, cleaning, visualization and EDA
# ------------------------------------------------------

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# -----------------------------------------
# 1. Load dataset
# -----------------------------------------
df = pd.read_csv("hanes_clean.csv")
print(df)
# 2. BMI calculation
# -----------------------------------------
df["BMI"] = df["Weight"] / (df["Height"] / 100) ** 2
# 3. Age Groups
# -----------------------------------------
bins = [0, 17, 40, 60, 80, 200]
labels = ["0-17 (child)", "18-40 (young)", "41-60 (adult)", "61-80 (senior)", "81+ (elder)"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True)
# -----------------------------------------
# 4. Summary Statistics
df=pd.read_csv('nhanes_clean.csv')

table_gender=df.groupby('Gender')[['Height', 'Weight']].mean()
print("average hifht and weight by gender:")
print(table_gender)

table_age = df.groupby('AgeGroup')[['Height', 'Weight']].mean()
print("\naverage hight and weeight by age:")
print(table_age)

table_min_max= df[['Height', 'Weight']].agg(['min','max'])
print("\nmin and max hight and weight:")
print(table_min_max)

age_counts=df['AgeGroup'].value_counts()
print("\nthe number of people in each age group:")
print (age_counts)

age_gender_counts=df.groupby(['AgeGroup', 'Gender'])['SEQN'].count()
print("\n the number of men and women in each age group:")
print(age_gender_counts)

stats_age=df.groupby('AgeGroup')[['Height', 'Weight']].agg(['mean', 'median', 'std', 'count'])
print("\n statistics for age groups")
print(stats_age)

stats_age_gender = df.groupby(['AgeGroup', 'Gender'])[['Height', 'Weight']].agg(['mean', 'median', 'std', 'count'])
print("\n statistics for age groups and gender")
print(stats_age_gender)
# 5. Correlation Heatmap
# -----------------------------------------
corr = df[["Age", "Height", "Weight", "BMI"]].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation: Age, Height, Weight, BMI")
plt.tight_layout()
plt.show()

# -----------------------------------------
# 6. Histograms
# -----------------------------------------
plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.hist(df["BMI"], bins=10, color="pink", edgecolor="black")
plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Count")
plt.show()

# -----------------------------------------
# 7. Countplots
# -----------------------------------------
sns.countplot(x="AgeGroup", data=df, color="red")
plt.title("People by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

sns.countplot(x="AgeGroup", hue="Gender", data=df, palette="Set2")
plt.title("People by Age Group and Gender")
plt.xlabel("Age Group")
plt.ylabel("Count")
plt.show()

# -----------------------------------------
# 8. Boxplots
# -----------------------------------------
sns.boxplot(x="AgeGroup", y="BMI", data=df, color="lightgreen")
plt.title("BMI by Age Group")
plt.xlabel("Age Group")
plt.ylabel("BMI")
plt.show()

sns.boxplot(x="Gender", y="BMI", data=df, color="lightblue")
plt.title("BMI by Gender")
plt.xlabel("Gender")
plt.ylabel("BMI")
plt.show()

# -----------------------------------------
# 9. Outlier Removal (Z-score)
# -----------------------------------------
df["z_BMI"] = (df["BMI"] - df["BMI"].mean()) / df["BMI"].std()
df_no_outliers = df[df["z_BMI"].abs() < 3]

sns.boxplot(
    x="AgeGroup",
    y="BMI",
    hue="AgeGroup",
    data=df_no_outliers,
    palette="pastel",
    dodge=False
)

plt.title("BMI by Age Group (No Outliers, Z-score)")
plt.xlabel("Age Group")
plt.ylabel("BMI")
plt.show()

