import subprocess

# List of libraries to install
libraries = [
    'aiocontextvars',
    'aiofiles'
]

def install_libraries():
    for lib in libraries:
        try:
            print(f"Installing {lib}...")
            subprocess.check_call(['pip', 'install', lib])
            print(f"{lib} installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {lib}. Error: {e}")

if __name__ == "__main__":
    install_libraries()