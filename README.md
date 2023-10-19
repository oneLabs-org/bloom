# Bloom 🌺 : A Self-Hosted CFP portal for Events.

<hr>
A Backend Server Written in 🐍 and FastAPI with 🐘 DB that powers the Self-Hosted CFP Management Service Bloom.

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)
[![GitHub issues](https://img.shields.io/github/issues/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend)
[![GitHub forks](https://img.shields.io/github/forks/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend)
[![GitHub stars](https://img.shields.io/github/stars/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/stargazers)
[![GitHub license](https://img.shields.io/github/license/blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/blossomlabsio/Bloom-Backend)
<br>

<hr>
<p align="center">
    <img width="320" height="320" src="artwork/4388667.png" alt="Material Bread logo">
</p>

# 🤔 Pre-requisites

`python3.9.x`
`pdm`
`postgres`

# 📦 Setup

- <h3> Local setup 🛠️ without Docker 🐳 </h3>
  <p>
  We are using <a href="https://pdm.fming.dev/latest/"> PDM </a> to manage depency for the project, so you need to install pdm to use this project.
  </p>
  <br>

  - Create a .env file and add these following variables with there respective values in it.

  ```env
  SQLALCHEMY_DATABASE_URI="YOUR POSTGRES URI"
  JWT_SECRET="YOUR JWT SECRET"
  JWT_ALGORITHM="YOUR JWT ALGORITHM"
  ACCESS_TOKEN_EXPIRY_MINUTES=YOUR ACCESS TOKEN EXPIRE TIME(INT)
  ```

  - Add POSTGRES 🐘 URI in alembic.ini

  ```ini
    63. sqlalchemy.url = YOUR_POSTGRES_URI
  ```

```commandline
# clone the repository
git clone https://github.com/blossomlabsio/Bloom-Backend.git

# Change Directory to the Project
cd Bloom-Backend

# Install Dependency
pdm install

# Run Migrations
pdm run makemigrations -m "init"

# Make Migrations
pdm run migrate

# Run the Project
pdm run start
```

## 🐍 Python Version Support

This project is compatible with the following Python versions:

> Python >= 3.9

It is recommended to use the latest version of Python for the best performances.

Please make sure you have the correct version of Python installed before starting to use
this project. You can check your Python version by running the following command in your
terminal:

```bash
python --version
```

## 🗒️ How to contribute

### 🏁 Get started

Please read the [code of conduct](https://github.com/blossomlabsio/Bloom-Backend/blob/main/CODE_OF_CONDUCT.md) and go through [CONTRIBUTING.md](https://github.com/blossomlabsio/Bloom-Backend/blob/main/CONTRIBUTING.md) before contributing to Bloom-Backend.

Feel free to open an issue for any clarifications or suggestions.

If you still need help to get started, feel free to reach out on our [community discord](https://discord.gg/8nzWAXuWN).

### ⚙️ To Develop Locally

1. Install the development dependencies: `pdm install`

2. Install the pre-commit git hooks: `pre-commit install`

3. Run `pdm run start` to start the server or `pdm run dev` to start the dev server.

4. Run `pdm run test`. This will run all the tests.

You can then request the server you ran from an other terminal. Here is a `GET` request done using [curl](https://curl.se/) for example:

```bash
curl http://127.0.0.1:8000/api/v1/healthz
```

or

```bash
curl http://127.0.0.1:8000/api/v1/readyz
```

## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping Bloom 🌺 grow.
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/graphs/contributors)

## 🙏 Support++

This project needs your shiny star ⭐.
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
