# Calligraphy CMS
A static blog generator

## Install (TODO)
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

### Deploy (TODO)
Builds the landing and each blog post into a static `dist` directory 

Export to html (defualt)

```shell
$ calligraphy export 
```

Deploy to AWS S3

```shell
$ calligraphy export --format=s3 --bucket=s3://example.com
```

