# aiml_generator.py
import openai

def generate_questions_and_answers_with_aiml(cv_text, user_request=None):
    api_key = "2c21f19286b84010968b6dd2ec3f1c71"
    base_url = "https://api.aimlapi.com"

    system_content = (
        "You are an AI specialized in generating interview questions and answers based on a candidate's CV. "
        "Generate at least 10 relevant questions and provide detailed answers based on the CV provided."
    )

    user_content = f"Here is the candidate's CV:\n\n{cv_text}"

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]

    if user_request:
        messages.append({"role": "user", "content": user_request})

    client = openai.OpenAI(api_key=api_key, base_url=base_url)

    try:
        response = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages,
            temperature=0.7,
            max_tokens=512,
        )

        questions_and_answers = response.choices[0].message.content

        # Split the response into individual questions and answers
        qa_pairs = questions_and_answers.split('\n\n')
        
        # Ensure there are at least 10 pairs
        if len(qa_pairs) < 10:
            additional_response = client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                messages=messages,
                temperature=0.7,
                max_tokens=512,
            )
            additional_qa_pairs = additional_response.choices[0].message.content.split('\n\n')
            qa_pairs.extend(additional_qa_pairs)
        
        # Take only the first 10 pairs if more than 10 are generated
        return '\n\n'.join(qa_pairs[:10])

    except openai.APIError as e:
        print(f"OpenAI API Error: {e}")
        return "An error occurred while generating questions and answers. Please try again later."
