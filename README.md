
# QR Code Attendance System 📷✅

A simple Python-based QR Code attendance system that scans QR codes using your webcam and marks attendance in a text file. Each person can only be marked once per day.

## 📦 Features

- Scan QR codes using your webcam
- Mark attendance with timestamp
- Prevents duplicate entries for the same day
- Simple `.txt` file-based storage
- Real-time QR code visualization

---

## 🔧 Requirements

Make sure you have the following Python libraries installed:

```bash
pip install opencv-python pyzbar
````

**Additional Setup for Windows Users:**

* You may need to install the `zbar` shared library. Download it from [ZBar Windows Downloads](https://github.com/NaturalHistoryMuseum/pyzbar#windows).

---

## 🚀 How to Run

1. Clone this repository:

```bash
git clone https://github.com/Alanbiju255/QR-Code-Attendance-System.git
cd QR-Code-Attendance-System
```

2. Run the script:

```bash
python aip.py
```

3. Hold up your QR code in front of the camera.
4. Your attendance will be marked and saved to `attendance.txt`.
5. Press **`q`** to quit.

---

## 📝 Attendance Format

Each entry in `attendance.txt` is stored as:

```
Name - YYYY-MM-DD HH:MM:SS
```

---

## 📌 Example

If the QR code contains:

```
John Doe
```

An example line in `attendance.txt` would be:

```
John Doe - 2025-05-26 10:24:17
```

---

## 💡 Future Improvements

* Export attendance as CSV or Excel
* Admin dashboard for viewing data
* Integration with Google Sheets
* Face recognition-based attendance

---

## 🤝 Contributions

Pull requests are welcome! Feel free to open issues for feature requests or bugs.

---

## 👨‍💻 Author

**Alan Biju**
[GitHub](https://github.com/Alanbiju255) • [LinkedIn](www.linkedin.com/in/alan-biju-34b0aa296)

``` 
