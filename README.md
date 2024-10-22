# Web-Application-Vulnerabilities
## Purpose
The goal of this project is to help developers and security enthusiasts learn about and practice web application security testing. It is designed to simulate real-world vulnerabilities in a controlled environment and enable users to:
- Understand how web application vulnerabilities work.
- Experiment with various testing tools like Burp Suite.
- Learn techniques to mitigate and prevent security issues.
## Technologies Used
- **Frontend**: HTML, JavaScript
- **Backend**: Python (Flask) 
- **Database**: SQL 
- **Security Testing Tools**: Burp Suite
## Vulnerabilities Demonstrated

1. **Cross-Site Scripting (XSS)**:
   Injection of malicious scripts via user input fields (e.g., comments).
   - **Security**: Output encoding and input validation.

2. **Cross-Site Request Forgery (CSRF)**:
   Simulated unauthorized form submission via an external site.
   - **Security**: CSRF tokens for form submissions.

3. **SQL Injection**:
   Bypassing login forms through SQL injection.
   - **Security**: Use of parameterized queries and ORM (SQLAlchemy/Sequelize).
  
## Burp Suite

### Start Intercepting:

- **Intercept Tab**: In Burp Suite, navigate to the **Proxy** tab at the top, then go to the **Intercept** sub-tab. This is where Burp Suite will capture and display HTTP/S requests that your browser sends to web servers.

- **Enable Interception**: By default, interception is turned on. You can see this by checking the button that says **“Intercept is on”** at the top of the screen. If it's not on, simply click the button to toggle it on.

- **Sending Requests**: With intercept enabled, all HTTP/S requests from your browser will now be captured by Burp Suite. Open your browser and start interacting with the target web application (e.g., log in, submit forms, etc.). Each time you send a request, Burp Suite will intercept it before it reaches the server.

- **Inspecting Requests**:
  - When a request is intercepted, Burp Suite will display its contents, allowing you to view and modify data before sending it to the server.
  - You can see headers, parameters, cookies, and more.
  - If you wish to send the intercepted request as-is, click **“Forward”**. If you want to drop the request, click **“Drop”**.

### Analyze Vulnerabilities:

- **Modify Requests**: You can edit any part of the intercepted request, such as changing query parameters, input fields, or cookies. This is useful for testing for vulnerabilities like **SQL Injection**, **XSS**, or **CSRF** by injecting malicious input into fields.

- **Testing XSS**: For example, to test for **Cross-Site Scripting (XSS)**, modify a user input field by injecting a script like `<script>alert('XSS')</script>` and then forward the request to see if it gets executed by the web application.

- **Testing SQL Injection**: To test for **SQL Injection**, modify a form submission or URL parameter with an SQL payload, such as `' OR 1=1 --`, and observe the web application’s response.

### View Responses:

- After forwarding the request, Burp Suite will capture the server’s response. You can inspect this response in the **HTTP history** tab (still under **Proxy**), where every request and response pair is logged.

- Analyze the server's response to see if it behaves as expected or if the input triggered a vulnerability. For example, if the server returns an error message containing SQL information, it could indicate an SQL injection vulnerability.

### Repeating Requests:

- To easily repeat a request without intercepting it again, you can send any request from the **HTTP history** to **Repeater** (another Burp Suite tool). This lets you modify and resend the request multiple times to experiment with different payloads, without interacting with the browser.

