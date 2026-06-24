# Vulnerable Flask Web Application Demo

> ⚠️ **Educational Use Only**
>
> This project intentionally contains multiple web application security vulnerabilities for learning, security research, and penetration testing practice. **Do not deploy this application to production or expose it to the public internet.**

## Overview

This Flask application demonstrates common web security vulnerabilities, including:

* Server-Side Template Injection (SSTI)
* Cross-Site Scripting (XSS)
* Potential Remote Code Execution (RCE) through SSTI exploitation

The application is designed as a safe learning environment for security professionals, students, bug bounty hunters, and developers who want to understand how these vulnerabilities work and how they can be mitigated.

---

## Features

### Vulnerable Components

#### 1. Server-Side Template Injection (SSTI)

User input is directly injected into a Jinja2 template and rendered using:

```python
render_template_string(...)
```

Example payload:

```jinja2
{{7*7}}
```

Expected result:

```text
49
```

---

#### 2. Cross-Site Scripting (XSS)

User-controlled input is reflected back into the page without proper sanitization.

Example payload:

```html
<script>alert('XSS')</script>
```

---

#### 3. Potential Remote Code Execution (RCE)

Through SSTI exploitation, an attacker may gain access to Python objects and potentially execute arbitrary code.

Example payloads:

```jinja2
{{config}}
```

```jinja2
{{''.__class__.__mro__[1].__subclasses__()}}
```

---

## Disclaimer

This project intentionally contains insecure code.

**You are solely responsible for how you use this software.**

Never:

* Deploy to production
* Expose to the public internet
* Store sensitive information
* Use in environments containing real data

This repository exists strictly for:

* Security education
* Vulnerability research
* Capture The Flag (CTF) practice
* Penetration testing training
* Secure coding demonstrations

---

## Installation

### Prerequisites

* Python 3.8+
* pip

### Clone Repository

```bash
git clone https://github.com/yourusername/vulnerable-flask-demo.git
cd vulnerable-flask-demo
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Linux/macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install flask
```

Or:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the server:

```bash
python app.py
```

The application will be available at:

```text
http://localhost:5000
```

Because the server is configured with:

```python
app.run(host='0.0.0.0', port=5000, debug=True)
```

it can also be accessed from other devices on the same network.

---

## Example Vulnerability Tests

### SSTI

Input:

```jinja2
{{7*7}}
```

Output:

```text
49
```

---

### XSS

Input:

```html
<img src=x onerror=alert('XSS')>
```

Result:

```text
JavaScript executes in the browser
```

---

### Configuration Disclosure

Input:

```jinja2
{{config}}
```

Result:

```text
Application configuration displayed
```

---

## Learning Objectives

By studying this project, you can learn:

* How Jinja2 template injection works
* Why `render_template_string()` can be dangerous
* The risks of unsanitized user input
* XSS attack vectors
* Python object introspection techniques
* Secure coding practices in Flask
* Common web application attack chains

---

## Secure Coding Recommendations

### Prevent SSTI

Avoid rendering user-controlled data as template code.

Unsafe:

```python
render_template_string(user_input)
```

Safer:

```python
render_template("index.html", name=user_input)
```

---

### Prevent XSS

Escape user input before rendering:

```html
{{ name }}
```

Use Flask/Jinja2 auto-escaping and avoid disabling it unless absolutely necessary.

---

### Disable Debug Mode

Never run production systems with:

```python
debug=True
```

Instead:

```python
debug=False
```

---

## Project Structure

```text
.
├── app.py
├── README.md
└── requirements.txt
```

---

## Educational Resources

Topics worth researching:

* OWASP Top 10
* Server-Side Template Injection
* Cross-Site Scripting (XSS)
* Flask Security Best Practices
* Jinja2 Template Security
* Secure Input Validation
* Content Security Policy (CSP)

---

## License

This project is provided for educational purposes only.

Use at your own risk.

---

## Author

Created as a vulnerable-by-design Flask application to demonstrate common web security issues and secure coding lessons.
