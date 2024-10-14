#!/bin/bash

# YouTube channel mention
echo -e "\n${PURPLE}Welcome to the Malicious Direction! 🐉${NC}"
echo -e "${CYAN}Check out my YouTube channel: Malicious Direction!${NC}\n"

# List of required modules
REQUIRED_MODULES=("pygame" "requests" "psutil")

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Function to check if a module is installed
check_module() {
    python3 -c "import $1" &> /dev/null
    return $?
}

# Function to check if Python is installed
check_python() {
    python3 --version &> /dev/null
    return $?
}

# Function to install Python based on the OS
install_python() {
    OS=$(uname -s)
    echo -e "${YELLOW}Python is not installed. Installing Python...${NC}"

    case $OS in
        Linux)
            # Check for specific Linux distributions
            if [ -f /etc/debian_version ]; then
                sudo apt update
                sudo apt install -y python3 python3-pip
            elif [ -f /etc/redhat-release ]; then
                sudo yum install -y python3 python3-pip
            else
                echo -e "${RED}Unsupported Linux distribution! Please install Python manually.${NC}"
                exit 1
            fi
            ;;
        Darwin)
            # For macOS
            brew install python
            ;;
        Android)
            # For Termux
            pkg install python python-pip
            ;;
        *)
            echo -e "${RED}Unsupported OS! Please install Python manually.${NC}"
            exit 1
            ;;
    esac

    echo -e "${BLUE}Python has been installed.${NC}"
}

# Check for Python installation
if ! check_python; then
    install_python
fi

# Loop through the required modules and check if each one is installed
for module in "${REQUIRED_MODULES[@]}"; do
    if check_module "$module"; then
        echo -e "${GREEN}$module is already installed.${NC}"
    else
        echo -e "${YELLOW}$module is not installed. Installing...${NC}"
        pip install "$module" || { echo -e "${RED}Failed to install $module.${NC}"; }
        if check_module "$module"; then
            echo -e "${BLUE}$module has been installed.${NC}"
        else
            echo -e "${RED}Failed to install $module.${NC}"
        fi
    fi
done

# Display a completion message with animation effect
echo -e "${PURPLE}Checking installation status...${NC}"

for i in {1..5}; do
    echo -n "."
    sleep 0.5
done

echo -e "\n${CYAN}All required modules have been checked!${NC}"

# Execute the Python script
python3 mobile.py
