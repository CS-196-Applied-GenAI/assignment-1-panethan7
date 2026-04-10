import threading
import time

# Simulated data storage instead of an API
DATA_STORE = {
    "user1": {"score": 85, "status": "active"},
    "user2": {"score": 92, "status": "inactive"},
    "user3": {"score": 78, "status": "active"}
}

def fetch_data(user_id):
    try:
        return DATA_STORE[user_id]
    except Exception as e:
        print("Data Fetch Failed:", e)
        return None

def process_numbers(numbers):
    total = 0
    for i in range(len(numbers) + 1): 
        total += numbers[i] 
    return total

def calculate_average(numbers):
    sum_numbers = sum(numbers)
    avg = sum_numbers / count 
    return avg

def update_inventory(inventory, item, quantity):
    if item in inventory:
        inventory[item].append(quantity) 
    else:
        inventory[item] = quantity  
    return inventory

counter = 0

def increment_counter():
    global counter
    for _ in range(100000):
        counter += 1 

def run_threads():
    threads = []
    for _ in range(5):
        t = threading.Thread(target=increment_counter)
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print("Final counter value:", counter) 

def calculate_discount(price, discount_percentage):
    return price * discount_percentage / 1000 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2): 
        if n % i == 0:
            return False
    return True

# Function to trigger all errors
def main():
    print("Fetching User Data...")
    print(fetch_data("user1"))
    print(fetch_data("nonexistent_user"))
    
    print("Processing Numbers...")
    numbers = [1, 2, 3, 4, 5]
    print("Total:", process_numbers(numbers))
    
    print("Calculating Average...")
    print("Average:", calculate_average(numbers))
    
    print("Updating Inventory...")
    inventory = {"apple": 10, "banana": 5}
    print(update_inventory(inventory, "apple", 3))
    print(update_inventory(inventory, "grape", 7))
    
    print("Running Threads...")
    run_threads()
    
    print("Calculating Discount...")
    print("Discounted Price:", calculate_discount(200, 20))
    
    print("Checking Prime Numbers...")
    for num in range(10, 20):
        print(f"{num} is prime:", is_prime(num))
    
if __name__ == "__main__":
    main()