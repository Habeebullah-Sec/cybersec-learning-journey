def log_analyzer(filename):
    failed_logins = 0
    print(f"Analyzing {filename}...")
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                if "Failed login" in line:
                    failed_logins += 1
                    print(f"Alert: {line.strip()}")
        
        print(f"\nTotal Failed Login Attempts: {failed_logins}")
    except FileNotFoundError:
        print("Error: File not found")

# Example usage
log_analyzer("auth.log")
