"""
Implement a BufferedWriter class that batches writes to minimize I/O operations.
- Buffer writes internally until buffer is full
- Support write(bytes), write(string), flush(), and close()
- Handle partial writes when the underlying file can only write a limited number
  of bytes at a time

Key challenge: Handle the case where file.write() returns fewer bytes written
than requested (simulate syscall limitations).
"""