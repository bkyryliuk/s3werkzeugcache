# s3werkzeugcache


Following is an example of use of s3cache for a server side encryption enabled bucket
```
  bucket = 'test-bucket'

  put_extra_args = {'ServerSideEncryption': 'AES256'}
  cache = S3Cache(bucket, 'cache_test/', put_extra_args=put_extra_args)
  cache.add('name', 's3cache')
  val = cache.get('name')
  print(val)
```