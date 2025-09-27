"""
Build a streaming log matcher that efficiently matches queries against logs.
- Support adding queries dynamically
- Support streaming log entries
- Use inverted indexes for O(1) lookup
- Match when log contains ALL keywords from a query

Optimize for:
- Sublinear matching time
- Memory efficiency (use integer IDs instead of strings)
- Support for millions of logs and thousands of queries
"""