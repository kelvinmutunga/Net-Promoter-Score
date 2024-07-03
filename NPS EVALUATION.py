import pandas as pd
import matplotlib.pyplot as plt
# Load the data fromthe Excel file
file_path = 'C://Users//Administration//OneDrive//Desktop//Postevaluation.xlsx'
data = pd.read_excel(file_path)
# Display the first few rows of the data to understand its structure
print(data.head())
# Define the columns to calculate the mean for
rating_columns = [
    'The objectives of the training were met*',
    'The presenters were engaging*',
    'The presentation materials were relevant',
    'The content of the course was organized and easy to follow',
    'The trainers were prepared well versed in the course content and able to answer any questions',
    'Presentability',
    'Conference Facilities',
    'Food',
    'Customer Service',
    'Accommodation Facilities',
    'WIFI Availability'
]
# Calculate the arithmetic mean for each column
mean_ratings = data[rating_columns].mean()
print(mean_ratings)

# Calculate the number of promoters and detractors
recommendations = data['Would you recommend IRES-Kenya to colleagues for Training and Development? Yes/No Why']
promoters = recommendations[recommendations == 'Yes'].count()
detractors = recommendations[recommendations == 'No'].count()
total_responses = recommendations.count()

# Calculate NPS
nps = ((promoters - detractors) / total_responses) * 100
print(f'NPS: {nps}')

# Create bar graph for average ratings
plt.figure(figsize=(12, 7))
mean_ratings.plot(kind='bar', color='skyblue')
plt.title('Average Ratings for Training Evaluation Criteria')
plt.xlabel('Criteria')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
# Create data for pie chart
labels = ['Promoters', 'Detractors']
sizes = [promoters, detractors]
colors = ['green', 'red']
explode = (0.1, 0)

# Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Net Promoter Score (NPS) Distribution')
plt.show()
