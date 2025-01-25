import os
import subprocess
import sys
import shutil

def check_dependencies():
    """Check if required tools are installed"""
    try:
        subprocess.run(['npm', '--version'], capture_output=True, text=True)
        subprocess.run(['python', '--version'], capture_output=True, text=True)
        subprocess.run(['pip', '--version'], capture_output=True, text=True)
    except FileNotFoundError as e:
        print(f"Error: Required dependency not found. {e}")
        print("Please ensure Node.js, Python, and pip are installed.")
        sys.exit(1)

def clean_previous_builds():
    """Clean previous build artifacts"""
    try:
        # Remove previous build directories
        directories_to_clean = ['dist', 'build', 'client/dist', 'client/build']
        for directory in directories_to_clean:
            if os.path.exists(directory):
                shutil.rmtree(directory)
                print(f"Cleaned {directory}")
    except Exception as e:
        print(f"Error cleaning previous builds: {e}")

def build_frontend():
    """Build React frontend"""
    try:
        print("Building frontend...")
        os.chdir('client')
        
        # Install frontend dependencies
        subprocess.run(['npm', 'install'], check=True)
        
        # Build frontend
        subprocess.run(['npm', 'run', 'build'], check=True)
        
        os.chdir('..')
        print("Frontend build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Frontend build failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during frontend build: {e}")
        sys.exit(1)

def install_backend_dependencies():
    """Install backend dependencies"""
    try:
        print("Installing backend dependencies...")
        os.chdir('server')
        
        # Activate virtual environment if it exists
        venv_path = '../venv/Scripts/activate' if sys.platform == 'win32' else '../venv/bin/activate'
        
        if os.path.exists(venv_path):
            subprocess.run([venv_path], shell=True, check=True)
        
        # Install requirements
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        
        # Install PyInstaller
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)
        
        os.chdir('..')
        print("Backend dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Backend dependency installation failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during dependency installation: {e}")
        sys.exit(1)

def create_pyinstaller_spec():
    """Create PyInstaller executable"""
    try:
        print("Creating executable...")
        subprocess.run([
            'pyinstaller', 
            '--name', 'RoutineMaster',
            '--onefile',
            '--windowed',
            '--add-data', 'client/dist:client/dist',
            '--add-data', 'server:server',
            'launcher.py'
        ], check=True)
        
        print("Executable created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"PyInstaller build failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error during executable creation: {e}")
        sys.exit(1)

def main():
    try:
        # Ensure script is run from project root
        project_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(project_root)

        # Comprehensive build process
        check_dependencies()
        clean_previous_builds()
        build_frontend()
        install_backend_dependencies()
        create_pyinstaller_spec()

        print("\nBuild process completed successfully!")
        print("Executable is located in the 'dist' directory.")

    except KeyboardInterrupt:
        print("\nBuild process interrupted.")
    except Exception as e:
        print(f"Unexpected error in build process: {e}")

if __name__ == "__main__":
    main()