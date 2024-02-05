# py-react-kit

![GitHub](https://img.shields.io/github/license/pascalallen/py-react-kit)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/pascalallen/py-react-kit)

py-react-kit is a fully containerized dev kit designed to get you up and running fast for Python and React development. This kit ships with:

- Docker + Docker configuration
- a Python server
- a Postgres database
- Adminer as a DB GUI
- an API built with Flask + GraphQL
- an ORM built with SQLAlchemy
- a React client
- TypeScript
- Webpack
- and helper scripts

## Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Development Environment Setup

### Clone Repository

```bash
cd <projects-parent-directory> && git clone https://github.com/pascalallen/py-react-kit.git
```

### Bring Up Environment

```bash
bin/up
``` 

You will find the site running at [http://localhost:8080/](http://localhost:8080/)

### Install JavaScript Dependencies

```bash
bin/yarn ci
```

### Compile TypeScript with Webpack

```bash
bin/yarn build
```

### Watch For Frontend Changes

```bash
bin/yarn watch
```

### Take Down Environment

```bash
bin/down
```

### Interact with the Python image

```bash
bin/exec <python ./app.py>
```