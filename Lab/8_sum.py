a = 30
b = '12.5'
try:
    result = a + b
    print(f"Sum: {result}")
    
except TypeError:
    try: 
        result = a + float(b)
        print(f"Sum: {result}")
        
    except ValueError:
        print("Something went wrong")