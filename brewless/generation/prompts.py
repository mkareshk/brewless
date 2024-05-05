from textwrap import dedent

PROMPT_TEXT_FOR_TOPIC = dedent(
    """
    I am developing an in-depth tutorial to provide advanced users with a thorough understanding of the background, context, and core concepts of {TOPIC_NAME}.

    # Outline
    Below is the outline of the tutorial:
    {OUTLINE}

    # Current Task
    Your task is to generate the tutorial content for section {SECTION_NAME} exclusively.

    # Considerations
    Please adhere to the following guidelines when generating the content for this section:
    - Ensure the section content is comprehensive, self-contained, and easy to comprehend.
    - Discuss the significance of the topic, potential applications, and alternative approaches.
    - Explain the underlying principles, challenges, and solutions associated with the topic.
    - Provide clear, intuitive examples to elucidate concepts.
    - Incorporate detailed explanations of relevant mathematics and linear algebra.
    - Include comprehensive computer algorithms.
    - Where applicable, provide code implementations to demonstrate practical applications.
    - Develop a minimum of 10 diverse and advanced interview questions related to the topic, each accompanied by detailed answers. Follow this format:
        - <question number>. Question: The interview question
        - Answer: The corresponding answer.
    - Structure the section into multiple sub-sections, using Roman numerals for chapter headings to enhance clarity.

    # Format
    - Format the output according to the {TOPIC_FILE_FORMAT} format.
    - Ensure the generated text contains a minimum of 500,000 tokens in total.
    - Each section of the generated text should comprise at least 100,000 tokens.
    - Ensure mathematical equations are correctly formatted.
    - Avoid including additional information in the output.
    """
)

PROMPT_TEXT_SECTIONS = dedent(
    """
    I am drafting a comprehensive book on "{TOPIC_NAME}"
    that will span at least {PAGES_NUM} pages and encompass {SECTION_NUM} distinct sections.
    Your task is to create the outline of the book, comprising a list of section titles without any subsections.

    Generate the outline following these guidelines:
    - Ensure each section title minimally correlates with others.
    - Craft an outline that is thorough, self-contained, and easily navigable.

    # Format:
    - Each section title should appear on a separate line.
    - Begin each title with a Roman numeral, followed by a period and a space.
    - Generate exactly {SECTION_NUM} titles in exactly {SECTION_NUM} lines.
    - Only generate the section titles; do not include code for saving to a file or any JSON object description.
    - Avoid including additional information in the output.
    """
)
