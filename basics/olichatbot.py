from openai import OpenAI
def olichatbot(text):
    client = OpenAI(api_key = "Fill in your own API key")
    result = client.chat.completions.create(
        model = "gpt-3.5-turbo" ,
        messages = [
            {"role" :"user" , "content" :text}
            ]
    )
    return result.choices[0].message.content
if __name__ == "__main__":     
    print("what's up")
    while (True):
        response = input()
        print(olichatbot(response))
