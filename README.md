# Omni WebUI

Omni-WebUI (OI) is a web-based user interface for the Chatbot. It is currently built
upon Open WebUI.

## Installation

```bash
pip install omni-webui
```

OR

```bash
pip install git+https://github.com/omni-webui/omni-webui.git
```

## Setup development environment

### Pre-requisites

1. [`uv`](https://docs.astral.sh/uv/)
2. [`deno`](https://deno.land/)

### Steps

First, clone the repository:

```bash
git clone https://github.com/omni-webui/omni-webui.git
```

Then, install the dependencies, `uv` is required (for read frontend files from cache):

```bash
uv sync
```

Build the whole project, you don't need to do `deno task build` because `uv build` will do it for you:

```bash
uv build
```

Run the development server:

```bash
uv run omni-webui serve --reload
```

Install git hooks:

```bash
uv run pre-commit install && uv run pre-commit install --hook-type commit-msg
```

## Frequently Asked Questions

### What is Omni WebUI? What is Open WebUI? What is the difference?

Omni-WebUI (OI) is a web-based user interface for the Chatbot. It is currently built upon [Open WebUI](https://github.com/open-webui/open-webui). But Omni-WebUI is not a fork of Open WebUI. It is a separate project that uses Open WebUI as a dependency. The main difference between the two is that Omni-WebUI is focused on simplicity, reliability and stability.

### Why should I use Omni WebUI instead of Open WebUI?

In most cases, you could use Open WebUI instead of Omni WebUI. However, if you are looking for a more flexible and extensible solution, Omni WebUI is the way to go. It is designed to be easy to use and easy to extend. It is also more reliable and stable than Open WebUI.

### How did I do Omni WebUI?

Since Open WebUI is a dependency of Omni WebUI, I did not have to do much.
FastAPI would use the entry point firstly registered by Omni WebUI, and then Open WebUI.
Therefore, I can easily override the default behavior of Open WebUI by registering my own entry point.

Frontend is a bit different. I copy the frontend files from Open WebUI and modify them to fit my needs.

## How to contribute

GitHub PRs are the way to go. Please make sure to write tests for your code and
run the tests before submitting a PR.
