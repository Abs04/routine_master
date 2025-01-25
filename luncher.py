import subprocess
import sys
import os
import threading
import time
import webbrowser

def start_frontend():
    try:
        print("Starting frontend...")
        frontend_process = subprocess.Popen(
            ['npm', 'run', 'dev'], 
            cwd='client',  
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        def print_output(pipe, prefix):
            for line in pipe:
                print(f"{prefix}:", line.decode('utf-8').strip())
        
        stdout_thread = threading.Thread(target=print_output, args=(frontend_process.stdout, "FRONTEND-OUT"))
        stderr_thread = threading.Thread(target=print_output, args=(frontend_process.stderr, "FRONTEND-ERR"))
        stdout_thread.start()
        stderr_thread.start()
        
        return frontend_process
    except Exception as e:
        print(f"Error starting frontend: {e}")
        return None

def start_backend():
    try:
        print("Starting backend...")
        # Create the full command as a single string
        if os.name == 'nt':  # Windows
            command = 'call venv\\Scripts\\activate && uvicorn src.main:app --reload'
        else:  # Unix-like systems
            command = 'source venv/bin/activate && npm run dev'
            
        backend_process = subprocess.Popen(
            command,
            cwd='server',  
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        def print_output(pipe, prefix):
            for line in pipe:
                print(f"{prefix}:", line.decode('utf-8').strip())
        
        stdout_thread = threading.Thread(target=print_output, args=(backend_process.stdout, "BACKEND-OUT"))
        stderr_thread = threading.Thread(target=print_output, args=(backend_process.stderr, "BACKEND-ERR"))
        stdout_thread.start()
        stderr_thread.start()
        
        return backend_process
    
    except Exception as e:
        print(f"Error starting backend: {e}")
        return None

def open_frontend():
    try:
        # Wait for services to start
        time.sleep(15)  # Increased wait time
        webbrowser.open('http://localhost:5173')
    except Exception as e:
        print(f"Error opening frontend: {e}")

def main():
    try:
        # Ensure we're in the right directory
        project_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(project_root)

        # Start frontend in a thread
        frontend_thread = threading.Thread(target=start_frontend, daemon=True)
        frontend_thread.start()

        # Start backend in a thread
        backend_thread = threading.Thread(target=start_backend, daemon=True)
        backend_thread.start()

        # Open frontend in browser
        browser_thread = threading.Thread(target=open_frontend, daemon=True)
        browser_thread.start()

        # Keep the application running
        print("Application started. Press Ctrl+C to exit.")
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nApplication stopped.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()