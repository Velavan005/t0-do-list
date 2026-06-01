import re
import getpass

def check_password_strength(password):
    """
    Evaluates password strength and returns a score, rating, and detailed feedback.
    """
    score = 0
    feedback = []
    
    # 1. Length Check
    if len(password) >= 12:  # Modern standard recommends 12+ characters
        score += 1
    elif len(password) >= 8:
        score += 1
        feedback.append("Increase length to 12+ characters for better security.")
    else:
        feedback.append("Password is too short (minimum 8 characters).")
        
    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")
        
    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")
        
    # 4. Numeric Digit Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")
        
    # 5. Special Character Check (Broadened list)
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+\-\[\]\\/~`=;']", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, $, %, _).")

    # Determine Rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    else:
        rating = "Strong"
        
    # Extra check: Common weak passwords
    common_passwords = {"password", "password123", "12345678", "qwertyuiop", "letmein123"}
    if password.lower() in common_passwords:
        rating = "Weak (Commonly Used)"
        feedback.insert(0, "This password is widely known and easily cracked. Choose something unique.")

    return score, rating, feedback

def main():
    print("=== Password Strength Checker ===")
    
    # Use getpass to hide typing. Fallback to input if not in a supported terminal.
    try:
        password = getpass.getpass("Enter password: ")
    except (AttributeError, NotImplementedError):
        password = input("Enter password: ")
        
    if not password:
        print("No password entered.")
        return

    score, rating, feedback = check_password_strength(password)
    
    print("\n--- Results ---")
    print(f"Rating: {rating}")
    print(f"Score:  {score}/5")
    
    if feedback:
        print("\nSuggestions for improvement:")
        for suggestion in feedback:
            print(f" - {suggestion}")
    else:
        print("\nExcellent! Your password meets all security criteria.")

if __name__ == "__main__":
    main()