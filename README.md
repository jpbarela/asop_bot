# ASOP Bot

ASOP Bot is a simple repo designed to teach actuaries about the use of embeddings in Large Language Models(LLMs).
The repo builds a simple chat bot based off the US Actuarial Standards of Practice.

## Dependencies

For the quick start, users will need to have [Docker](https://www.docker.com/) and an
[OpenAI API key](https://platform.openai.com/account/api-keys). The OpenAI API key will need to be loaded into an
environmental variable `OPENAI_API_KEY`. This key is only used to communicate with OpenAI and is not sent to any other
service.

Users who have `make` installed on their system, most Linux machines and MacOs users, will be able to

Users who want to experiment with the code will also need Python installed and the [Poetry](https://python-poetry.org/).

## Installation

The quickest way to get started is to run `make` or `docker compose up`. These commands bring up a working instance of
the ASOP Bot and associated database. The bot can be accessed at [http://localhost:8501](http://localhost:8501).

## Components

The ASOP Bot is made up of several different components. Each component has more information about the design of the
component in a separate README but a high level description is provided here.

### ASOP Bot

The ASOP Bot is the main interface. It is currently powered by [Streamlit](https://streamlit.io/),
[Langchain](https://python.langchain.com/docs/get_started/introduction.html) OpenAI.

## Troubleshooting
