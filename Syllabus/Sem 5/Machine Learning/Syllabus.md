

### Machine Learning Exam Survival Guide  

---

#### **Module-I: ML Fundamentals [4L]**  
* **Conceptual Frameworks:**  
  - **Learning Types:**  
    - *Supervised:* Teacher gives answers (labeled data → classification/regression).  
    - *Unsupervised:* Self-study (unlabeled data → clustering/dimensionality reduction).  
    - *Reinforcement:* Trial-and-error gaming (agent + rewards → optimal actions).  
  - **Discriminative Algorithms:** Learn decision boundaries (e.g., SVM, Logistic Regression).  

* **Algorithm Selection Tree:**  
  ```mermaid  
  graph TD  
    A[Labeled Data?] -->|Yes| B[Predict category?]  
    A -->|No| C[Cluster or Reduce Dimensions?]  
    B -->|Yes| D[Use Classifier]  
    B -->|No| E[Use Regressor]  
    C -->|Cluster| F[K-means/Hierarchical]  
    C -->|Reduce| G[PCA/ICA]  
  ```  

* **Resource Kit:**  
  - 🎥: "ML Types Explained" (StatQuest, 8 min)  
  - 📄: Google ML Crash Course Cheat Sheet  

---

#### **Module-II: Feature Engineering [7L]**  
* **Core Mechanics:**  
  - **Entropy/Gini:**  
    - *Entropy:* `H = -Σ(p_i * log p_i)` → Uncertainty measure (0 = pure).  
    - *Gini:* `G = 1 - Σ(p_i²)` → Simpler impurity metric.  
  - **PCA vs ICA:**  
    - *PCA:* Finds orthogonal axes of max variance (→ compression). *Analogy:* "Squinting to see main shapes."  
    - *ICA:* Separates mixed signals into independent sources (→ blind source separation). *Analogy:* "Untangling spaghetti."  

* **Key Formulas:**  
  - **Standardization:** `z = (x - μ)/σ`  
  - **EM Algorithm:** Iteratively estimates hidden params (e.g., Mixture of Gaussians).  

* **Exam Hotspot:** Normalization vs Standardization use cases (e.g., use standardization for SVM/PCA).  

---

#### **Module-III: Classification [12L]**  
* **Algorithm Breakdowns:**  
  | Algorithm         | Core Mechanics                          | Visualization                     |  
  |-------------------|-----------------------------------------|-----------------------------------|  
  | **Logistic Reg**  | Sigmoid output (0-1) for probability    | S-curve decision boundary         |  
  | **SVM**           | Maximize margin between classes         | Hyperplane with support vectors   |  
  | **Gradient Descent** | Roll downhill to find min loss       | [●]→[●]→[●] (steps in valley)     |  
  | **Backpropagation** | Pass errors backward to adjust weights | Input → ▣ → ▣ → Output (blame flow)|  
  | **Naive Bayes**   | Bayes' theorem + feature independence  | Probability tree                  |  

* **Key Comparisons:**  
  - **Generative vs Discriminative:**  
    | Type           | Goal                     | Example          |  
    |----------------|--------------------------|------------------|  
    | Generative     | Model data distribution  | Naive Bayes      |  
    | Discriminative | Learn decision boundary  | SVM, Logistic Reg|  

  - **Bias-Variance Tradeoff:**  
    - *High Bias:* Oversimplified (underfit) → Misses patterns.  
    - *High Variance:* Overly complex (overfit) → Noise-sensitive.  

* **Exam Hotspots:**  
  - **Regularization:** L1 (Lasso → sparsity) vs L2 (Ridge → small weights).  
  - **Vectorization:** Matrix ops for speed (e.g., `numpy` in Python).  
  - **Neural Nets:** Input → Hidden (ReLU) → Output (Softmax).  

---

#### **Module-IV: Clustering [7L]**  
* **Clustering Visuals:**  
  - **K-means Steps:**  
    1. Pick K centroids randomly.  
    2. Assign points → nearest centroid.  
    3. Move centroids → mean of points.  
    4. Repeat until stable.  
  - **PCA:** Projects data onto eigenvectors (↓ dimensions).  

* **Classification vs Clustering:**  
  | Aspect         | Classification           | Clustering             |  
  |----------------|--------------------------|------------------------|  
  | Data           | Labeled                  | Unlabeled              |  
  | Goal           | Predict class            | Discover groups        |  

* **Resource Kit:**  
  - 🎥: "K-means Clustering" (StatQuest, 6 min)  
  - 🛠️: PCA Visualization (scikit-learn demo)  

---

#### **Module-V: ML System Design [6L]**  
* **Evaluation Toolkit:**  
  - **Confusion Matrix:**  
    ```  
                Actual +     Actual -  
    Predicted +   TP           FP  
    Predicted -   FN           TN  
    ```  
  - **Precision vs Recall Tradeoff:**  
    - *Precision:* "Don’t flag innocents" (Fraud detection: minimize false alarms).  
    - *Recall:* "Catch all criminals" (Medical tests: minimize missed cases).  
  - **F1-Score:** `2 * (Precision * Recall) / (Precision + Recall)` → Balances P/R.  

* **ROC Curve Cheat Sheet:**  
  - X-axis: FPR (False Positive Rate)  
  - Y-axis: TPR (Recall)  
  - **AUC > 0.9** = Excellent model!  

* **Overfitting Solutions:**  
  - Cross-validation (k-fold)  
  - Regularization (↑ Lambda → ↓ variance)  

---

#### **Module-VI: Case Studies [4L]**  
* **Recurring Patterns:**  
  1. **Customer Segmentation:**  
     - *Clustering (K-means) + PCA* → Group users by behavior.  
  2. **Anomaly Detection:**  
     - *SVM/PCA* → Flag fraud (e.g., credit card transactions).  
  3. **Predictive Maintenance:**  
     - *Time-series + HMM* → Forecast machine failures.  

* **Exam Hotspot:** Map algorithms to problems (e.g., "Spam detection → Naive Bayes").  

---

### **Exam Power Kit**  
- **Formulas to Memorize:**  
  - **Entropy:** `H = -Σ p_i log₂(p_i)`  
  - **F1-Score:** `2 * (P * R) / (P + R)`  
  - **L2 Regularization:** `Loss + λ Σ w_i²`  

- **Python Snippets:**  
  ```python  
  # Confusion Matrix (scikit-learn)  
  from sklearn.metrics import confusion_matrix  
  cm = confusion_matrix(y_true, y_pred)  
  ```  

- **Last-Minute Resources:**  
  - 🎥: "ROC Curves Explained" (StatQuest, 9 min)  
  - 📄: Scikit-learn Algorithm Cheat Sheet  
  - 🛠️: TensorFlow Playground (NN visualization)  

**Pro Tip:** For theory-heavy questions (e.g., backprop math), focus on *intuition* over derivations. Use analogies!