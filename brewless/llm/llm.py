import time

import numpy as np
from openai import OpenAI

from .utils import get_gpu_temperature


class LLM:

    def __init__(
        self,
        base_url: str = "http://localhost:8000/v1",
        api_key: str = "EMPTY",
        model: str = "meta-llama/Meta-Llama-3-8B-Instruct",
        system_prompt: str = "You an advanced AI.",
        gpu_temperature_threshold: float = 60,
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.model = model
        self.system_prompt = system_prompt
        self.gpu_temperature_threshold = gpu_temperature_threshold

        self.is_local = self.base_url.startswith("http://localhost")

        self.client = OpenAI(base_url=self.base_url, api_key="EMPTY")

    def generate(self, prompt: str) -> str:
        """
        Generate text based on the prompt.

        Args:
            prompt (str): The prompt to generate text from.

        Returns:
            str: The generated text.
        """

        self.release_when_gpu_is_cooldown()

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt},
        ]

        response = self.client.chat.completions.create(
            model=self.model, messages=messages
        )

        if response.choices:
            return str(response.choices[0].message.content)

    def release_when_gpu_is_cooldown(self) -> None:
        if self.is_local:
            for i in np.logspace(-1, 3, num=5):
                temprature = get_gpu_temperature()
                if (
                    temprature is not None
                    and temprature < self.gpu_temperature_threshold
                ):
                    break
                time.sleep(i)
