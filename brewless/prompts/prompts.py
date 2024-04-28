from textwrap import dedent

PROMPT_TEXT_FOR_TOPIC = dedent(
    """
    I need a comprehensive tutorial that helps me deeply understand
    the background, context, and core concepts of a specific topic.
    Please generate the tutorial with the following guidelines:

    - Ensure the tutorial is comprehensive, self-contained, and easy to follow.
    - Discuss the importance of the topic, potential use cases, and possible alternatives.
    - Explain the underlying intuitions, challenges,
        and solutions associated with the topic, and provide clear examples to illustrate these points.
    - Include detailed explanations of relevant mathematics and algorithms,
        along with necessary notations, if this enhances understanding.
    - Provide code implementations where applicable to demonstrate practical applications.
    - Develop a set of diverse and advanced interview questions
        related to the topic, each accompanied by answers.
    - Structure the tutorial into multiple sections
        for clarity and use Roman numerals for chapter headings.

    Please format the output in the {TOPIC_FILE_FORMAT} format.

    Topic: "{TOPIC_NAME}"
    """
)
