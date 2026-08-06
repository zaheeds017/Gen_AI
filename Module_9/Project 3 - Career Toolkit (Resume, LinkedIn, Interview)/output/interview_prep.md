# Interview Prep - Priya Sharma

Generated 2026-07-31. Practice out loud; do not memorise word for word.

## Technical questions (tailored to your skills)

### Python
**Q: What is the difference between a list and a tuple?**
A: A list is mutable (you can change it) and uses []; a tuple is immutable and uses (). Use a tuple for fixed data you do not want changed, e.g. coordinates.

**Q: What does a list comprehension do? Give an example.**
A: It builds a list in one line: squares = [x*x for x in range(5)] gives [0,1,4,9,16]. It is shorter and often faster than a for-loop that appends.


### Machine Learning
**Q: Explain the train/test split and why we need it.**
A: We hold back part of the data (the test set) and never train on it, so we can measure how the model does on data it has never seen. Testing on training data gives a dishonestly high score.

**Q: What is overfitting and how do you reduce it?**
A: Overfitting is when a model memorises the training data and fails on new data. Reduce it with more data, a simpler model, regularisation, or cross-validation.

**Q: When is accuracy a misleading metric?**
A: On imbalanced data. If 99 percent of emails are 'not spam', a model that always says 'not spam' is 99 percent accurate but useless. Use precision, recall, or F1 instead.


### Data Visualization
**Q: How do you choose the right chart?**
A: Match the chart to the question: bar for comparing categories, line for trends over time, histogram for one variable's distribution, scatter for the relationship between two.


### NLP
**Q: What is TF-IDF in one line?**
A: It scores a word high when it is frequent in one document but rare across all documents, so common words like 'the' get low weight and distinctive words get high weight.


### Flask
**Q: How do you serve a trained model with Flask?**
A: Load the saved model once when the server starts, add a route (e.g. /predict) that reads the input, calls model.predict, and returns the result as JSON or a rendered page.


### Streamlit
**Q: Why might you pick Streamlit over Flask for a demo?**
A: Streamlit builds an interactive UI from a plain Python script with almost no web code, so it is faster for data demos. Flask gives more control and is better for real APIs.


### Git/GitHub
**Q: What is the difference between git commit and git push?**
A: commit saves a snapshot to your LOCAL history; push uploads your commits to the REMOTE repository (e.g. GitHub) so others can see them.


## General questions
**Q: Tell me about yourself.**
A: Give a 60-second story: who you are, what you have built, and what you want next. End on why this role fits.

**Q: Why do you want to work in AI/ML?**
A: Tie it to something concrete you built and enjoyed, plus the impact you want to have.

## Behavioral questions (use the STAR method)
STAR = Situation, Task, Action, Result. Keep answers to ~60-90 seconds.

**Q: Tell me about a project you are proud of.**
- Situation: I built 'Iris Species Predictor (Flask)' during my AI program.
- Task: I had to make it work end-to-end, not just in a notebook.
- Action: Trained a Random Forest classifier and served it as both an HTML form and a JSON API
- Result: It runs reliably and is on my GitHub as a portfolio piece.

**Q: Tell me about a time you faced a bug or setback.**
- Situation/Task: describe the problem and what was at stake.
- Action: what you tried, step by step (this is the important part).
- Result: what fixed it and what you learned.

