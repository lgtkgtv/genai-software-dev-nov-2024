from openai import OpenAI
client = OpenAI()

base_content = '''
Newton's First Law, often called the Law of Inertia, states that an object will remain at rest or continue to move at a constant velocity unless acted upon by an external force. This law highlights the inherent "inertia" in objects, which is the tendency of an object to resist changes to its state of motion. In simple terms, if an object is stationary, it won’t start moving on its own. Similarly, if an object is moving in a straight line at a constant speed, it won’t slow down, speed up, or change direction unless something influences it.
For instance, when a soccer ball is kicked across a field, it eventually slows down and stops due to forces like friction from the grass and air resistance. Without these forces, the ball would theoretically keep rolling indefinitely. Newton's First Law helps explain why passengers lurch forward in a car when it stops suddenly; they were moving at the same speed as the car and will keep moving forward until something, like a seatbelt, applies a force to stop them. This principle of inertia is foundational in physics, illustrating that motion (or lack of it) does not change unless influenced by a force, providing a basis for understanding how forces interact in our physical world.
'''

def create_prompt(reading_level, interests):
    return f'Rewrite this article for someone with a {reading_level}-grade reading level, who is interested in {",".join(interests)}. """{base_content}"""'

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": create_prompt(12, ['Baseball', 'Golf'])
        }
    ]
)

print(completion.choices[0].message)