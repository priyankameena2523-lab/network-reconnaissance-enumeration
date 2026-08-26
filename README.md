
# Network Reconnaissance and Enumeration Using Nmap

## Project Overview

Network Reconnaissance and Enumeration is a cybersecurity project developed to identify open ports, running network services, and service versions on a target system.

The project uses Nmap for network scanning and a Python Tkinter-based graphical interface to make the scanning process simple and user-friendly.

The project was developed and tested in an isolated virtual cybersecurity lab using Kali Linux and Metasploitable 2.

## Objectives

- Discover open ports on a target system.
- Identify services running on open ports.
- Detect service and software versions.
- Provide a simple graphical interface for running Nmap scans.
- Understand the basic process of network reconnaissance and enumeration.

## Technologies Used

- Python
- Tkinter
- Nmap
- Kali Linux
- Metasploitable 2
- Oracle VirtualBox

## Project Architecture

Kali Linux acts as the scanning machine, while Metasploitable 2 is used as the target machine in an isolated virtual network.

```text
Kali Linux
192.168.56.20
      |
      | Nmap Scan
      |
      v
Metasploitable 2
192.168.56.10
      |
      v
Open Ports
Services
Service Versions
