---
title: "TryHackMe - SnykCode writeup"
date: 2024-06-21
categories:
  - Easy
tags:
  - N/A
---

This is a INFO room from [TryHackMe](https://www.tryhackme.com/) and this room can be found @ https://tryhackme.com/r/room/snykcode. 
Key lessons learnt here:    
    Identify security vulnerabilities and understand the significance of integrating security testing throughout the SDLC <br>
    Set up, configure, and use Snyk Code for analysing codebases and discovering potential issues <br>
    Remediate discovered vulnerabilities by applying recommended fixes <br>
    Measure the impact of a security tool implementation via calculating returns on investment <br>


## Task 3 Understanding Code Security Risks

How many dependencies do we have for this new feature?
```
3
```

##  Task 4 Getting Started With Snyk Code
How many vulnerabilities are flagged on the search-feature.js file?
```
4
```
How many high-severity vulnerabilities are flagged on the search-feature.js file?
```
2
```
What are the two medium-severity vulnerabilities flagged on the search-feature.js file? (in alphabetical order)
```
Cross-Site Request Forgery, Information Exposure
```


## Task 5 Diving Deeper Into Vulnerabilities

What is the CWE for Cross-site Scripting?
```
CWE-79
```
What is the CWE for SQL injection?

```
CWE-89
```

What is the unsanitised user input in the chat-controller.js file?
```
searchTerm
```

## Task 6 Remediating Vulnerabilities

What is the new vulnerability introduced with the XSS fix?
```
Allocation of Resources Without Limits or Throttling
```

Which Express method is used to fix the XSS vulnerability in the code snippet?
```
res.render
```

What is the updated code in the code snippet using to fix the SQL injection?
```
parameterised queries
```

## Task 7 CI/CD Pipelines Automation & Continuous Monitoring

Establishing sensible alert thresholds in continuous monitoring practices involves considering the severity, frequency, and rate of change of vulnerabilities. (y/n)
```
y
```


## Task 8 Establishing Best Practices

Which OWASP framework serves as a guide to strengthen the relationship between development teams and information security teams?
```
OWASP security shampion playbook
```
