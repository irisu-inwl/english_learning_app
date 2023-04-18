# English Learning App

An interactive app to help you learn English more effectively.

# Setup

## Installation

To install the required dependencies, run:

```
poetry install
```

## GCP Setting

This app utilizes Google Text-to-Speech API, so you'll need to set up a GCP project. 

Follow the instructions in the official documentation: https://cloud.google.com/text-to-speech/docs/before-you-begin

You'll also need to obtain an application credential (e.g., service account key or application default credentials). 

Here's an example of how to use your ADC:

```
gcloud auth application-default login
```

from: https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login

## Set Environment Variable

Make sure to set the following environment variables before running the app:

```
export OPENAI_API_KEY=<your openai api key>
export GOOGLE_APPLICATION_CREDENTIALS=<your credential file, e.g. ~/.config/gcloud/application_default_credentials.json>
```

## Running App

To run the app, simply execute the following command:

```
poetry run streamlit run app.py
```
