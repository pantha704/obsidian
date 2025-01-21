
Here's a comprehensive guide for Machine Learning projects, from beginner to advanced:

### Beginner Level Projects

1. **House Price Prediction**
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

class HousePricePredictor:
    def __init__(self):
        self.model = LinearRegression()
        
    def prepare_data(self, data):
        # Handle missing values
        data = data.fillna(data.mean())
        
        # Select features
        self.features = ['square_feet', 'bedrooms', 'bathrooms']
        X = data[self.features]
        y = data['price']
        
        return train_test_split(X, y, test_size=0.2, random_state=42)
    
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)
        
    def evaluate(self, X_test, y_test):
        predictions = self.model.predict(X_test)
        return {
            'mse': mean_squared_error(y_test, predictions),
            'r2': r2_score(y_test, predictions)
        }
```

2. **Image Classification (MNIST)**
```python
import tensorflow as tf
from tensorflow.keras import layers, models

def create_cnn_model():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    
    return model

# Load and preprocess data
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
```

### Intermediate Level Projects

3. **Sentiment Analysis**
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

class SentimentAnalyzer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.classifier = RandomForestClassifier()
        
    def preprocess_text(self, text):
        # Tokenization
        tokens = word_tokenize(text.lower())
        
        # Remove stopwords and punctuation
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words and t.isalnum()]
        
        return ' '.join(tokens)
    
    def train(self, texts, labels):
        processed_texts = [self.preprocess_text(text) for text in texts]
        X = self.vectorizer.fit_transform(processed_texts)
        self.classifier.fit(X, labels)
        
    def predict(self, text):
        processed_text = self.preprocess_text(text)
        X = self.vectorizer.transform([processed_text])
        return self.classifier.predict(X)[0]
```

4. **Time Series Forecasting**
```python
import pandas as pd
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

class TimeSeriesForecaster:
    def __init__(self):
        self.model = Prophet(
            yearly_seasonality=True,
            weekly_seasonality=True,
            daily_seasonality=True
        )
        
    def prepare_data(self, data):
        # Prophet requires columns 'ds' (date) and 'y' (value)
        data = data.rename(columns={
            'date': 'ds',
            'value': 'y'
        })
        return data
        
    def train_and_forecast(self, data, forecast_periods):
        self.model.fit(data)
        future = self.model.make_future_dataframe(periods=forecast_periods)
        forecast = self.model.predict(future)
        return forecast
```

### Advanced Level Projects

5. **Recommendation System**
```python
import numpy as np
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import cosine_similarity

class RecommenderSystem:
    def __init__(self, n_factors=50):
        self.n_factors = n_factors
        
    def create_user_item_matrix(self, ratings):
        self.user_item_matrix = ratings.pivot(
            index='user_id',
            columns='item_id',
            values='rating'
        ).fillna(0)
        
    def train(self):
        # Perform SVD
        U, sigma, Vt = svds(self.user_item_matrix.values, k=self.n_factors)
        
        # Convert to diagonal matrix
        sigma = np.diag(sigma)
        
        # Calculate predicted ratings
        self.predicted_ratings = np.dot(np.dot(U, sigma), Vt)
        
    def get_recommendations(self, user_id, n_recommendations=5):
        user_row = self.predicted_ratings[user_id]
        already_rated = self.user_item_matrix.iloc[user_id].nonzero()[0]
        
        # Get items that user hasn't rated
        not_rated = np.setdiff1d(
            np.arange(self.user_item_matrix.shape[1]),
            already_rated
        )
        
        # Get predicted ratings for not rated items
        predicted_ratings = user_row[not_rated]
        
        # Get top N recommendations
        recommended_items = not_rated[predicted_ratings.argsort()[-n_recommendations:]]
        
        return recommended_items
```

6. **Object Detection with YOLO**
```python
import torch
from torch.utils.data import DataLoader
from torchvision import transforms

class ObjectDetector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        
    def detect_objects(self, image_path):
        results = self.model(image_path)
        return results.pandas().xyxy[0]  # Returns bounding boxes
    
    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frames = []
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            results = self.detect_objects(frame)
            annotated_frame = self.draw_boxes(frame, results)
            frames.append(annotated_frame)
            
        cap.release()
        return frames
```

7. **Reinforcement Learning**
```python
import gym
import numpy as np
from collections import defaultdict

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        self.env = env
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: np.zeros(env.action_space.n))
        
    def choose_action(self, state):
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.q_table[state])
        
    def learn(self, n_episodes):
        for episode in range(n_episodes):
            state = self.env.reset()
            done = False
            
            while not done:
                action = self.choose_action(state)
                next_state, reward, done, _ = self.env.step(action)
                
                # Q-learning update
                old_value = self.q_table[state][action]
                next_max = np.max(self.q_table[next_state])
                new_value = (1 - self.lr) * old_value + self.lr * (reward + self.gamma * next_max)
                self.q_table[state][action] = new_value
                
                state = next_state
```

### Utility Functions and Tools

1. **Data Preprocessing**
```python
def preprocess_data(df):
    # Handle missing values
    df = df.fillna(df.mean())
    
    # Remove outliers
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=[np.number])))
    df = df[(z_scores < 3).all(axis=1)]
    
    # Normalize numerical features
    scaler = StandardScaler()
    df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(
        df.select_dtypes(include=[np.number])
    )
    
    return df
```

2. **Model Evaluation**
```python
def evaluate_model(y_true, y_pred, task_type='classification'):
    if task_type == 'classification':
        return {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1': f1_score(y_true, y_pred, average='weighted')
        }
    else:
        return {
            'mse': mean_squared_error(y_true, y_pred),
            'rmse': np.sqrt(mean_squared_error(y_true, y_pred)),
            'mae': mean_absolute_error(y_true, y_pred),
            'r2': r2_score(y_true, y_pred)
        }
```

Remember to:
- Use proper data preprocessing
- Implement cross-validation
- Handle imbalanced datasets
- Document your code
- Use version control
- Create proper test sets
- Validate your models
- Consider model interpretability

These projects will help you build a strong portfolio in machine learning while learning essential concepts and techniques.


3. Handwritten pdf doc to computer readable text pdf doc