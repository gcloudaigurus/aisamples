
# Advanced Prompt Techniques: Prompt Chaining & Decomposition

# This program demonstrates prompt chaining and decomposition 
# to solve a complex task: generating a story based on user input.

# Prompt Chaining: We break down the story generation into smaller, 
# manageable prompts, chaining the output of one prompt as input to the next.

# Prompt Decomposition:  Each prompt focuses on a specific aspect of the story 
# (e.g., setting, characters, plot points), making the overall task less overwhelming 
# for the language model.

def get_setting():
    """Gets the story setting from the user."""
    return input("Enter the story setting (e.g., a dark forest, a bustling city): ")

def get_characters(setting):
    """Gets the main characters, influenced by the setting."""
    return input(f"Describe the main characters in this {setting}: ")

def create_plot_point_one(characters, setting):
    """Generates the first plot point, using characters and setting."""
    return input(f"Describe the first plot point involving {characters} in the {setting}: ")

def create_plot_point_two(plot_point_one, characters):
    """Generates the second plot point, building on the first."""
    return input(f"What happens next, building on '{plot_point_one}' involving {characters}?: ")


def generate_conclusion(plot_point_two, characters, setting):
    """Generates the story conclusion."""
    return input(f"How does the story conclude, given '{plot_point_two}' in the {setting} with {characters}?: ")



def generate_story():
    """Chains together the prompts to generate the full story."""

    setting = get_setting()
    characters = get_characters(setting)
    plot_point_one = create_plot_point_one(characters, setting)
    plot_point_two = create_plot_point_two(plot_point_one, characters)
    conclusion = generate_conclusion(plot_point_two, characters, setting)

    story = f"""
    Story:

    Setting: {setting}
    Characters: {characters}
    Plot Point 1: {plot_point_one}
    Plot Point 2: {plot_point_two}
    Conclusion: {conclusion}
    """
    print(story)


if __name__ == "__main__":
    generate_story()


