# SRE Challenge – Flask App on Vagrant

This project demonstrates running a simple Python Flask application using Vagrant on Fedora Linux. The setup provisions a VM, installs Python, clones the app folder, and runs it as a systemd service with port forwarding.

---

## Prerequisites (Fedora Linux)

1. **Install virtualization tools and vagrant**
  * Libvirt + dependencies: https://docs.fedoraproject.org/en-US/quick-doc/virtualization-getting-started/
  * Vagrant: https://developer.hashicorp.com/vagrant/install
  * Libvirt plugin for Vagrant: https://github.com/vagrant-libvirt/vagrant-libvirt?tab=readme-ov-file#installing

## Running the app
2. **Clone the repository**

```bash
git clone -b dev https://github.com/DdeGooijer/sre-challenge.git
cd sre-challenge
```

3. **Start the VM and provision the app**
* Start the VM by running the following command:
```bash
vagrant up
```
* Open your webbrowser and go to `http://localhost:5000`

## Optional commands
* SSH into the VM
```bash
vagrant ssh
```
* Stop the VM
```bash
vagrant stop
```
* Destroy the VM (start fresh)
```bash
vagrant destroy -f
```
* Re-run provisioning (if Vagrantfile or repo changes)
```bash
vagrant provision
```
