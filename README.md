# Bloom 🌺 : A Self-Hosted CFP portal for Events.

<hr>
A Backend Server Written in 🐍 and FastAPI with 🐘 DB that powers the Self-Hosted CFP Management Service Bloom.

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

# Pre-requisites

`python3.9.x`
`pip`
`postgres`

# Development Setup

- <h3> Local setup 🛠️ without Docker 🐳 </h3>
  <p>
  We are using <a href="https://pdm.fming.dev/latest/"> PDM </a> to manage depency for the project, so you need to install pdm to use this project.
  </p>

```commandline
# clone the repository
git clone https://github.com/blossomlabsio/Bloom-Backend.git

# Change Directory to the Project

cd Bloom-Backend

# Install Dependency

pdm install

# Run Migrations

pdm run makemigrations "init"

# Make Migrations

pdm run migrate

# Run the Project

pdm run start
```

## 💪 Thanks to all Wonderful Contributors

Thanks a lot for spending your time helping Bloom 🌺 grow.
Thanks a lot! Keep rocking 🍻

[![Contributors](https://contrib.rocks/image?repo=blossomlabsio/Bloom-Backend)](https://github.com/blossomlabsio/Bloom-Backend/graphs/contributors)

## 🙏 Support++

This project needs your shiny star ⭐.
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
