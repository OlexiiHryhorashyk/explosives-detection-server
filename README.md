# Explosives Detection Server

## Description
Web-server for detecting explosives on images and video with mockup of the interface and interactive documentation.

---

## Getting Started

### Prerequisites
Ensure you have the following installed on your system:
- **Python** (3.8 or newer)
- **Git**

---

### Installation and Setup

Follow these steps to get the project up and running:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/OlexiiHryhorashyk/explosives-detection-server.git
   cd explosives-detection-server

   ```

2. **Create a Virtual Environment**

- On Linux/Mac:
  ```bash
  python3 -m venv venv
  ```

- On Windows:
  ```bash
  python -m venv venv
  ```

3. **Activate the Virtual Environment**

- On Linux/Mac:
  ```bash
  source venv/bin/activate
  ```

- On Windows:
  ```bash
  & ./.venv/Scripts/Activate.ps1
  ```

4. **Install Dependencies**

Once the virtual environment is activated, install the project dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

5. **Run the Server**

To start the application, run the `server.py` script:

```bash
python server.py
```

The server should now be running. Open your browser and navigate to `http://localhost:8000`

---

## Usage

On `http://localhost:8000` you can find a web page that provides interface to detect explosives on uploaded images.  
On `http://localhost:8000/video` you can find a web page that provides interface to detect explosives from a video thread from a web camera.

---

