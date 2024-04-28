# brewless

brewless is a Python library designed to facilitate the running of local large language models (LLMs) and generate topic-specific content efficiently. It offers tools to start an LLM server locally and to generate educational content in Markdown format.

## Installation

To install Brewless, clone the repository and run the setup:

```bash
git clone https://github.com/mkareshk/brewless.git
cd brewless
pip install -e .
```

This package requires Python 3.10 or higher.

## Features

- **Local LLM Server:** Start a local server for large language models using a specified model from HuggingFace with configurable data types.
- **Content Generation:** Generate comprehensive tutorials on various topics using predefined prompts and the ability to run the local LLM.

## Usage

### Running the Local LLM

You can start the local LLM server using the following command:

```bash
make run_local_llm \
    --model meta-llama/Meta-Llama-3-8B-Instruct \
    --api_command vllm.entrypoints.openai.api_server \
    --dtype float16
```

### Generating Content

To generate content on a specified topic, use the following command:

```bash
make generate
```

This will create a Markdown file `output.md` in your current directory containing the generated content based on the prompts provided.

## Configuration

Brewless allows you to configure several aspects of the local LLM server and content generation through command-line arguments:

- **Model:** Specify the model to use (default is `meta-llama/Meta-Llama-3-8B-Instruct`).
- **API Command:** Command to start the server (default is `vllm.entrypoints.openai.api_server`).
- **Data Type:** Configure the data type for the model server (default is `float16`).

## Development

To set up a development environment for contributing to Brewless, install the dependencies as follows:

```bash
pip install -e .[dev]
```

This will install all necessary packages, including `pre-commit`, `pytest`, and related testing tools.

## License

Brewless is licensed under the MIT License. For more information, see the `LICENSE` file in the repository.

## Contact
For any questions or issues, please contact Moein Kareshk at mkareshk@outlook.com.
