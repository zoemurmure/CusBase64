Customize the indexing string of base64 encoding.

You can set you own indexing string using the config() method.



Usage: 

```python
b = CusBase64()
b.encode('binary\x00string') # Output: YmluYXJ5AHN0cmluZw==
b.decode('YmluYXJ5AHN0cmluZw==') # Output: binary\x00string

b.config('aABCDEFGHIJKLMNOPQRSTUVWXYZbcdefghijklmnopqrstuvwxyz0123456789+/')
b.decode('c2UsYi1kYWM0cnUjdFlvbiAjb21wbFU0YP==') # Output: self-destruction complete
```



