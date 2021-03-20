# Base64

## I Presentation

Base64 is a standard library to convert ASCII or UTF-8 encodage on base64.

## II Generals Informations

### Links

- [Python official docs](https://docs.python.org/3/library/base64.html "Python official documentation on base64")
- [RFC](https://tools.ietf.org/html/rfc4648 "RFC for base64 encoding")

### Install

With pip:

```bash
python -m pip install base64
```

## III Use

### Importation

```python
import base64
```

### Encode in base64

```python
base64_string = base64.b64encode(binary_string)
```

### Decode from base64

```python
binary_string = base64.b64decode(base64_string)
```

⚠ if _base64_string_ is not a length multiple of 4, the function raises an error. To avoid this, add enough '=' to reach a length multiple of 4\. The character '=' does not affect the value of the string when decoded.

Use this to solve this problem:

```python
base64_corrected_string = base64_string + b'=' * (-len(base64_string) % 4)
```

### Convert string between binary and standard

To convert string between binary form and standard form

```python
binary_string = std_string.encode()
std_string = binary_string.decode()
```
