from ragas import Dataset

samples = [{"text": "I love learning NLP! It is fantastic.", "label": "positive"},
           {"text": "The concept was terrible and boring.", "label": "negative"},
           {"text": "It was an average session, nothing special.", "label": "positive"},
           {"text": "Absolutely amazing! Best Book of the year.", "label": "positive"}]
# Create a new dataset
dataset = Dataset(name="test_dataset", backend="local/csv", root_dir=".")

# Add a sample to the dataset
for sample in samples:
    dataset.append(sample)

# make sure to save it
dataset.save()