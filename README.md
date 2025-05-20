# HTTP/S-debugger

This is an HTTP/S service debugger and recon tool. Which can be used to test for response latency from a web service and inspect HTML/DOM structure for malicious code. This repository includes a powerpoint representation of why I made this project and my experience making it, along with a demo of said project.


## 📄 License

MIT License — see [LICENSE](LICENSE) for details.


## 📜 Table of Contents

- [Features](#Features)
- [Usage](#Usage)
- [Presentation](#Presentation)
- [Requirements](#Requirements)
- [Installation](#Installation)


# Features

- Testing connection speeds automatically upon successful connection with a legitimate site. If a site does not appear legitimate towards the internet or is not accepting connections, the website will said to be an invalid choice.

- Connections can be performed on port 80 and port 443. Why both if most websites and browsing solutions force encrypted connections? To test for proper rerouting of services and incase a web service is only accepting connections to port 80. When selecting port 443 the SSL certificate will be grabbed automatically.

- The tool will display HTTP packet information in a neat, organized manner. After choosing to test port 80 or 443 connections and responding to the prompt to display the said packet information.

- The tool can reuse the socket address for performing multiple connection tests in one go, rather than having to wait for the standard "TIME_WAIT" state for the TCP protocol.


# Usage

The intended usage of this tool is to be a lightweight, catered CLI tool designed for quick testing of website responsiveness, HTTP content, legitimacy (to some extent), and to review the safety of the source code of a website for malicious payloads without exposing the user to danger as the source code can be effectively viewed as text in a Pythonic environment. 


# Presentation

For a presentation/demo of the project [CLICK ME](https://1drv.ms/p/c/8d3e98d829540707/ESvu3V1S6vJGjr9dlvnkVU0BGHtKPD3NyqD_e2FWwZP65Q?e=okM3HH).


# Requirements

- Make sure you are using a system compatible with the tool. The tool is pretty much compatible with most modern systems where socket access is available to the user (Linux, Windows, MacOS).

- Make sure that the latest version of Python3 is installed and utilized for the best performance. And that the requests library is properly installed in your dedicated REPL. Other libraries utilized are standard libraries and will not have to be manually installed.


# Installation

- Due to how lightweight the operations of this tool are, multiple files are not needed for installation. Instead, the dedicated file for this tool is to be installed. Which can then be executed with a dedicated Windows REPL environment (Python3 console or dedicated graphical REPL) or a dedicated Linux REPL environment (python3 HTTP_Debugger.py). The requests library will also need to be installed for this tool to function (pip install requests).


### 🔖 Tags

`#python` `#cybersecurity` `#networking` `#http` `#OSINT` `#cli-tools`

