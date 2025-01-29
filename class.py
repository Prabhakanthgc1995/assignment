import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='| %(levelname)-15s | %(asctime)s | %(name)s | %(lineno)-4s | %(name)s ::  %(message)s')

logger = logging.getLogger("test")

# Define the commands you want to execute
commands = [
    'grep -rl "org" *',
    'ls',
    'pwd'
]

# Run the commands
for cmd in commands:
    try:
        result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # Print the stdout and stderr
        logger.info(result.stdout)
        if result.stderr:
            logger.error(result.stderr)  # Log errors to the logger
        else:
            print(result.stderr, end='')  # Print error if not logged
    except subprocess.CalledProcessError as e:
        logger.error(f"Command '{cmd}' failed with exit code {e.returncode}.")
        logger.error(f"stderr: {e.stderr}")

