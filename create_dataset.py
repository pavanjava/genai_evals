from ragas import Dataset

def create_sentiment_dataset():
    samples = [{"text": "I love learning NLP! It is fantastic.", "label": "positive"},
               {"text": "The concept was terrible and boring.", "label": "negative"},
               {"text": "It was an average session, nothing special.", "label": "positive"},
               {"text": "Absolutely amazing! Best Book of the year.", "label": "positive"}]
    # Create a new dataset
    dataset = Dataset(name="prompt_eval_dataset", backend="local/csv", root_dir=".")

    # Add a sample to the dataset
    for sample in samples:
        dataset.append(sample)

    # make sure to save it
    dataset.save()

def create_math_dataset():
    samples = [
        {"expression": "∫(3x² + 2x - 1)dx from 0 to 2", "expected": 10},
        {"expression": "∫(e^x + 1/x)dx from 1 to e", "expected": "e^e - e + 1"},
        {"expression": "∫sin(x)cos(x)dx from 0 to π/2", "expected": 0.5},
        {"expression": "d/dx(x³ - 4x² + 5x - 2) at x=3", "expected": 14},
        {"expression": "d/dx(e^(2x) * sin(x)) at x=0", "expected": 1},
        {"expression": "d/dx(ln(x²+1)) at x=2", "expected": 0.8},
        {"expression": "dy/dx = 2x, y(0) = 3, find y(2)", "expected": 7},
        {"expression": "dy/dx = y, y(0) = 1, find y(1)", "expected": 2.71828},
        {"expression": "Vertex of parabola y = 2x² - 8x + 5 (x-coordinate)", "expected": 2},
        {"expression": "Focus distance from vertex for y² = 16x", "expected": 4},
        {"expression": "Radius of circle x² + y² - 6x + 8y = 0", "expected": 5},
        {"expression": "Area of circle (x-3)² + (y+2)² = 25", "expected": 78.54},
        {"expression": "Eccentricity of hyperbola x²/16 - y²/9 = 1", "expected": 1.25},
        {"expression": "Distance between foci of x²/25 - y²/144 = 1", "expected": 26},
        {"expression": "Determinant of [[3, 2], [1, 4]]", "expected": 10},
        {"expression": "Trace of matrix [[5, 2, 1], [0, 3, 4], [1, 0, 2]]", "expected": 10},
        {"expression": "Rank of matrix [[1, 2, 3], [2, 4, 6], [3, 6, 9]]", "expected": 1},
        {"expression": "Solve: 2x + y = 7, x - y = 2 (value of x)", "expected": 3},
        {"expression": "Solve: 3x + 2y = 12, x + y = 5 (value of y)", "expected": 3},
        {"expression": "Solve: x + y + z = 6, 2x - y + z = 3, x + 2y - z = 5 (value of x)", "expected": 1},
    ]
    # Create a new dataset
    dataset = Dataset(name="agent_eval_dataset", backend="local/csv", root_dir=".")

    # Add a sample to the dataset
    for sample in samples:
        dataset.append(sample)

    # make sure to save it
    dataset.save()

if __name__ == "__main__":
    create_sentiment_dataset()
    create_math_dataset()