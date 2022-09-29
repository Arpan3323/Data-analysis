import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =  pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race'].value_counts())

    # What is the average age of men?
    menAgeSeries = df.loc[df['sex']=='Male', 'age']
    avg = menAgeSeries.mean()
    average_age_men = avg.round(1)

    # What is the percentage of people who have a Bachelor's degree?
    education = df.loc[df['education']=='Bachelors', 'education']
    X = education.count()
    allEducation = df['education']
    Y = allEducation.count()
    percentBachelors = (X / Y) * 100
    percentage_bachelors = percentBachelors.round(1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higherEd = df.loc[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'), 'salary']
    higherEdRich = df.loc[((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')) & (df['salary'] == '>50K' ), 'salary']
    higherEdCount = higherEd.count()
    higherEdRichCount = higherEdRich.count()
    richPercent = ((higherEdRichCount / higherEdCount) * 100)

    #not having Bachelors, masters, or doctorate and making more than 50K
    notHighEd = df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate'), 'salary']
    notHighEdRich = df.loc[((df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')) & (df['salary'] == '>50K' ), 'salary']
    notHighEdCount = notHighEd.count()
    notHighEdRichCount = notHighEdRich.count()
    richNotHighEdPercent = (notHighEdRichCount / notHighEdCount) * 100

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = higherEdCount
    lower_education = notHighEdCount

    # percentage with salary >50K
    higher_education_rich = richPercent.round(1)
    lower_education_rich = richNotHighEdPercent.round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    minHpw = df.loc[:,'hours-per-week']
    min_work_hours = minHpw.min()
    minWorkers = df.loc[df['hours-per-week']==1, 'salary']
    minWorkersCount = minWorkers.count()
    richminWorkers = df.loc[(df['hours-per-week']==1) & (df['salary']=='>50K'), 'salary']
    richminWorkersCount = richminWorkers.count()
    
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = minWorkersCount

    rich_percentage = (richminWorkersCount/minWorkersCount) * 100

    # What country has the highest percentage of people that earn >50K?
    people = df['native-country']
    peopleNo = pd.Series(people.value_counts())
    richCountry = df.loc[df['salary']=='>50K','native-country']
    richPeopleNo= pd.Series(richCountry.value_counts())
    df2 = pd.DataFrame({'percent' : (richPeopleNo[:] / peopleNo[:])*100})
    
    highest_earning_country = df2.loc[df2['percent'] == df2['percent'].max(), 'percent'].index[0]
    highest_earning_country_percentage = (df2['percent'].max()).round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    richIndianOccupation = df.loc[(df['salary']=='>50K') & (df['native-country']=="India"), 'occupation']
    richIndianOccupation.value_counts().index[0]
    top_IN_occupation = richIndianOccupation.value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

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