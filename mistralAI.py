from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

def build_prompt(query, search_results):
    prompt_template = """
    You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
    Use only the facts from the CONTEXT when answering the QUESTION.

    QUESTION: {question}

    CONTEXT: 
    {context}
    """.strip()

    context = ""
    
    for doc in search_results:
        context = context + f"section: {doc['_source']['section']}\nquestion: {doc['_source']['question']}\nanswer: {doc['_source']['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt, model="mistral-medium-latest"):
    mistral_key = "pqcHo388Jwjc76uZ3kBVhGCMpiobC3kF"
    messages = [
        ChatMessage(role="user", content=prompt)
    ]
    client = MistralClient(api_key=mistral_key)
    chat_response = client.chat(
        model=model,
        messages=messages
    )
    return (chat_response.choices[0].message.content)