import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df):
    df['TOTAL KWH'].plot(kind='hist', bins=50, color='skyblue')
    plt.title('Histogram of Total KWH')
    plt.xlabel('Total KWH')
    plt.show()

def plot_heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='cividis', fmt='.2f')
    plt.title('Correlation Matrix for KWH Usage')
    plt.show()

def plot_total_kwh_by_month(df):
    total_kwh_by_month = df[['KWH JANUARY 2010', 'KWH FEBRUARY 2010', 'KWH MARCH 2010', 
                             'KWH APRIL 2010', 'KWH MAY 2010', 'KWH JUNE 2010', 
                             'KWH JULY 2010', 'KWH AUGUST 2010', 'KWH SEPTEMBER 2010', 
                             'KWH OCTOBER 2010', 'KWH NOVEMBER 2010', 'KWH DECEMBER 2010']].sum()
    
    total_kwh_by_month.plot(kind='line', marker='^', color='#183348', markerfacecolor='#581845', markeredgecolor="#FF5733")
    plt.title('Total KWH Usage in 2010 by Month')
    plt.xlabel('Month')
    plt.ylabel('Total KWH Usage')
    plt.xticks(rotation=45)
    plt.show()

def plot_avg_kwh_per_community(avg_kwh_per_community):
    avg_kwh_per_community.plot(kind="bar", color='lightblue')
    plt.title("Average KWH per Community")
    plt.xlabel("Community")
    plt.ylabel("KWH")
    plt.xticks(rotation=45)
    plt.show()

def plot_boxplot(df):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df.iloc[:, 2:], palette='coolwarm')  # Boxplot of KWH Usage
    plt.title('Boxplot of KWH Usage (2010)')
    plt.xticks(rotation=45)
    plt.show()
