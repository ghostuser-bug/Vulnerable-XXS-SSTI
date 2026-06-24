```
# Vulnerable Flask Web Application Demo

> ⚠️ **Educational purpose only**  
> This project intentionally contains web security vulnerabilities for learning and testing in a controlled environment.

## Overview

This is a deliberately vulnerable Flask web application designed to demonstrate common web security issues such as:

- Server-Side Template Injection (SSTI)
- Cross-Site Scripting (XSS)
- Unsafe template rendering
- Potential Remote Code Execution through template injection

The goal of this project is to help students, beginners, and security learners understand how insecure coding patterns can introduce serious vulnerabilities in web applications.

## Important Warning

**Do not deploy this application to a public server.**

This application is intentionally insecure. Running it on the public internet may expose your server, files, environment variables, and system resources to attackers.

Use this project only in:

- Localhost environments
- Private labs
- Virtual machines
- CTF-style practice environments
- Isolated cloud instances with strict firewall rules

## Features

- Simple Flask web interface
- User input form
- Intentionally vulnerable template rendering
- Demonstrates reflected XSS
- Demonstrates SSTI behavior
- Includes educational warnings and vulnerability descriptions

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2 templates

## Project Structure

```

.

├── [app.py](http://app.py)

├── requirements.txt

└── [README.md](http://README.md)

```

## Installation

### 1. Clone the repository

```

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

cd YOUR-REPOSITORY

```

### 2. Create a virtual environment

```

python3 -m venv venv

```

### 3. Activate the virtual environment

#### Linux / macOS

```

source venv/bin/activate

```

#### Windows

```

venvScriptsactivate

```

### 4. Install dependencies

```

pip install -r requirements.txt

```

If you do not have a `requirements.txt` file yet, create one with:

```

Flask

```

## Running the Application

```

python [app.py](http://app.py)

```

By default, the application runs on:

```

http://127.0.0.1:5000

```

If the app is configured to bind to all interfaces:

```

[app.run](http://app.run)(host="0.0.0.0", port=5000, debug=True)

```

then it may also be accessible from other devices on the same network.

Again, **do not expose this app publicly**.

## Example Test Payloads

### Basic SSTI Test

Enter this into the form:

```

{{7*7}}

```

If the application is vulnerable, the output may evaluate the expression and display:

```

49

```

### Basic XSS Test

Enter this into the form:

```

<script>alert('XSS')</script>

```

If the application reflects input unsafely, the browser may execute the script.

### HTML Injection Test

```

<h1>Hello from user input</h1>

```

This demonstrates how unescaped user input can affect page rendering.

## Vulnerabilities Demonstrated

### 1. Server-Side Template Injection

Server-Side Template Injection happens when user-controlled input is inserted into a server-side template and rendered as template code.

In Flask, unsafe use of `render_template_string()` can allow user input to be interpreted by the Jinja2 template engine.

Example vulnerable pattern:

```

return render_template_string(template_with_user_input)

```

A safer approach is to avoid building templates directly from user input.

### 2. Cross-Site Scripting

Cross-Site Scripting happens when user input is rendered in a webpage without proper escaping or sanitization.

Example dangerous behavior:

```

<p>User input appears here without safe handling</p>

```

An attacker could inject JavaScript into the page if input is not escaped correctly.

### 3. Debug Mode Risk

Running Flask with debug mode enabled can be dangerous in production.

```

[app.run](http://app.run)(debug=True)

```

Debug mode should only be used during local development.

## Safer Coding Practices

To prevent these issues in real applications:

- Do not concatenate user input into templates
- Do not use `render_template_string()` with untrusted input
- Use normal template files with safe variable passing
- Keep autoescaping enabled
- Validate and sanitize user input
- Disable debug mode in production
- Use a Content Security Policy where appropriate
- Never expose intentionally vulnerable apps to the public internet

## Example Secure Pattern

Instead of rendering user input as part of a template string, pass it safely as a variable:

```

from flask import Flask, request, render_template

app = Flask(**name**)

@app.route("/", methods=["GET", "POST"])

def index():

name = ""

if request.method == "POST":

name = request.form.get("name", "")

return render_template("index.html", name=name)

```

And in the template:

```

<p>Hello, {{ name }}</p>

```

Jinja2 escapes variables by default in HTML templates, which helps prevent XSS.

## requirements.txt

```

Flask

```

## Disclaimer

This project is intentionally vulnerable and is provided for educational purposes only.

The author is not responsible for any misuse, damage, unauthorized access, or illegal activity caused by using this project.

Use responsibly and only in environments where you have permission.

## License

This project is released for educational use. You may modify and use it for learning, demonstrations, or security training labs.
```
