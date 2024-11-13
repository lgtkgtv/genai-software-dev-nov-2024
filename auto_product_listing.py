from openai import OpenAI
client = OpenAI()

product_description_short = input('Please enter a short description of the product you wish to sell: ')

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"Suggest a title for a product with this description: {product_description_short}"
        }
    ]
)

title = completion.choices[0].message.content
print(title)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"Write a one-paragraph, detailed description for this product: {product_description_short}"
        }
    ]
)

product_description_long = completion.choices[0].message.content
print('Description:')
print(product_description_long)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": f"Give me 5 image generation prompts that would create compelling visuals for a product with this description. Respond with only the prompts, separated by commas. The prompts themselves must not include commas: {product_description_long}."
        }
    ]
)

# image_prompts = completion.choices[0].message.content.split(',')
# print('Image prompts:')
# print(image_prompts)

# for prompt in image_prompts:
#     response = client.images.generate(
#         model="dall-e-3",
#         prompt=prompt,
#         size="1024x1024",
#         quality="standard",
#         n=1,
#     )

#     image_url = response.data[0].url

    # print(image_url)