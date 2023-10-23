import multiprocessing

def show_process_name():
    print(f"Initializing process with name {multiprocessing.current_process().name}")
    
def calculate(data):
    return data ** 2

def main():
    pool_size = multiprocessing.cpu_count() * 2
    print(f"Pool Size: {pool_size}")
    
    # Creating N processes, where N='pool_size'
    # Each separate process has a name
    pool = multiprocessing.Pool(processes=pool_size, initializer=show_process_name) 
    
    inputs = list(range(7))
    outputs = pool.map(calculate, inputs)
    
    print(f"Outputs: {outputs}")
    
    pool.close()
    pool.join()
    
if __name__ == "__main__":
    main()