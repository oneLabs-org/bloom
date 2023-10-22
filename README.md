# Bloom 🌺 : A Self-Hosted CFP portal for Events

---
A Backend Server Written in 🐍 and FastAPI with 🐘 DB that powers the Self-Hosted CFP Management Service Bloom.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![GitHub issues](https://img.shields.io/github/issues/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend)
[![GitHub forks](https://img.shields.io/github/forks/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend)
[![GitHub stars](https://img.shields.io/github/stars/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/stargazers)
[![GitHub license](https://img.shields.io/github/license/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/blossomlabsio/Bloom-Backend)
---

<p align="center">
    <img width="320" height="320" src="artwork/4388667.png" alt="Material Bread logo">
</p>

# 🤔 Pre-requisites

- `python3`
- `pdm`
- `postgres`

## 🐍 Python Version Support

This project is designed to be compatible with specific versions of Python for optimal performance and stability.

### Supported Python Version

- **Python 3.11.0rc2**

> ❗️ For the best experience and performance, it is recommended to use the version mentioned above.

Before diving into the project, ensure that you have the correct Python version installed. To check the version of Python you currently have, execute the following command in your terminal:

```bash
python --version
```

### 🐍 Installing Python 3.11.0rc2 with `pyenv`

**Protip:** Managing multiple Python versions is a breeze with [pyenv](https://github.com/pyenv/pyenv). It allows you to seamlessly switch between different Python versions without the need to reinstall them.

If you haven't installed `pyenv` yet, follow their [official guide](https://github.com/pyenv/pyenv) to set it up.

Once you have `pyenv` ready, install the recommended Python version by running:

```bash
pyenv install 3.11.0rc2
```

> When you navigate to this project's directory in the future, `pyenv` will automatically select the recommended Python version, thanks to the `.python-version` file in the project root.


# 📦 Setup

## Local setup 🛠️ without Docker 🐳 

### Configuring your `.env` file

1. **Copying the `.env.example` file**:
   Begin by creating a copy of the `.env.example` file and renaming it to `.env`.
   ```bash
   cp .env.example .env
   ```

2. **Filling in the Parameters**:
   
   - **SQLALCHEMY_DATABASE_URI**:
     This is the connection string for your PostgreSQL database. The format is generally:
     ```
     postgresql://[user[:password]@][host][:port][/dbname]
     ```
     For example, if you have a local PostgreSQL server with the database `mydb`, username `admin`, and password `password123`, the connection string would be:
     ```
     SQLALCHEMY_DATABASE_URI="postgresql://admin:password123@localhost/mydb"
     ```

   - **JWT_SECRET**:
     This is a secret key used to encode and decode JWT tokens. It should be a random and long string to ensure the security of your tokens. You can generate one using various online tools or by running the following Python snippet:
     ```python
     import secrets
     print(secrets.token_hex(16))
     ```

   - **JWT_ALGORITHM**:
     This specifies the algorithm used to sign the JWT tokens. The most common algorithm is `HS256`, which stands for HMAC using SHA-256. Depending on your requirements, you might use other algorithms, but for most applications, `HS256` is sufficient. So, you can set it as:
     ```
     JWT_ALGORITHM="HS256"
     ```

   - **ACCESS_TOKEN_EXPIRY_MINUTES**:
     This is an integer that represents the number of minutes before a generated access token expires. For example, if you want the token to expire in 60 minutes (1 hour), you'd set:
     ```
     ACCESS_TOKEN_EXPIRY_MINUTES=60
     ```


### Configuring PostgreSQL URI in `alembic.ini`

To set up the PostgreSQL connection for [Alembic](https://alembic.sqlalchemy.org/en/latest/):

* **Locate the Configuration in `alembic.ini`**:
   * Open the `alembic.ini` file and navigate to approximately line `#63`.

* **Add Your PostgreSQL URI**:
   Find the following line:
   ```
   sqlalchemy.url = ...
   ```
   Replace it with your PostgreSQL URI. The format for the URI is generally:
   ```
   postgresql://[user[:password]@][host][:port][/dbname]
   ```
   For example, if you have a local PostgreSQL server with the database `mydb`, username `admin`, and password `password123`, update the line to:
   ```
   sqlalchemy.url = postgresql://admin:password123@localhost/mydb
   ```

> ❗️ Ensure that the database credentials provided have the necessary permissions for Alembic to perform migrations.

### Setting Up the Project with PDM

[PDM (Python Development Master)](https://pdm.fming.dev/latest/) is utilized for dependency management in this project. To set up and run the project:

* **Installing PDM**:
   Before you begin, ensure you have PDM installed. If not, refer to the [official documentation](https://pdm.fming.dev/latest/) to install PDM.

* **Clone the Repository**:
   Get the project source code from GitHub:
   ```bash
   git clone https://github.com/blossomlabsio/Bloom-Backend.git
   ```

* **Navigate to the Project Directory**:
   ```bash
   cd Bloom-Backend
   ```

* **Install Dependencies**:
   Use PDM to install the project's dependencies:
   ```bash
   pdm install
   ```

* **Run Migrations**:
   Create migrations with the specified message:
   ```bash
   pdm run makemigrations -m "init"
   ```

* **Apply Migrations**:
   Apply the created migrations to the database:
   ```bash
   pdm run migrate
   ```

* **Start the Project**:
   Use PDM to run the project:
   ```bash
   pdm run start
   ```
  * You can also use `pdm run dev` to start the dev server.


## Setting Up and Testing the Project

To ensure the code quality and functionality of the project, follow the steps below:

### Installing Git Hooks with `pre-commit`

Before making any commits, it's essential to ensure that your code meets the quality standards. This project utilizes `pre-commit` hooks to automatically check your changes before any commit.

Install the pre-commit hooks with the following command:

```bash
pre-commit install
```

### Running Tests

To ensure the project's functionality, you should run all the provided tests. Execute the following command to run the tests:

```bash
pdm run test
```

### Testing the Running Server

Once you have your server up and running, you can send requests to it from another terminal to test its responsiveness and functionality.

Here are a couple of `GET` requests you can make using [curl](https://curl.se/):

```bash
curl http://127.0.0.1:8000/api/v1/healthz

curl http://127.0.0.1:8000/api/v1/readyz
```

> These endpoints typically return the health status or readiness of the server, helping in diagnostics and monitoring.


# 🗒️ How to contribute

> ❗️Important: **Please read the [Code of Conduct](CODE_OF_CONDUCT.md) and go through [Contributing Guideline](CONTRIBUTING.md) before contributing to Bloom-Backend.**

* Feel free to open an issue for any clarifications or suggestions. 

* If you still need help to get started, feel free to reach out on our [community discord](https://discord.gg/8nzWAXuWN).


# 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping Bloom 🌺 grow.
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/graphs/contributors)

# 🙏 Support++

This project needs your shiny star ⭐.
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
