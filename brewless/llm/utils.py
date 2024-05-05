import subprocess


def get_gpu_temperature() -> int:
    """
    Get the GPU temperature.

    Returns:
        int: The GPU temperature.
    """
    try:
        command = ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"]
        result = subprocess.check_output(command)
        temperature = int(result.decode("utf-8").strip().split()[0])
        return temperature
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Unable to retrieve GPU temperature.")
        return None
