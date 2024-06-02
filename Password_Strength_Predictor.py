import joblib
import matplotlib.pyplot as plt

# Function to extract features from a single password
def extract_features(password):
    has_digits = any(char.isdigit() for char in password)
    has_special_symbols = any(char in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for char in password)
    length = len(password)
    return [has_digits, has_special_symbols, length]

# Function to predict the strength of a given password and plot the result
def predict_and_plot_password_strength(password, model):
    features = extract_features(password)
    probabilities = model.predict_proba([features])[0]
    strength = model.predict([features])[0]
    
    # Map strength values to descriptive labels
    strength_labels = ['Weak', 'Medium', 'Strong']
    
    # Plot the probabilities
    plt.figure(figsize=(8, 4))
    plt.bar(strength_labels, probabilities, color=['red', 'orange', 'green'])
    plt.xlabel('Strength')
    plt.ylabel('Probability')
    plt.title(f"Password Strength Prediction for '{password}'")
    plt.ylim(0, 1)
    plt.show()
    
    return strength_labels[strength]

# Load the trained model
model = joblib.load('password_strength_model.pkl')

# Take user input for a password
user_password = input("Enter a password to check its strength: ")

# Predict the strength of the input password and plot the result
predicted_strength = predict_and_plot_password_strength(user_password, model)

# Output the result
print(f"The strength of the password '{user_password}' is: {predicted_strength}")
