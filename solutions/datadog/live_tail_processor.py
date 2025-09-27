"""
Process a stream of queries (Q:) and log lines (L:).
- For each query, acknowledge with "ACK: <query>; ID=<id>"
- For each log line, if it contains any queries (case-insensitive substring match),
  output "M: <log>; Q=<matched_query_ids>"

Example:
stream = [
    "Q: database",
    "Q: Stacktrace",
    "L: Database service started",
    "L: Loading snapshot failed no stacktrace available"
]
Output: [
    "ACK: database; ID=1",
    "ACK: stacktrace; ID=2",
    "M: database service started; Q=1",
    "M: loading snapshot failed no stacktrace available; Q=2"
]
"""