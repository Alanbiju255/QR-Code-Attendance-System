import cv2
from pyzbar import pyzbar
from datetime import datetime

attendance_file = "attendance.txt"

def load_attendance():
    """Load attendance records from the text file."""
    records = []
    try:
        with open(attendance_file, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(line)
    except FileNotFoundError:
        pass
    return records

def is_already_marked(records, name):
    """Check if the name is already marked today."""
    today = datetime.now().date()
    for record in records:
        # Each record format: Name - YYYY-MM-DD HH:MM:SS
        try:
            rec_name, rec_time = record.split(" - ")
            rec_date = datetime.strptime(rec_time, "%Y-%m-%d %H:%M:%S").date()
            if rec_name == name and rec_date == today:
                return True
        except:
            continue
    return False

def mark_attendance(name):
    records = load_attendance()
    if is_already_marked(records, name):
        print(f"Attendance already marked today for {name}")
        return
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{name} - {now}"
    with open(attendance_file, "a") as f:
        f.write(entry + "\n")
    print(f"Attendance marked for {name} at {now}")

def scan_qr():
    cap = cv2.VideoCapture(0)
    print("Scanning QR code. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        qr_codes = pyzbar.decode(frame)
        for qr in qr_codes:
            qr_data = qr.data.decode("utf-8").strip()
            # Use the name from QR code directly
            mark_attendance(qr_data)

            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.9, (0, 255, 0), 2)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr()
