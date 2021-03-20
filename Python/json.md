# JSON

## I Presentation

Json is a standard python library to load and save information in json format

## II Generals Informations

### Links

- [Python official docs](https://docs.python.org/3/library/json.html "Python official documentation on json package")
- [official json documentation](https://tools.ietf.org/html/rfc8259 "Official report on json standard")

### Install

With pip:

```bash
 python -m pip install json
```

## III Use

### Importation

```python
 import json
```

### Load Informations

To load informations from json file:

```python
 with open(file_path, 'r') as file:
     information = json.load(file)
```

To load informations from a structured string:

```python
 information = json.loads(string)
```

### Save Informations

To save informations to json file:

```python
 with open(file_path, 'w') as file:
     json.dump(information, file)
```

To save informations to a structured string:

```python
 string = json.loads(information)
```
