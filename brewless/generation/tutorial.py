from .prompts import PROMPT_TEXT_FOR_TOPIC, PROMPT_TEXT_SECTIONS


class TutorialGenerator:

    def __init__(self, llm, topic: str, section_num=8, pages_num: int = 1000) -> None:
        self.llm = llm
        self.topic = topic
        self.section_num = section_num
        self.pages_num = pages_num

    def generate(self):

        # generate the section titles
        self.sections = self.generate_outline()
        self.sections_str = "\n".join(self.sections)

        # generate sections
        for section in self.sections:
            text = self.generate_section(section_title=section)
            with open(f"{section}.md", "w") as f:
                f.write(text)

    def generate_outline(self) -> str:
        """
        Generate the outline of the tutorial.

        Returns:
            str: The generated outline of the tutorial.
        """
        prompt = PROMPT_TEXT_SECTIONS.format(
            TOPIC_NAME=self.topic,
            PAGES_NUM=self.pages_num,
            SECTION_NUM=self.section_num,
        )
        sections_text = self.llm.generate(prompt)
        sections = [i for i in sections_text.split("\n") if i != ""]
        assert len(sections) == self.section_num
        return sections

    def generate_section(self, section_title: str) -> str:
        """
        Generate the content for a specific section of the tutorial.

        Args:
            section_title (str): The title of the section to generate content for.

        Returns:
            str: The generated content for the section.
        """
        prompt = PROMPT_TEXT_FOR_TOPIC.format(
            TOPIC_FILE_FORMAT="Markdown",
            TOPIC_NAME=self.topic,
            OUTLINE=self.sections_str,
            SECTION_NAME=section_title,
        )
        return self.llm.generate(prompt)
