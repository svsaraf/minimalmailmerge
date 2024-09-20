# Gmail Draft Creator

This is a simple Python script that connects to your Gmail inbox and creates a draft message templatized with Jinja2. This script creates one draft per row in the CSV, so can create 100s of drafts at once. 

I find that creating gmail drafts is better than sending emails directly, because it gives an intermediate place (the draft view) where I can customize or modify drafts before they are sent. 

## Prerequisites

- Python 3.x installed on your machine.
- Basic knowledge of how to run Python scripts.

## Getting Started

### Step 1: Obtain `credentials.json`

Since this script is for use within our company, you can obtain the `credentials.json` file directly from Sanjay. This file contains the necessary credentials to access the Gmail API. I will wormhole it to you.

### Step 2: Clone the repo and install the python libraries

```bash
    git clone git@github.com:svsaraf/minimalmailmerge.git
    cd minimalmailmerge
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```

### Step 3: Copy credentials.json into the project folder

### Step 4: Update template.txt

template.txt contains the email draft you'd like to send. Surround variables with {{ double_brackets }}. Since it's a Jinja template you can also use if statements, loops, etc.

Here's an example:
```
Hi {{ recipient_name | default("Guest") }},

This is a message generated using Jinja2!

Best regards,
{{ sender_name | default("Your Name") }}
```

### Step 5: Update template_vars.csv

For each row in the csv, one email will be drafted. The mandatory columns in template_vars.csv include recipient_name,recipient_email,subject. The other variables are optional and you can add more. 

I've included an example template_vars file, so if you want to just test this script, rename template_vars_example.csv to template_vars.csv.

### Step 6: Run the script

```
    python gmail_draft.py
```

A browser window will open, prompting you to log in to your Google account and authorize the application. Once authorized, a token.json file will appear in the folder. 

The script will then create drafts in your Gmail account, one draft per row in the CSV.
