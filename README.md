# **Pre-Requisites to run this solution:**

**Python 3.12.2**  
**Selenium for Python selenium 4.28.1**  
**Firefox v135.0**

---

## **Background**

This solution is a sample of tests against the **Hudl login page**. This is not an exhaustive suite of tests with full coverage.  

There are **3 categories of tests**:  
- **E-mail**  
- **Password**  
- **Negative tests**  

Each test is written as an individual Python script that can be run separately or as a group. Each script can be executed using an IDE, e.g., **PyCharm**, where the browser will run maximized.

---

## **Testing Types NOT Covered**

### **Functional**
- Validation of elements such as **colour/font**, etc.  
- Further negative testing of **input fields**  
- **URL validations**  
- Grid running tests in parallel  
- Validation of other login types (e.g., **Google, Apple, Facebook**)  
- Validation of **privacy policy links**  
- Validation for **Terms of Service**  
- Validation in other browsers such as **Edge, Chrome, & Safari**  

### **Non-Functional Testing**
- **Soak testing** (performance at expected volumes)  
- **Stress testing** (beyond acceptable volumes)  

### **Security (General Penetration Testing)**  
- **XSS (Cross-Site Scripting)**  
- **CSRF (Cross-Site Request Forgery)**  
- Validation of **libraries and packages** (ensuring they are current and have zero vulnerabilities)  
- General **DDoS (rate limits)**  
- **Data compliance** (e.g., tracking cookies in line with local laws)  

### **Accessibility**  
- **Web Content Accessibility Guidelines (WCAG 2.1, 2.2, etc.)**  

### **SEO**  
- **Tracking cookies**  
- **Tags firing**  
- **Keyword/HREF lang compliance** for Google ranking  
