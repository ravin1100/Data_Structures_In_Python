
# Tasks:
# Most Popular Tags – Use collections.Counter to find the most frequent tags across posts.
# User Engagement Analysis – Use defaultdict to compute total likes per user.
# Top Posts by Likes – Use sorted() to list posts in descending order of likes.
# User Activity Summary – Combine post and user data to generate a summary per user (posts count, likes, followers, etc.).

from collections import Counter
from collections import defaultdict

posts = [
    {"id": 1, "user": "alice", "content": "Love Python programming!", "likes": 15, "tags": ["python", "coding"]},
    {"id": 2, "user": "bob", "content": "Great weather today", "likes": 8, "tags": ["weather", "life"]},
    {"id": 3, "user": "alice", "content": "Data structures are fun", "likes": 22, "tags": ["python", "learning"]},
]

users = {
    "alice": {"followers": 150, "following": 75},
    "bob": {"followers": 89, "following": 120},
}

tags = [tag for post in posts for tag in post["tags"]]

tags_counter = Counter(tags)

print(tags_counter.most_common())

likes_count = defaultdict(int)
# for user in users:
#     for post in posts:
#         if post["user"] == user:
#             likes_count[user] = post["likes"]
#             break

for post in posts:
    likes_count[post["user"]]+= post["likes"]

print(dict(likes_count))


print(sorted(posts, key = lambda x: x["likes"], reverse= True))


post_count = defaultdict(int)
for post in posts:
    post_count[post["user"]]+=1

print(dict(post_count))

for user in users:
    print(f"User: {user}, Post Count: {post_count[user]}, Likes: {likes_count[user]}, Followers: {users[user]['followers']}")
