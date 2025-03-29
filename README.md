<h1 align="center" style="
    font-weight: bold;  
    font-size: 2.5em; 
    color:rgb(18, 18, 19);
">
  Muda-Muda 🍺
</h1>

<h1 align="center" style="
    font-weight: bold; 
    font-size: 1.5em; 
    color:rgb(6, 6, 6);
    text-transform: uppercase;
    text-decoration: underline;
    letter-spacing: 1.5px;
">
  ⭐ DDoS Detection Using Machine Learning ⭐
</h1>

## 
---

## 📜 Table of Contents  

🔹 [Introduction](#introduction)  
🔹 [Motivation](#motivation)  
🔹 [Objectives](#objectives)  
🔹 [Installation](#installation)  
🔹 [Literature Survey](#literature-survey)  
🔹 [Implemented System](#implemented-system)  
🔹 [Description of the Implemented System](#description-of-the-implemented-system)  
🔹 [Software Requirements Specification](#software-requirements-specification)  
🔹 [System Design](#system-design)  
🔹 [Implementation](#implementation)  
🔹 [Testing](#testing)  
🔹 [Results & Discussion](#results-and-discussion)  
🔹 [Conclusion](#conclusion)  
🔹 [References](#references)  
🔹 [Appendix](#appendix)  

---

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<u>
    <h2>Introduction</h2>
</u>

A <b>DDoS(Distributed denial-of-service)</b> attack is when hackers overload a server, website, or network with too much traffic, making it slow or crash. They use many infected devices, including computers and smart gadgets, to send fake requests. It’s like a traffic jam blocking a road so real cars can’t pass. If not stopped quickly, it can cause big problems and take hours to fix. The hardest part is stopping the attack without blocking real users because fake traffic looks real..

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<u>
    <h2> Motivation</h2>
</u>

For businesses running critical operations at the edge, where downtime is not an option, <b>DDoS</b> protection is vital. It helps maintain the availability of essential services and prevents disruptions.  

<b>Software-Defined Networking (SDN)</b> enables the design, deployment, and management of networks. However, data centers face a growing threat from <b>DDoS</b> attacks, which can severely impact their performance.<b>SDN</b> networks, in particular, are increasingly targeted by evolving security threats, including frequent and sophisticated <b>DDoS</b> attacks.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<u>
    <h2>Objectives:</h2>
</u>
 
- To implement a network using mininet and Ryu controller
- To generate the dataset
- To apply Machine learning algorithm to detect DDoS attack and select the best fitting model

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<u>
    <h2>Setup:</h2> 
</u>

```bash
Install VirtualBox or VMware Workstation
# Link: https://www.virtualbox.org/wiki/Downloads

Install Mininet-VM
# Link: https://github.com/mininet/mininet/releases/

Install Ubuntu in VirtualBox
# Link: https://ubuntu.com/download/desktop

Install Ryu Controller in Ubuntu VM
# Link: https://ryu.readthedocs.io/en/latest/getting_started.html

# Use git clone to install the code files
git clone https://github.com/Ansh2004P/Muda-Muda
```


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

###
 ---

<h2>Implemented System</h2>

![image](https://github.com/chiragbiradar/DDoS-Attack-Detection-and-Mitigation/assets/78417411/c6c46e97-7845-4a5e-8446-95be2821ff68)

##
 ---

### Description of the Implemented system

Our system combines the power of Software-Defined Networking (SDN) with machine learning to keep your network safe from DDoS attacks. Here's a friendly look at how it works:

- **Centralized Control:**  
  At the heart of the system is an SDN controller that keeps an eye on all network traffic, gathering information from switches and routers in real time.

- **Real-Time Monitoring:**  
  Network devices send key data—like packet rates and IP addresses—to the controller. This continuous stream of information helps us spot when something unusual is happening.

- **Smart Anomaly Detection:**  
  Using machine learning, the system learns what normal traffic looks like. When it detects a sudden spike or abnormal pattern that could signal a DDoS attack, it springs into action.

- **Easy Scalability:**  
  Thanks to the flexible design of SDN, our solution can grow with your network and adapt to new threats, ensuring ongoing protection.

In essence, our system offers a smart, proactive defense against DDoS attacks—keeping your network secure and running smoothly.


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2>Software requirements specification</h2>


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3> Overview of SRS:</h3>

Software Requirement Definition (SRS) is a comprehensive specification and description of the software requirements that must be met for the software systems to be developed successfully. Depending on the sort of demand, they may be both functional and non-functional. In order to thoroughly grasp the demands of consumers, contact between various customers and contractors is done.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4> Requirement Specification:</h4>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>Functional Requirement:</h4>

- Machine learning model should be able to detect DDoS attacks
-  Communicate with the controller to request traffic information

<h4>Non-Functional Requirement:</h4>

-  Detect DDoS attack within 20 seconds
- Analyze traffic data every 5 seconds to classify traffic as normal or abnormal.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Software and Hardware requirement specification:</h3>

- Windows/ Linux/ macOS
- Virtualization software (VMware/virtual box)
- Ryu controller
- Mininet software
<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2>System Design</h2>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Architecture of the System</h3>
Software-Defined Networking (SDN) is a network architecture approach that enables the network to be intelligently and centrally controlled, or 'programmed,' using software applications

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>SDN architecture includes three layers: </h4>


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>Application layer:</h4>

The application layer is where the network applications, such as network management, traffic engineering, and security, are implemented.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>Control layer:</h4>

The control layer represents the centralized SDN controller software that acts as the brain of the 
software-defined networking. This controller resides on a server and manages policies and traffic flows throughout the network.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Architecture of the System</h3>

#### Infrastructure layer:
The infrastructure layer is made up of the physical switches or routers in the network which forward traffic according to the instructions from the control plane.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3> Activity Diagram</h3>


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

## Dataset Features Description

The dataset is generated using Python scripts to simulate both **malicious** and **legitimate** network traffic.

### **Dataset Overview**
- **Total Features:** 23 columns  
- **Total Records:** 1,04,345 rows  

### **Feature Descriptions**
- **`dt`** – Timestamp of the captured traffic  
- **`switch`** – Switch ID handling the packet  
- **`src`** – Source IP address  
- **`dst`** – Destination IP address  
- **`pktcount`** – Total number of packets in the flow  
- **`bytecount`** – Total bytes transferred in the flow  
- **`dur`** – Flow duration in seconds  
- **`dur_nsec`** – Flow duration in nanoseconds  
- **`tot_dur`** – Total duration of the flow  
- **`flows`** – Number of flows within a specific period  
- **`packetins`** – Number of Packet-In messages received by the controller  
- **`pktperflow`** – Average packets per flow  
- **`byteperflow`** – Average bytes per flow  
- **`pktrate`** – Rate of packets per second  
- **`Pairflow`** – A measure of bidirectional traffic  
- **`Protocol`** – Type of protocol used (e.g., TCP, UDP, ICMP)  
- **`port_no`** – Port number associated with the flow  
- **`tx_bytes`** – Total bytes transmitted  
- **`rx_bytes`** – Total bytes received  
- **`tx_kbps`** – Transmission rate in Kbps  
- **`rx_kbps`** – Reception rate in Kbps  
- **`tot_kbps`** – Total bandwidth consumption in Kbps  
- **`label`** – Classifies traffic as **legitimate (0)** or **malicious (1)**  

This dataset helps in detecting DDoS attacks by analyzing network flow characteristics and distinguishing between normal and malicious traffic.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2> Implementation</h2>


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Implemented Methodology</h3>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>Explanation:</h4>

The implemented system consists of two key modules: **Detection Module** and **Mitigation Module**. The detection model is trained using a dataset generated from simulated network traffic.

### **Dataset Generation Process**
1. **SDN Topology Creation:**  
   - A network topology is created using **Mininet** in a **Software-Defined Networking (SDN)** environment.
   
2. **Traffic Simulation:**  
   - Both **normal traffic** (legitimate users) and **anomalous traffic** (DDoS attack patterns) are simulated.

3. **Feature Extraction using RYU Controller:**  
   - The RYU controller captures network flow data and extracts key features from packets, including:  
     - **Source (`src`) & Destination (`dst`) IP addresses**  
     - **Port number (`port_no`)**  
     - **Flow duration (`dur`, `tot_dur`)**  
     - **Packet statistics (`pktcount`, `pktrate`, `pktperflow`)**  
     - **Byte statistics (`bytecount`, `byteperflow`, `tx_bytes`, `rx_bytes`, `tx_kbps`, `rx_kbps`, `tot_kbps`)**  
     - **Network flow metadata (`switch`, `flows`, `packetins`, `Pairflow`, `Protocol`)**  
     - **Traffic classification (`label` → 0 = Legitimate, 1 = Malicious)**  

4. **Model Training:**  
   - The extracted dataset is used to train a **machine learning model** that can detect **DDoS attacks** in real time.

This methodology enables **real-time DDoS detection and mitigation** in an SDN environment, ensuring network security and stability.


<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Network topology:</h3>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Module Description</h3>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h4>Traffic Control Module:</h4>

The **Flow Collector** gathers traffic data by communicating with the **SDN controller**. The controller requests flow statistics from all connected switches using the **OpenFlow protocol**. Each switch responds with a **flow-stats reply**, containing flow details and counters.

### **Flow Data Extraction:**
- The **Flow Collector** processes the received data, discarding irrelevant information.
- Key extracted features include:
  - **Flow Identifier (Flow-ID):** A **seven-tuple** consisting of:
    - **Source & Destination IP addresses**
    - **Source & Destination MAC addresses**
    - **TCP/UDP Source & Destination Ports**
    - **Transport Protocol (including ICMP type for ICMP traffic)**
  - **Flow Counters:**
    - **Packet Count**
    - **Byte Count**
    - **Flow Duration**
  
This extracted data is used for real-time **DDoS detection and traffic analysis** in an SDN environment.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<u>
    <h2>Detection Module</h2>
</u>

<h3>📊 Machine Learning-Based Detection</h3>

- The detection module analyzes network traffic to identify **DDoS attacks** using **flow-based anomaly detection**.  
- Various **Machine Learning (ML) models** were trained and evaluated on the dataset to determine the most effective approach.  

<h3>🧪 Model Comparison & Results</h3>

- Multiple ML models were tested based on **accuracy** and **fitting parameters**.  
- **K-Nearest Neighbors (KNN)** emerged as the best-performing model.  
- The final model classifies network traffic as **legitimate (0) or malicious (1)** based on extracted flow features.  

## 🔄 Detection Workflow  

1. **Feature Extraction**  
   - Extract key attributes from network traffic (`src`, `dst`, `port_no`, `pktcount`, `pktrate`, `Protocol`).  

2. **Data Preprocessing & Normalization**  
   - Handle missing values (if any).  
   - Apply feature scaling to normalize numerical values.  

3. **ML Model Training & Evaluation**  
   - Train multiple models:  
     - Decision Trees 🌳  
     - Random Forest 🌲  
     - SVM 📊  
     - K-Nearest Neighbors (KNN) 🔍  

4. **Model Selection**  
   - **KNN** was selected as the **best model** based on accuracy and fitting parameters. ✅  

5. **Real-time Classification**  
   - Incoming traffic is classified as **✔️ Legitimate** or **🚨 DDoS Attack**.  


🚀 **This approach ensures accurate and efficient DDoS detection in SDN networks!** 🚀

---

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Description of Tools & Technology Used</h3>

- **Mininet:**  
  A tool for software-defined networks that lets you create and test virtual network environments on a single machine.

- **RYU Controller:**  
  An open-source SDN controller that simplifies network management by making it easier to adapt how traffic is handled.

- **VirtualBox:**  
  A virtualization software that enables you to run multiple operating systems on a single computer, perfect for testing and development.

- **Linux:**  
  A robust and secure operating system widely used in both server and desktop environments.

- **Python:**  
  A versatile programming language known for its simplicity and efficiency in developing a wide range of applications.

<h2>Testing</h2>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h3>Test Plan and Test Cases</h3>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2>Results & Discussion</h2>

After designing the attack detection and mitigation method, the results were tested and evaluated. The evaluation process involved analyzing the performance of different machine learning (ML) algorithms and comparing their accuracy in detecting attacks. The table below presents the accuracy of various models:

From the results, it is evident that the **Random Forest (RF) model provides the highest accuracy**  but if is clearly **overfitting** and **KNN gives both accuracy and is not overfitting** in distinguishing between normal and malicious traffic.

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2>Conclusion</h2>

In this work, a **KNN machine learning algorithm** was used to develop a model capable of **automatically detecting DDoS attacks** in **Software-Defined Networking (SDN)** environments. The model continuously collects network flow data, extracts native flow features, and expands them with additional attributes. 

A detection module then applies five key criteria to classify network traffic as **normal or anomalous**. When an attack is detected, the system immediately **blocks the source** to prevent further malicious activity. 

To ensure optimal performance, three ML algorithms— **Random Forest (RF)**, **Support Vector Machine (SVM)**, and **K-Nearest Neighbors (KNN)**, **Logistic Regression(LR)** —were evaluated. The results confirmed that **KNN outperformed the other classifiers**, delivering the best results for attack detection. 

The implemented methodology successfully **identified attacks efficiently** without disrupting legitimate network traffic.

---
<!-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -->

<h2> References</h2>

Here are some related papers

[[1] Dong Li,Chang Yu, Qizhao Zhou and Junqing Yu .”Using SVM to Detect DDoS Attacks in SDN Network.” 2018 IOP Conf. Ser.: Mater. Sci. Eng. 466 012003,2018 .](https://iopscience.iop.org/article/10.1088/1757-899X/466/1/012003/meta)

[[2] Yijie Li, Boyi Liu, Shang Zhai and Mingrui Chen ,”DDoS attack detection method based on feature extraction of deep belief networks.”,IOP Conference Series: Earth and Environmental Science, Volume 252, Issue 3,2019.](https://iopscience.iop.org/article/10.1088/1755-1315/252/3/032013/met)

[[3] Peng Xiao,Wenyu Qu,Heng Qi ,Zhiyang Li.”Detecting DDoS attacks against data centers with correlation analysis.”,Computer Communications 67,2015.](https://www.sciencedirect.com/science/article/abs/pii/S0140366415002285)

[[4] Fatima Khashab, Joanna Moubarak, Antoine Feghali , and Carole Bassil.”DDoS Attack Detection and Mitigation in SDN using Machine Learning”,IEEE 7th International Conference on Network Softwarization (NetSoft),2021.](https://ieeexplore.ieee.org/abstract/document/9492558/)

[[5] Bawany NZ, Shamsi JA, Salah K. DDoS attack detection and mitigation  using
 SDN:     methods, practices, and solutions. Arabian Journal for Science and 
 Engineering. 2017 Feb;42(2):425-41.](https://link.springer.com/article/10.1007/s13369-017-2414-5)


[[6] Dharma, N.G., Muthohar, M.F., Prayuda, J.A., Priagung, K. and Choi, D., 2015,
August. Time-based DDoS detection and mitigation for SDN controller. In 
2015 17th Asia-Pacific Network Operations and Management Symposium (APNOMS) (pp. 550-553). IEEE.](https://ieeexplore.ieee.org/abstract/document/7275389/)
            
[[7]  da Silveira Ilha, A., Lapolli, A.C., Marques, J.A. and Gaspary, L.P., 2020. Euclid: A fully in-network, P4-based approach for real-time DDoS attack detection and mitigation. IEEE Transactions on Network and Service Management, 18(3), pp.3121-3139.](https://ieeexplore.ieee.org/abstract/document/9311137/)

    
[[8] Singh, J. and Behal, S., 2020. Detection and mitigation of DDoS attacks in SDN: A comprehensive review, research challenges and future directions. Computer Science Review, 37, p.100279.](https://www.sciencedirect.com/science/article/abs/pii/S1574013720301647)

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

---
<h2> Appendix</h2>

<!-- --------------------------------------------------------------------------------------------------------------------------------------------------------- -->

## 👥 <u>Contributors</u>

- [Ansh Patel](https://github.com/Ansh2004P/) 🚀  
- [Tanishq Singh](http://github.com/stanishq2710) 💡  
- [Vagish Bharadwaj](https://github.com/unfilteredd) 🔥  
- [Aditya Kumar](https://github.com/Adityakumar1805) 🎯  



<p align="right">
  <a href="#top" style="
    display: inline-block;
    padding: 8px 12px;
    background-color: #007bff;
    color: white;
    text-decoration: none;
    font-weight: bold;
    border-radius: 20px;
  ">
    ⬆️ Top
  </a>
</p>
