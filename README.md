# s3werkzeugcache

A `cachelib`-compatible cache backend that uses Amazon S3 for storage. This project is an implementation of the `werkzeug` cache interface, now part of [`cachelib`](https://pypi.org/project/cachelib/).

## Installation

```bash
pip install s3werkzeugcache
```

## Usage

Here is an example of how to use `s3werkzeugcache`:

```python
from s3cache import S3Cache

# Basic usage
cache = S3Cache(s3_bucket='your-s3-bucket', key_prefix='cache/')

# Set a value in the cache
cache.set('my_key', 'my_value')

# Get a value from the cache
value = cache.get('my_key')
print(value)  # Output: my_value

# Add a value only if the key does not already exist
cache.add('another_key', 'another_value')

# Delete a key from the cache
cache.delete('my_key')

# Example with server-side encryption
put_extra_args = {'ServerSideEncryption': 'AES256'}
secure_cache = S3Cache(
    s3_bucket='your-s3-bucket',
    key_prefix='secure-cache/',
    put_extra_args=put_extra_args
)
secure_cache.set('secure_key', 'a very secure value')
```

## Configuration

The `S3Cache` constructor accepts the following arguments:

-   `s3_bucket` (str): The name of the S3 bucket to use for storage.
-   `key_prefix` (str or callable): A string that is prepended to all cache keys. If a callable is provided, it will be called to generate the prefix.
-   `default_timeout` (int): The default timeout for cache keys in seconds. **Note:** This parameter is currently ignored. See the Limitations section for more details.
-   `get_extra_args` (dict): A dictionary of extra arguments to pass to the `download_fileobj` method of the `boto3` S3 client.
-   `put_extra_args` (dict): A dictionary of extra arguments to pass to the `upload_fileobj` method of the `boto3` S3 client.
-   `head_extra_args` (dict): A dictionary of extra arguments to pass to the `head_object` method of the `boto3` S3 client.

## Limitations

### `clear()` Method

The `clear()` method is not supported by this cache backend and will always return `False`.

### Timeouts

The `timeout` parameter in the `set()` and `add()` methods is ignored, as S3 does not support key-level expiration. To manage object expiration, you should configure lifecycle rules on your S3 bucket. For more information, please refer to the [AWS S3 documentation on object lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).