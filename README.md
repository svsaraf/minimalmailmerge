# Gmail Draft Creator

This is a simple Python script that connects to your Gmail inbox and creates a draft with the message "Hello World" using the Gmail API.

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of how to run Python scripts.

## Getting Started

### Step 1: Obtain `credentials.json`

Since this script is for use within our company, you can obtain the `credentials.json` file directly from Sanjay. This file contains the necessary credentials to access the Gmail API. I will wormhole it to you.

### Step 2: Clone the repo and install the python libraries

```bash
    git clone <repo_name>
    cd <repo_name>
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

### Step 3: Copy credentials.json into the project folder

### Step 4: Run the script

```
    python gmail_draft.py
```

A browser window will open, prompting you to log in to your Google account and authorize the application. Once authorized, the script will create a draft in your Gmail account.

---

Next thing to add is the capability of creating a CSV and then auto writing drafts. 