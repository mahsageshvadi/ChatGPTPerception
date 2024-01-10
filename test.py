import base64
import requests
import os
from CMGBarChartGenerator import GenerateCMGBarChart

# Generate Charts
#GenerateCMGBarChart(10)

# OpenAI API Key
api_key = "**************************"


frame_result = []   # Result by ChatGPT (frame)
no_frame_result = [] # Result by ChatGPT (no frame)
correct = []  # Correct result given by ground_truth.txt

frame_average_scores = [] # Store average scores (5 trials)
no_frame_average_scores = [] # Store average scores (5 trials)

# Fill in "correct" array
with open('dataset\\barchart_CMG\\ground_truth.txt', 'r') as file:
    for line in file:
        numbers = list(map(float, line.split()))

        max_index = numbers.index(max(numbers))
        correct.append(max_index)


#################################################################################
# Get images

def get_image_path(folder_path):
  return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.png')]

folder_path = "dataset"
image_paths = get_image_path(folder_path)

##########################################################
# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
for i in range(5):
    frame_result = []
    no_frame_result = []
    count = 0

    # Call the api with the images
    for image_path in image_paths:
        count += 1
        # Getting the base64 string
        base64_image = encode_image(image_path)
        
        headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
        }

        payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": "Which bar is longer? The left bar has the ID 0 and the right bar has the ID 1. Give me the ID of the longest bar. I don't need any sentence. JUST GIVE ME 0 or 1. For framed rectangles, just look at the length of bars inside."
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
                }
            ]
            }
        ],
        "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        content_string = response.json()['choices'][0]['message']['content']

       
        if count <= 10:
            if (content_string=="0" or content_string=="1"):
                frame_result.append(int(content_string))
            else:
                frame_result.append(None)
        else:
            if (content_string=="0" or content_string=="1"):
                no_frame_result.append(int(content_string))
            else:
                no_frame_result.append(None)

    print("Attempt " + str(i+1))
    print("Correct: " + str(correct) + str(correct))
    print("ChatGPT: " + str(frame_result) + str(no_frame_result) )
    print()
    
    frame_correct_answers = sum([correct[i] == frame_result[i] for i in range(len(correct))])
    no_frame_correct_answers = sum([correct[i] == no_frame_result[i] for i in range(len(correct))])

    total_questions = len(correct)
    frame_correct_percentage = (frame_correct_answers / total_questions) * 100
    no_frame_correct_percentage = (no_frame_correct_answers / total_questions) * 100

    frame_average_scores.append(frame_correct_percentage)
    no_frame_average_scores.append(no_frame_correct_percentage)


###########################################################################
frame_average_score = sum(frame_average_scores)/len(frame_average_scores)
print("Average percentage (frame): " + str(frame_average_score) + "%")

no_frame_average_score = sum(no_frame_average_scores)/len(no_frame_average_scores)
print("Average percentage (No frame): " + str(no_frame_average_score) + "%")

