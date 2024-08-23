from langchain_ollama import OllamaLLM
import time

# Define the model
model = OllamaLLM(model="ollama_prompt")


# Parsed CV data

cv_data2 = {
  "candidate_name": "Ali",
  "skills": [
    {"skill": "Medicine", "proficiency": "expert"},
    {"skill": "Surgery", "proficiency": "advanced"},
    {"skill": "Patient Care", "proficiency": "expert"}
  ],
  "interests": ["medical research", "public health"],
  "potential_roles": ["surgeon", "medical researcher"],
  "education": {
    "degree": "Doctor of Medicine",
  }
}

cv_data = {
    "candidate_name": "Ahmet",
    "skills": [
        {"skill": "Python", "proficiency": "intermediate"},
        {"skill": "SQL", "proficiency": "advanced"},
        {"skill": "Machine Learning", "proficiency": "beginner"}
    ],
    "interests": ["data science", "artificial intelligence"],
    "potential_roles": ["data analyst", "machine learning engineer"],
    "education": {
        "degree": "Bachelor of Computer Science",
    }
}

# Welcome the candidate
welcome_message = (
    f"Welcome {cv_data['candidate_name']}! Are you ready to start the interview?"
)
print(welcome_message)

time.sleep(2)  # Pause for 3 seconds to simulate conversational delay

# Ask if the candidate wants to start the interview
answer = input("Should we start the interview now? (yes/no): ").strip().lower()

question_prompt = (
             f"The candidate has proficiency in {cv_data['skills'][0]['skill']} and an interest in {cv_data['interests'][0]}. "          
        )

if answer in ["yes", "y"]:
    while True:       
        # Invoke the model to generate the interview question
        question_result = model.invoke(input=question_prompt)
        print(f"Model: {question_result}")
        
        # Prompt the user for an answer or to quit
        user_input = input("Your answer (type 'quit' to exit): ").strip().lower()
        
        if user_input in ["quit", "exit", "stop"]:
            print("Interviewer: Thank you for your time. Have a great day!")
            break
        else:
            # Pause briefly before asking the next question
            time.sleep(1)
            question_prompt = user_input
            
        
elif answer in ["no", "n"]:
    print("Interviewer: No problem, let me know when you're ready!")
else:
    print("Interviewer: I didn't quite catch that. Please answer with 'yes' or 'no'.")
