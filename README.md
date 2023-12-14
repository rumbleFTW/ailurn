# Ailurn: **_A new way to read Research papers!_**

![Screenshot](https://github.com/rumbleFTW/ailurn/assets/85807431/53e11f20-c918-418e-a4d5-76e91d70e69e)

## Podcast from PDF Research Papers

This Python project aims to create an AI-powered podcast generator that utilizes research papers in PDF format. Ailurn converts the text content of research papers into spoken words, allowing users to listen to research papers as podcasts.

#### Features

    - Convert PDF research papers into spoken audio.
    - Customize voice and language preferences.
    - Generate podcasts for offline listening.

#### Running Locally

To run the Ailurn locally, follow these steps:

1. Prerequisites

   Make sure you have the following installed on your machine:
   i. Python 3.x
   ii. PIP (Python package installer)

2. Installation

   i. Clone the repository:

   ```bash
       git clone https://github.com/rumbleFTW/ailurn.git
       cd ailurn
   ```

   Also create a .env file in ailurn/src/ and include GOOGLE_API_KEY=<YOUR_KEY_HERE>

   ii. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

   iii. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   iv. Run the application

   ```bash
   python app.py
   ```

   v. Access the application at in your web browser.

   Follow the on-screen instructions to choose a research paper and customize the podcast settings.
