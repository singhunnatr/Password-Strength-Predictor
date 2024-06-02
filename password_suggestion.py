import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load the trained model
model = joblib.load('password_strength_model.pkl')

# Function to extract features from a password
def extract_features(password):
    has_digits = any(char.isdigit() for char in password)
    has_special_symbols = any(char in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for char in password)
    length = len(password)
    return [has_digits, has_special_symbols, length]

# Function to predict password strength
def predict_strength(password):
    features = np.array(extract_features(password)).reshape(1, -1)
    strength = model.predict(features)[0]
    return strength

# Function to suggest ways to strengthen the password
def suggest_improvements(password):
    suggestions = []
    if not any(char.isdigit() for char in password):
        suggestions.append("Add digits (0-9)")
    if not any(char in '!@#$%^&*()-_=+[{]}\\|;:\'",<.>/?' for char in password):
        suggestions.append("Add special characters (!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?')")
    if len(password) < 8:
        suggestions.append("Increase the length to at least 8 characters")
    return suggestions

# Function to plot suggestions
def plot_suggestions(suggestions):
    fig, ax = plt.subplots()
    ax.axis('off')
    suggestions_str = "\n".join(suggestions)
    plt.text(0.5, 0.5, suggestions_str, ha='center', va='center', fontsize=12, wrap=True)
    plt.title("Password Strengthening Suggestions", fontsize=15)
    plt.show()

# Main function
def main():
    password = input("Enter a password to check its strength: ")
    strength = predict_strength(password)
    strength_str = ["Weak", "Medium", "Strong"][strength]
    
    print(f"Password strength: {strength_str}")

    if strength < 2:
        suggestions = suggest_improvements(password)
        if suggestions:
            plot_suggestions(suggestions)
        else:
            print("Your password is strong.")

if __name__ == "__main__":
    main()
