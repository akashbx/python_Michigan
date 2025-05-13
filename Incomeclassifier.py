import math

# ------------------------------
# STEP 1: Load Data
# ------------------------------
def load_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = [line.strip().split(', ') for line in lines if len(line.strip()) > 0 and '?' not in line]
        return data

# ------------------------------
# STEP 2: Train Classifier
# ------------------------------
def trainClassifier(training_records):
    gt_model = {}    # >50K model
    lte_model = {}   # <=50K model

    gt_count = 0
    lte_count = 0

    for record in training_records:
        attributes = record[:-1]
        label = record[-1].strip()

        if label == '>50K':
            model = gt_model
            gt_count += 1
        else:
            model = lte_model
            lte_count += 1

        for i, attr in enumerate(attributes):
            if i not in model:
                model[i] = []
            model[i].append(attr)

    return build_model(gt_model, gt_count), build_model(lte_model, lte_count)

# ------------------------------
# STEP 3: Build Model
# ------------------------------
def build_model(raw_dict, count):
    model = {}
    for idx, attr_list in raw_dict.items():
        try:
            values = list(map(float, attr_list))
            model[idx] = sum(values) / len(values)
        except:
            freq = {}
            for val in attr_list:
                freq[val] = freq.get(val, 0) + 1
            for k in freq:
                freq[k] /= count
            model[idx] = freq
    return model

# ------------------------------
# STEP 4: Classify Test Records
# ------------------------------
def classifyTestRecords(test_records, classifier):
    gt_model, lte_model = classifier
    predictions = []

    for record in test_records:
        score_gt = 0
        score_lte = 0

        for i, attr in enumerate(record[:-1]):
            try:
                val = float(attr)
                diff_gt = abs(val - gt_model.get(i, val))
                diff_lte = abs(val - lte_model.get(i, val))
                if diff_gt < diff_lte:
                    score_gt += 1
                else:
                    score_lte += 1
            except:
                freq_gt = gt_model.get(i, {}).get(attr, 0)
                freq_lte = lte_model.get(i, {}).get(attr, 0)
                if freq_gt > freq_lte:
                    score_gt += 1
                else:
                    score_lte += 1

        predicted_class = '>50K' if score_gt > score_lte else '<=50K'
        predictions.append(predicted_class)

    return predictions

# ------------------------------
# STEP 5: Report Accuracy
# ------------------------------
def reportAccuracy(test_records, predictions):
    correct = 0
    for rec, pred in zip(test_records, predictions):
        actual = rec[-1].strip()
        if actual == pred:
            correct += 1
    total = len(test_records)
    print(f"\nCorrect: {correct}")
    print(f"Total: {total}")
    print(f"Accuracy: {correct / total:.2%}")

# ------------------------------
# STEP 6: Main Driver
# ------------------------------
def main():
    filename = "annual-income-training.data"
    data = load_data(filename)

    if not data:
        print("No valid data found in file.")
        return

    # Shuffle if needed, here we just split
    split = int(0.75 * len(data))  # 75% train, 25% test
    train_data = data[:split]
    test_data = data[split:]

    print("Training classifier...")
    classifier = trainClassifier(train_data)
    print("Classifying test records...")
    predictions = classifyTestRecords(test_data, classifier)
    reportAccuracy(test_data, predictions)

if __name__ == "__main__":
    main()
