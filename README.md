# Calligraphy CMS
A static blog generator

## Install
```bash
$ pip3 install calligraphy -U
```

## Development
```shell
$ python3 -m venv .
$ . bin/activate
$ pip3 install --editable .
$ calligraphy
```

## Methods

### Verify

Validate all themes and blog posts.

```shell
$ calligraphy verify
```

---

### Export to html
Builds the landing and each blog post into a static `html` directory

Export to html (default)

```shell
$ calligraphy export
```

---

### Static
Run a static version of website

```shell
$ calligraphy static
$ calligraphy static --port=8088
```

## Todo
- [ ] Markdown parser
- [ ] Theme documentation
- [ ] 404 template
- [ ] Tags
