from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Intentionally vulnerable template with SSTI and XSS
VULNERABLE_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerable Demo Site - Educational Purpose</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        .warning {
            background: #fff3cd;
            border: 2px solid #ffc107;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        form {
            margin: 20px 0;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin: 20px 0;
            padding: 15px;
            background: #e7f3ff;
            border-left: 4px solid #007bff;
        }
        .vulnerability-info {
            background: #f8d7da;
            border: 2px solid #f5c6cb;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Vulnerable Web Application Demo</h1>
        
        <div class="warning">
            ⚠️ <strong>WARNING:</strong> This application contains intentional security vulnerabilities for educational purposes only.
            Never deploy this in a production environment!
        </div>

        <div class="vulnerability-info">
            <h3>🔴 Known Vulnerabilities:</h3>
            <ul>
                <li><strong>Server-Side Template Injection (SSTI)</strong> - Template rendering without sanitization</li>
                <li><strong>Cross-Site Scripting (XSS)</strong> - User input reflected without escaping</li>
                <li><strong>Remote Code Execution (RCE)</strong> - Possible via SSTI exploitation</li>
            </ul>
        </div>

        <h2>Test Form</h2>
        <form method="POST" action="/">
            <label for="name">Enter your name or test payload:</label>
            <input type="text" id="name" name="name" placeholder="Try: {{7*7}} or <script>alert('XSS')</script>">
            <button type="submit">Submit</button>
        </form>

        {% if name %}
        <div class="result">
            <h3>Result:</h3>
            <!-- VULNERABILITY 1: XSS - Direct output without escaping -->
            <p>Raw output: {{ name }}</p>
            
            <!-- VULNERABILITY 2: SSTI - Template injection point -->
            <p>Processed: ''' + name + '''</p>
        </div>
        {% endif %}

        <h3>🧪 Test Payloads:</h3>
        <ul>
            <li><strong>SSTI Test:</strong> <code>{{7*7}}</code> (should show 49)</li>
            <li><strong>SSTI RCE:</strong> <code>{{config}}</code> or <code>{{''.__class__.__mro__[1].__subclasses__()}}</code></li>
            <li><strong>XSS Test:</strong> <code>&lt;script&gt;alert('XSS')&lt;/script&gt;</code></li>
            <li><strong>XSS Alternative:</strong> <code>&lt;img src=x onerror=alert('XSS')&gt;</code></li>
        </ul>

        <h3>📚 Learning Resources:</h3>
        <p>Research these vulnerabilities to understand:</p>
        <ul>
            <li>How SSTI can lead to RCE</li>
            <li>Python object introspection for exploitation</li>
            <li>XSS prevention techniques (escaping, CSP)</li>
            <li>Secure template rendering practices</li>
        </ul>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    name = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
    
    # CRITICAL VULNERABILITY: render_template_string with user input
    # This allows SSTI which can lead to RCE
    return render_template_string(VULNERABLE_TEMPLATE, name=name)

if __name__ == '__main__':
    # Run in debug mode for educational purposes
    print("\n" + "="*60)
    print("🔴 VULNERABLE APPLICATION - EDUCATIONAL USE ONLY 🔴")
    print("="*60)
    print("This app contains intentional security vulnerabilities:")
    print("- Server-Side Template Injection (SSTI)")
    print("- Cross-Site Scripting (XSS)")
    print("- Remote Code Execution (RCE) via SSTI")
    print("\nNEVER deploy this to a public server!")
    print("="*60 + "\n")
    
    # Bind to 0.0.0.0 to allow external access on DigitalOcean
    app.run(host='0.0.0.0', port=5000, debug=True)
