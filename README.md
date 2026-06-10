---
base_model: failspy/Meta-Llama-3-8B-Instruct-abliterated-v3
language:
- es
- en
library_name: transformers
tags:
- devops
- uncensored
- abliterated
- llama-3
- agents
- orchestrator
- system-management
- code-generation
- android
- windows
- linux
license: mit
datasets: []
metrics: []
---

# 🚀 DevOps Senior AI Orchestrator (Uncensored)

> **"De la Palabra a la Acción: Automatización de Sistemas sin Restricciones"**

Este proyecto es un sistema de orquestación de IA de vanguardia que combina la potencia de **Llama-3-8B (Abliterated)** con agentes especializados para transformar peticiones en lenguaje natural en acciones reales sobre tu sistema operativo. Diseñado para ser el compañero definitivo de un DevOps Senior, funciona de forma nativa en **Android (Termux)**, **Windows** y **Linux**.

---

## 🌟 Características Principales

| Característica | Descripción |
| :--- | :--- |
| **🧠 Orquestador Central** | Inteligencia que descompone peticiones complejas en planes de ejecución lógicos. |
| **🛡️ Agentes Especializados** | Equipos de SysAdmin, Developer y Auditor trabajando en paralelo. |
| **🔓 Sin Censura** | Basado en modelos *abliterated* para garantizar respuestas directas y sin restricciones. |
| **📱 Multiplataforma** | Un único núcleo compatible con Termux, PowerShell y Bash. |
| **🛠️ Modificación Real** | Capacidad de ejecutar comandos de sistema y generar código funcional. |

---

## 🏗️ Arquitectura del Sistema

El sistema opera bajo un modelo de delegación inteligente:

1.  **Input:** Recibe una orden en lenguaje natural (ej: *"Configura un cluster Docker"*).
2.  **Análisis:** El orquestador identifica las dependencias y el sistema operativo.
3.  **Delegación:** 
    *   **SysAdmin Agent:** Genera los comandos de infraestructura.
    *   **Developer Agent:** Escribe los scripts de automatización necesarios.
    *   **Auditor Agent:** Valida la seguridad y sintaxis antes de la ejecución.
4.  **Ejecución:** Los cambios se aplican mediante la interfaz `SystemTools`.

---

## 🚀 Inicio Rápido

### 1. Requisitos Previos
*   Python 3.11+
*   Token de Hugging Face (para descarga del modelo base)

### 2. Instalación
```bash
git clone https://huggingface.co/N11100/devops-orchestrator-ai
cd devops-orchestrator-ai
sudo pip3 install -r requirements.txt
```

### 3. Configuración
Crea un archivo `.env` con tu token:
```text
HF_TOKEN=tu_token_aqui
```

### 4. Ejecución
```bash
python3 orchestrator.py
```

---

## 🛡️ Seguridad y Auditoría

A pesar de ser un modelo **Uncensored**, el sistema incluye un **Agente Auditor** que actúa como una capa de seguridad técnica. Este agente revisa:
*   ✅ **Sintaxis:** Comandos válidos para el shell actual.
*   ✅ **Riesgos:** Identificación de comandos destructivos accidentales.
*   ✅ **Validación:** El usuario tiene la última palabra antes de ejecutar cambios críticos.

---

## 📂 Estructura del Proyecto
*   `orchestrator.py`: Núcleo del sistema y lógica de agentes.
*   `system_tools.py`: Interfaz de bajo nivel con el sistema operativo.
*   `requirements.txt`: Dependencias necesarias.
*   `setup.py`: Script de instalación y empaquetado.

---

## 🤝 Contribuciones e Instrucciones de Modificación
Este proyecto es altamente extensible. Puedes añadir nuevas herramientas en `system_tools.py` o refinar los prompts de los agentes en `orchestrator.py` para adaptar el sistema a tus necesidades específicas.

**Licencia:** [MIT](https://opensource.org/licenses/MIT)
