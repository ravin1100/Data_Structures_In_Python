# Deque for Efficient Operations
# Use Python’s collections.deque to implement a browser history system with a maximum size of 5 pages. Your system should support:

# Add New Page – Append new page URLs to the end. If the size exceeds 5, remove the oldest page from the front.
# Go Back – Remove the last visited page (from end) and store it in a forward stack.
# Go Forward – Restore the most recently backed-out page from the forward stack to the end of the history.
# Maintain State – Track current history and forward stack after each action.
# Use two deque objects for history and forward_stack.



from collections import deque

history = deque(maxlen=5)
forward_stack = deque()

def add_new_page(url):
    history.append(url)
    forward_stack.clear()
    show_state(f"Visited: {url}")

def go_back():
    if len(history) > 1:
        last_page = history.pop()
        forward_stack.append(last_page)
        show_state(f"Back to: {history[-1]}")
    else:
        show_state("No page found to go back")

def go_forward():
    if forward_stack:
        next_page = forward_stack.pop()
        history.append(next_page)
        show_state(f"Next Page: {next_page}")
    else:
        show_state("No forward page is available")

def show_state(action=""):
    print(f"\n{action}")
    print("Current History:", list(history))
    print("Forward Stack:", list(forward_stack))

add_new_page("google.com")
add_new_page("openai.com")
add_new_page("github.com")
add_new_page("stackoverflow.com")
add_new_page("python.org")

add_new_page("claude.com")

go_back()     # Go back to python.org
go_back()     # Go back to stackoverflow.com

go_forward()  # Forward to python.org

add_new_page("wikipedia.org")  # Forward stack cleared

go_back()
go_forward()
go_forward()

