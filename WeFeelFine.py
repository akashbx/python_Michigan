# Project 5 - We Feel Fine Analyzer

import urllib.request

def main():
    BASE_URL = "http://api.wefeelfine.org:8080/ShowFeelings?display=text&returnfields=sentence&limit=1500"

    age_input = input("Enter an age (leave blank to skip): ").strip()
    city_input = input("Enter a city (leave blank to skip): ").strip().lower()
    gender_input = input("Enter gender (male/female, leave blank to skip): ").strip().lower()

    url = BASE_URL

    if gender_input == "male":
        url += "&gender=1"
    elif gender_input == "female":
        url += "&gender=0"

    if city_input:
        url += f"&city={city_input}"

    try:
        age = int(age_input)
        age = (age // 10) * 10 
        url += f"&agerange={age}"
    except ValueError:
        pass 

    print("\nConstructed URL:")
    print(url)

    try:
        connection = urllib.request.urlopen(url)
        data = connection.read().decode('utf-8')
        connection.close()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    sentences = data.split("<br>")
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    print(f"\nTotal sentences fetched: {len(sentences)}")

    top25_feelings = [
        'better', 'bad', 'good', 'sad', 'great', 'happy', 'sorry', 'stupid', 'tired',
        'mad', 'beautiful', 'funny', 'sick', 'fine', 'alone', 'angry', 'awesome', 'cool',
        'depressed', 'okay', 'lost', 'nervous', 'confused', 'fat', 'scared'
    ]

    feeling_counts = {feeling: 0 for feeling in top25_feelings}

    additional_feelings = []
    while True:
        user_feeling = input("Enter a feeling to track (or press Enter to finish): ").strip().lower()
        if user_feeling == "":
            break
        additional_feelings.append(user_feeling)
        feeling_counts[user_feeling] = 0

    for sentence in sentences:
        lower_sentence = sentence.lower()
        for feeling in feeling_counts:
            if f" {feeling} " in lower_sentence or lower_sentence.endswith(f" {feeling}"):
                feeling_counts[feeling] += 1

    print("\nFeeling Counts:")
    for feeling, count in feeling_counts.items():
        print(f"{feeling.capitalize()}: {count}")

if __name__ == "__main__":
    main()
