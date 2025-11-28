🚀 Project Title & Tagline
===========================
### TranWall: A Comprehensive Network Traffic Analysis and Firewall System 🚫
TranWall is an innovative, AI-powered network traffic analysis and firewall system designed to provide unparalleled protection and insights into your network's traffic patterns. With its robust feature set and user-friendly interface, TranWall is the ultimate solution for network administrators and security professionals seeking to bolster their network's defenses.

📖 Description
---------------
TranWall is a Python-based project that leverages the power of machine learning and data analysis to identify and block malicious traffic patterns. The system consists of multiple components, including a network traffic capture module, a machine learning-based anomaly detection engine, and a user-friendly graphical interface. By utilizing the popular Scapy library for packet capture and analysis, TranWall provides a comprehensive view of network traffic, enabling administrators to make informed decisions about their network's security.

The project's primary goal is to develop a robust and scalable network traffic analysis and firewall system that can be easily integrated into existing network infrastructures. With its modular design and flexible architecture, TranWall can be tailored to meet the specific needs of various organizations, from small businesses to large enterprises. By providing a transparent and customizable solution, TranWall empowers network administrators to take control of their network's security and stay one step ahead of emerging threats.

The TranWall project is built on top of a robust tech stack, including Python, Scapy, and various machine learning libraries. The system's architecture is designed to be highly scalable, allowing it to handle large volumes of network traffic with ease. With its intuitive interface and comprehensive feature set, TranWall is an ideal solution for organizations seeking to enhance their network's security and performance.

This project integrates:
------------------------
- A Transformer neural network for intrusion detection
- Real-time packet capture using Scapy
- Autonomous IP blocking using Linux iptables
- A live Streamlit dashboard for monitoring flows, alerts, and blocked hosts

It functions as a modern Intelligent Network Intrusion Prevention System (NIPS), capable of identifying malicious flows and instantly mitigating threats.
  
✨ Features
-----------
The following features are included in the TranWall project:
1. **Network Traffic Capture**: Utilizes Scapy to capture and analyze network traffic in real-time.
2. **Machine Learning-Based Anomaly Detection**: Employs machine learning algorithms to identify and flag suspicious traffic patterns.
3. **Graphical User Interface**: Provides a user-friendly interface for administrators to monitor and manage network traffic.
4. **Customizable Rules Engine**: Allows administrators to define custom rules for traffic filtering and blocking.
5. **Real-Time Alerts and Notifications**: Sends alerts and notifications to administrators when suspicious activity is detected.
6. **Comprehensive Logging and Reporting**: Generates detailed logs and reports for network traffic and system activity.
7. **Scalable Architecture**: Designed to handle large volumes of network traffic with ease.
8. **Integration with Popular Security Tools**: Supports integration with popular security tools and platforms.
9. **Automatic Updates and Patching**: Ensures the system stays up-to-date with the latest security patches and updates.
10. **Multi-Platform Support**: Compatible with various operating systems, including Windows, Linux, and macOS.

🏛️Architecture
      ┌───────────────┐
      │ capture.py    │  ---> Captures packets using Scapy
      └───────▲───────┘
              │ flows
              ▼
   ┌───────────────────────┐
   │ defender.py (ML Model)│ ---> Classifies flow: Benign / Malicious
   └───────────▲───────────┘
               │ malicious IP
               ▼
     ┌──────────────────────┐
     │ blocker.py (iptables)│ ---> Adds DROP rules
     └───────────┬──────────┘
                 │ logs
                 ▼
   ┌──────────────────────────┐
   │ firewall_log.csv         │
   └──────────────────────────┘
                 │
                 ▼
    ┌────────────────────────┐
    │ Streamlit Dashboard    │
    └────────────────────────┘


🧰 Tech Stack Table
--------------------------------------------
| Component        | Technology            |
|------------------|-----------------------|
| Frontend         | Streamlit             |
| Backend          | Python, Scapy         |
| Machine Learning | PyTorch, Scikit-Learn |
| Database         | CSV, Pandas           |
| Operating System | Windows, Linux, macOS |
| Security Tools   | KaggleHub, Scapy      |
--------------------------------------------

📁 Project Structure
-------------------
The project is organized into the following folders and files:
* `capture.py`: Network traffic capture and analysis module.
* `tranwall_cli.py`: Command-line interface for administrators to manage network traffic.
* `download_unsw.py`: Script to download the UNSW-NB15 dataset for machine learning model training.
* `tranwall_gui.py`: Graphical user interface for administrators to monitor and manage network traffic.
* `defender.py`: Machine learning-based anomaly detection engine.
* `blocker.py`: Module responsible for blocking suspicious traffic patterns.
* `show_stats.py`: Script to display network traffic statistics and reports.
* `results/`: Folder containing log files and reports generated by the system.
* `models/`: Folder containing trained machine learning models.

project-root/
│
├── capture/ # Live packet & flow capture module
├── firewall/ # ML defender + blocking engine
├── gui/ # Streamlit dashboard
├── model/ # Training/testing notebooks and model weights
├── results/ # Logs, snapshots, confusion matrix exports
└── data/ # UNSW-NB15 dataset (excluded from Git)

📈Training Performance (Real Woeld)
----------------------------
| Metric     | Score       |
|------------|-------------|
| Accuracy   | 87.52 %     |
| Precision  | 98.49 %     |
| Recall     | 82.94 %     |
| F1 Score   | 90.05 %     |
----------------------------
confusion Matrix
-----------------

<img width="692" height="482" alt="image" src="https://github.com/user-attachments/assets/054282aa-c0f1-4216-84ae-0e4d6a7c43b4" />



⚙️ How to Run
---------------

To run the TranWall project, follow these steps:
1. **Setup**: Install the required dependencies, including Python, Scapy, and PyTorch.
2. **Environment**: Configure the system's environment variables to point to the project's root directory.
3. **Build**: Run the `tranwall_cli.py` script to build and initialize the system.
4. **Deploy**: Deploy the system on a network interface or virtual machine.
5. **Configure**: Configure the system's settings and rules engine to suit your organization's needs.

🧪 Testing Instructions
----------------------
To test the TranWall project, follow these steps:
1. **Unit Testing**: Run the `unittest` module to test individual components and functions.
2. **Integration Testing**: Run the `integration_test.py` script to test the system's overall functionality.
3. **Performance Testing**: Run the `performance_test.py` script to test the system's performance under heavy network traffic.

📸 Screenshots
---------------
[Placeholder for screenshot 1]
[Placeholder for screenshot 2]
[Placeholder for screenshot 3]


👤 Author
----------
The TranWall project was developed by Ankit Halder.
