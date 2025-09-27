"""
Implement recursive directory deletion without using built-in recursive methods.
Use iterative approach with stacks to:
1. Delete all files first
2. Delete directories in post-order (after their contents)

Given APIs: is_directory(path), delete(path), get_all_files(path)
"""