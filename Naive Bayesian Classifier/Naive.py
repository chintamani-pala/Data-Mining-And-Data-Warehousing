import pandas as pd
data = pd.read_csv('/content/play_tennis.csv')
def calculate_probabilities(data, target_attribute):
    probabilities = {}
    total_count = len(data)
    for value in set(data[target_attribute]):
        value_count = (data[target_attribute] == value).sum()
        probabilities[value] = value_count / total_count

    return probabilities

def calculate_conditional_probabilities(data, target_attribute, condition_attribute, condition_value):
    conditional_probabilities = {}
    total_count = len(data)
    for target_value in set(data[target_attribute]):
        target_value_count = (data[target_attribute] == target_value).sum()
        condition_value_count = ((data[target_attribute] == target_value) & (data[condition_attribute] == condition_value)).sum()
        conditional_probabilities[(target_value, condition_value)] = condition_value_count / target_value_count
    return conditional_probabilities

play_probabilities = calculate_probabilities(data, 'play')

outlook_probabilities = calculate_conditional_probabilities(data, 'play', 'outlook', 'Rain')
temperature_probabilities = calculate_conditional_probabilities(data, 'play', 'temp', 'Hot')
humidity_probabilities = calculate_conditional_probabilities(data, 'play', 'humidity', 'Normal')
wind_probabilities = calculate_conditional_probabilities(data, 'play', 'wind', 'Strong')

new_instance = {'outlook': 'Rain', 'temp': 'Hot', 'humidity': 'Normal', 'wind': 'Strong'}

play_yes_probability = play_probabilities['Yes'] * outlook_probabilities[('Yes', new_instance['outlook'])] * temperature_probabilities[('Yes', new_instance['temp'])] * humidity_probabilities[('Yes', new_instance['humidity'])] * wind_probabilities[('Yes', new_instance['wind'])]

play_no_probability = play_probabilities['No'] * outlook_probabilities[('No', new_instance['outlook'])] * temperature_probabilities[('No', new_instance['temp'])] * humidity_probabilities[('No', new_instance['humidity'])] * wind_probabilities[('No', new_instance['wind'])]

prediction = f'Yes with the accuracy of {play_yes_probability}' if play_yes_probability > play_no_probability else f'No with the accuracy of {play_no_probability}'

print(f"The predicted outcome for the new instance is: {prediction}")
