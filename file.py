import itertools
import string
import time

# Simulated login system
def login(username, password):
    # Simulated correct credentials
    correct_username = "user"
    correct_password = "pass"  # Use a shorter password for demonstration purposes
    
    if username == correct_username and password == correct_password:
        return True
    return False

# Brute force attack simulation
def brute_force_attack(username, max_length=4):
    chars = string.ascii_lowercase  # Use only lowercase letters for simplicity
    attempts = 0
    
    for length in range(1, max_length + 1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            print(f"Attempt {attempts}: Trying '{guess}'")
            
            if login(username, guess):
                print(f"Success! Password is '{guess}'")
                print(f"Total attempts: {attempts}")
                return guess
            
    print("Brute force attack failed. Password not found.")
    return None

# Main function
if __name__ == "__main__":
    username = "user"
    print("Starting brute force attack...")
    start_time = time.time()
    
    brute_force_attack(username)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")