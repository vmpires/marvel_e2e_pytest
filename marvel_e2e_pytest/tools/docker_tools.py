import subprocess
import os
from dotenv import load_dotenv

# Load and instantiate environment variables
load_dotenv()
env_path = os.getenv('API_PATH')

def docker_up(argument_path=None):
    # Run docker compose up command
    print("Deploying Marvel API containers 🚀")
    path = argument_path or env_path
    result = subprocess.run(["docker", "compose", "up", "-d", "--build"], capture_output=True, text=True, cwd=path)
  
    # Handle the output of the command
    if result.returncode == 0:
        print("Marvel API containers are up and running! 🔥")
    else:
        print(f"🤬 Marvel API containers failed running with return code: {result.returncode}!")
        print(result.stderr)

def docker_down(argument_path=None):
        # Stop all containers with keyword in the name
        print("Stopping Marvel API containers 📥")
        path = argument_path or env_path
        keyword = "marvel"
        containers = subprocess.run(["docker","container","ls","--filter",f"name={keyword}","-q"], capture_output=True, text=True, cwd=path)
        containers_array = containers.stdout.strip().split("\n")
        result = subprocess.run(["docker", "container", "stop", *containers_array], capture_output=True, text=True, cwd=path)
        if result.returncode == 0:
            print(f"Marvel API containers stopped successfully! ✅")
        else:
            print(f"🤬 Failed to stop Marvel API containers: {result.stderr}")