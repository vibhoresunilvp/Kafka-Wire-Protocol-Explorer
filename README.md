# 🚀 TinyKafka — A Minimal Kafka Protocol Server (Codecrafters Challenge)

[![progress-banner](https://backend.codecrafters.io/progress/kafka/e0f8ca2a-732b-4687-817a-19928d8f9262)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This repository contains my implementation for the **Codecrafters “Build Your Own Kafka” challenge**—with a personal twist.  
The goal is to build a tiny Kafka-compatible server from scratch, explore Kafka’s internals, and decode the binary wire protocol byte by byte.

Throughout this project, I work through:

- 🧩 Kafka’s low-level **wire protocol**  
- 🔍 Parsing structured binary messages  
- 🔄 Handling **APIVersions** and **Fetch** requests  
- ⚡ Implementing event loops and TCP networking  
- 🧵 Working with raw Python sockets  
- 🛠 Building proper Kafka-style request/response structures  

This is not a full Kafka clone. Instead, it’s a **learning-focused micro-broker** designed to reveal how Kafka works under the hood.

---

## 📂 Project Overview

The core implementation lives in:
    📂 app -> main.py