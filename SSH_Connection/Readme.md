# 📌 Project: Secure SSH Communication in WSL Ubuntu

This project demonstrates setting up an **OpenSSH server and client** within **WSL Ubuntu** to enable secure remote access and communication between multiple containers or virtual environments.

## 📜 Overview

- **Server:** Runs OpenSSH server (`openssh-server`) to allow secure remote connections.
- **Client:** Runs OpenSSH client (`openssh-client`) to connect to the server.
- **Authentication:** Uses SSH keys for secure access.
- **Benefits:** Improved security, better collaboration, scalability, portability, and ease of management.

---

## 🚀 Installation & Setup Guide

### **Step 1: Update and Install OpenSSH in WSL Ubuntu**
Before setting up SSH, ensure your system is up-to-date.

```bash
sudo apt-get update 
```

Then, install OpenSSH server and client:

```bash
sudo apt-get install openssh-server openssh-client -y
```

### **Step 2: Start and Enable the SSH Service**
Once installed, start the OpenSSH server:

```bash
sudo service ssh start
```

Enable it to start automatically on boot:

```bash
sudo systemctl enable ssh
```

Check the status of the SSH service:

```bash
sudo service --status -all
```

If the service is running, you should see output like:

```
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running)
```

### **Step 3: Configure SSH for Secure Access**
Modify the SSH configuration file to allow remote connections:

```bash
sudo nano /etc/ssh/sshd_config
```

Find the following lines and update them:

```ini
 PermitRootLogin yes
```

Save the file (`Ctrl + s`, then `Ctrl + X`).

Set a new password for the root user:

``` bash
passwd root
```
Start the SSH service:


```bash
service ssh start
```

 

### **SStep 4: Connect to the SSH Server from Container2**
Start the second container (container2):

```bash
docker start container2
```
Execute a bash shell in container2:

```bash
docker exec -it container2 bash
```

Update the package list and install OpenSSH client:

```bash
apt-get update
apt-get install openssh-client
```

Attempt to SSH into container1 from container2 using its IP address:

```bash
ssh root@<container1-ip-address> 
```

---

## 🔧 Troubleshooting

1. **Check if SSH is running in the server container**
   ```bash
docker exec -it container1 service ssh status
   ```
2. **Restart the SSH service**
   ```bash
   docker exec -it container1 service ssh restart
   ```
3. **Check firewall rules (if applicable)**
   ```bash
   sudo ufw allow ssh
   sudo ufw enable
   ```

---

## 📌 Features & Benefits

✅ Improved security  
✅ Ease of management  
✅ Better collaboration  
✅ Scalability  
✅ Portability  

---

## 📂 Project Structure

```
/project1
│── setup_ssh.sh       # Script for automatic installation & setup
│── README.md          # Detailed documentationx