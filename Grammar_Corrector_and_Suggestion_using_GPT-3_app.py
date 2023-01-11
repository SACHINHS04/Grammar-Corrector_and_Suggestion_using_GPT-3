import openai
import streamlit as st

def correct_passage():
    api_key = st.text_input("Please enter OpenAI API key", "")
    openai.api_key = api_key
    if openai.api_key:
        passage = st.text_area("Enter the passage you want to correct", "")
        # Use GPT-3 to correct the grammar in the passage
        prompt = (f"Please correct the grammar in the following passage and suggest a better version: {passage}")
        corrected_passage = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2048, n =1,stop=None,temperature=0.5)

        # Display the corrected passage
        st.write("Corrected Passage :")
        st.write(corrected_passage.choices[0].text)
    else:
        st.warning("API key is missing")
if __name__=="__main__":
    st.title("Grammar Corrector and Suggestion using GPT-3")
    correct_passage()
