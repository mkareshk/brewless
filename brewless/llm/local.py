import subprocess


class LocalLLM:

    def __init__(
        self,
        model="meta-llama/Meta-Llama-3-8B-Instruct",
        api_command="vllm.entrypoints.openai.api_server",
        dtype="float16",
    ) -> None:
        self.model_name = model
        self.api_command = api_command
        self.dtype = dtype

        self.command = [
            "python",
            "-m",
            self.api_command,
            "--model",
            self.model_name,
            "--dtype",
            self.dtype,
        ]

    def run(self):
        try:
            subprocess.run(self.command, check=True)
            print("Server started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to start server: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
