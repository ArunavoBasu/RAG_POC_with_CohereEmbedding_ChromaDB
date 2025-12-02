## This file is for reading the prompt and storing the text into the variable which will return the prompt

def prompt_reader(context, question):
    """
    This function returns the prompt
    """
    prompt = f"""
                You are an expert assistant. Use ONLY the following context to answer.

                CONTEXT:
                {context}

                QUESTION:
                {question}

                ANSWER:
            """

    return prompt