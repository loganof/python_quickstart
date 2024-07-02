class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context")
        
with MyContextManager():
    print("Inside the context")