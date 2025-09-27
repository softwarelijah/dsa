"""
Similar to Tag Stream Filter but with optimized data structures:
- Build inverted index: tag -> document IDs
- Support efficient multi-keyword AND searches
- Return related tags from matching documents
Time complexity requirements:
- Add tag: O(n * k) where k = tag count
- Search: O(m * d + l * k) where m = keywords, d = docs per keyword
"""