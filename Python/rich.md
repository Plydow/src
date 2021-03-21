# Rich

## I Presentation

Rich is a library to increase the console output from python.

## II Generals Informations

### Links

- [Rich documentation](https://rich.readthedocs.io/en/stable/ "Unofficial documentation for rich")
- [Github](https://github.com/willmcgugan/rich "Github rich")

### Install

with pip:

```bash
python -m pip install rich
```

## III Use

### Importation

```python
import rich
```

### Colorize a print

Rich allows you to colorize and format python outputs in the main consoles.

```python
rich.print(string)
```

Rich's string formatting system works under the tag principle. Tags are in the form [tag_name] and [/tag_name].

Some of the tags are as follows:

   Tag     | Description
:--------: | :--------------------------------------
color name | colorize text in this color
    b      | bold
    i      | italic
    u      | underline
    s      | text strike
    uu     | text with two underline
    o      | overline text
link=http  | transform text in hypertext link to web
