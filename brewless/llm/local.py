import subprocess
from typing import Literal


class LocalLLM:

    def __init__(
        self,
        model: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        api_command: str = "vllm.entrypoints.openai.api_server",
        dtype: Literal["float16", "float32"] = "float16",
    ) -> None:
        """
        Initialize the LocalLLM class.

        Args:
            model (str, optional): The LLM to use. Defaults to "meta-llama/Meta-Llama-3-8B-Instruct".
            api_command (str, optional): The command to run the LLM using vllm. Defaults to "vllm.entrypoints.openai.api_server".
            dtype (Literal[&quot;float16&quot;, &quot;float32&quot;], optional): The data type of the model. Defaults to "float16".
        """
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

    def run(self) -> None:
        """
        Run the local LLM server.
        """
        try:
            subprocess.run(self.command, check=True)
            print("Server started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to start server: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
