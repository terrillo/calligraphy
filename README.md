# Calligraphy CMS
A static blog generator

## Install
```bash
$ pip install calligraphy
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

### Deploy
Builds the landing and each blog post into a static `html` directory

Export to html (default)

```shell
$ calligraphy export
```

Deploy to AWS S3 (TODO)

```shell
$ calligraphy export --format=s3 --bucket=s3://example.com
```
