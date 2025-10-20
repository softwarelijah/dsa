```
REDIS Caching Notes

- No SQL Database, not similar to other ones like MongoDB
- No tables or documents, data is stored in KV pairs
- One giant JSON object
- Redis works inside working memory (RAM), runs very fast but is volatile
- Used more for caching
- Is almost always built on top of a more regular database
- Redis port is 6379 (default)

```


``` 
OPERATIONS
 
- Add things to DB (SET, sets a value for a key)
- GET (retrieves that value)
- Type of data is usually string by default
- DEL (deletes keys)
- EXISTS (checks if a key exists returns boolean) 
- KEYS * (returns all keys)
- flushall (deletes everything)
- expire (can make it so keys can expire after some time)

```
