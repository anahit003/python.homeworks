import requests

def get_filtered_titles(endpoint):
    response = requests.get(endpoint)
    data = response.json()

    filtered_titles = []
    for item in data:
        if len(item['title'].split()) <= 6:
            filtered_titles.append(item['title'])

    return filtered_titles

def get_filtered_bodies(endpoint):
    response = requests.get(endpoint)
    data = response.json()

    filtered_bodies = []
    for item in data:
        if item['body'].count('\n') <= 3:
            filtered_bodies.append(item['body'])

    return filtered_bodies

def create_post(endpoint, data):
    response = requests.post(endpoint, json=data)
    if response.status_code == 201:
        print("Post created ")
    else:
        print("Error creating post:", response.status_code)

def update_post(endpoint, post_id, data):
    response = requests.put(f"{endpoint}/{post_id}", json=data)
    if response.status_code == 200:
        print("Post updated ")
    else:
        print("Error updating post:", response.status_code)

def delete_post(endpoint, post_id):
    response = requests.delete(f"{endpoint}/{post_id}")
    if response.status_code == 200:
        print("Post deleted ")
    else:
        print("Error deleting post:", response.status_code)

# Example
filtered_titles = get_filtered_titles("https://jsonplaceholder.typicode.com/posts")
print("Filtered titles with 6 words or less:", filtered_titles)

filtered_bodies = get_filtered_bodies("https://jsonplaceholder.typicode.com/comments")
print("Filtered bodies with 3 lines of description or less:", filtered_bodies)

create_post("https://jsonplaceholder.typicode.com/posts", {"title": "My New Post", "body": "This is the content of my new post."})

update_post("https://jsonplaceholder.typicode.com/posts", 1, {"title": "Updated Title"})

delete_post("https://jsonplaceholder.typicode.com/posts", 2)
