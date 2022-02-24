import pandas as pd 


def calculate_demographic_data(print_data = True):
    # Read Data from File
    df = pd.read_csv("adult.data.csv")

    # How many of each race are 
    # represented in this dataset? 
    # This should be a Pandas series with race 
    # names as the index labels.

    race_count = {}
    for race in df['race']:
        race_count[race] = race_count.get(race,0) + 1
    race_count = pd.DataFrame.from_dict(race_count, orient='index', columns = ['Race Amount'])

    # Avg Age of men
    age_sex_df = df[['sex', 'age']]
    age_male_df = age_sex_df[df['sex'] == 'Male']
    average_age_men = (age_male_df['age'].mean()).round(decimals = 1)
    
    # Percentage of people who have a Bachelor's degree
    education_df = df['education']
    bachelor_amount = (education_df == 'Bachelors').sum()
    total_amount = len(education_df)
    percentage_bachelors = ( (bachelor_amount/total_amount)*100 ).round(decimals = 1)

    # Percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    rich_salary_mask = df.salary == '>50K'
    higher_education_mask = (df.education == 'Bachelors') |(df.education == 'Masters')|(df.education == 'Doctorate')
    lower_education_mask = (df.education != 'Bachelors') & (df.education != 'Masters') & (df.education != 'Doctorate')
    
    higher_education_amount = df[higher_education_mask]
    lower_education_amount = df[lower_education_mask]

    higher_education_rich = round((len(higher_education_amount[rich_salary_mask])/(len(higher_education_amount))*100),1)
    lower_education_rich = round((len(lower_education_amount[rich_salary_mask])/(len(lower_education_amount))*100),1)

    # minimum number of hours a person works per week (hours-per-week feature)
    min_work_hours = df['hours-per-week'].min()
    
    # Percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers_rich = num_min_workers[rich_salary_mask]

    rich_percentage = round((((len(num_min_workers_rich)) / len(num_min_workers))*100),1)



    # Highest Earning Country
    country_count = df['native-country'].value_counts()
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_rich_count / country_count).idxmax()
    highest_earning_country_percentage = round(((country_rich_count / country_count)*100),1)

    # Highest Job In India
    # Highest Job In India
    newdf = df[df['native-country'] == 'India'][df['salary'] == '>50K']
    highest_occupation_India = dict()
    for rich_job in newdf['occupation']:
      highest_occupation_India[rich_job] = highest_occupation_India.get(rich_job,0)+1

    top_IN_occupation = max(highest_occupation_India, key = highest_occupation_India.get)

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()