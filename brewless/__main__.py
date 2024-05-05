import argparse

from brewless.generation.tutorial import TutorialGenerator
from brewless.llm import LLM, LocalLLM


def run_local_llm(model, api_command, dtype):
    local_llm = LocalLLM(model, api_command, dtype)
    local_llm.run()


def generate():

    llm = LLM()

    tutorial_generation = TutorialGenerator(
        llm,
        "Information Theory for Machine learning",
        10,
        1000,
    )
    tutorial_generation.generate()


def main():

    parser = argparse.ArgumentParser(prog="brewless", description="brewless CLI help")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    parser_llm = subparsers.add_parser("run_local_llm", help="Run a local LLM")
    parser_llm.add_argument(
        "--model",
        type=str,
        required=False,
        default="meta-llama/Meta-Llama-3-8B-Instruct",
        help="Model name or identifier from HuggingFace",
    )
    parser_llm.add_argument(
        "--base_url",
        type=str,
        required=False,
        default="http://localhost:8000/v1",
        help="The base URL for the OpenAI/local API",
    )
    parser_llm.add_argument(
        "--api_key",
        type=str,
        required=False,
        default="EMPTY",
        help="API key for accessing the model (if any)",
    )
    parser_llm.add_argument(
        "--api_command",
        type=str,
        required=False,
        default="vllm.entrypoints.openai.api_server",
        help="The vllm command to run the server",
    )
    parser_llm.add_argument(
        "--dtype",
        type=str,
        required=False,
        default="float16",
        help="The dtype to use in vllm",
    )
    subparsers.add_parser("generate", help="Generate the text")

    args = parser.parse_args()

    if args.command == "run_local_llm":
        run_local_llm(args.model, args.api_command, args.dtype)
    elif args.command == "generate":
        generate()


if __name__ == "__main__":
    main()
