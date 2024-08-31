import qrcode
import json
from datetime import datetime

def generate_user_qrcode(name, email, roll_number, sport):
    data = {
        "name": name,
        "email": email,
        "roll_number": roll_number,
        "sport": sport
    }
    json_data = json.dumps(data)
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=10,  
        border=4, 
    )
    qr.add_data(json_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"{roll_number}_qrcode.png"
    img.save(filename)
    img.show()

    return f"QR Code generated and saved as {filename}"

def validate_qrcode(qr_data):
    data = json.loads(qr_data)
    current_time = datetime.now().strftime("%H:%M")
    valid_from = "16:00" 
    valid_to = "22:30"    
    if valid_from <= current_time <= valid_to:
        return "QR Code is valid."
    else:
        return "QR Code is not valid outside of the time window."
generate_user_qrcode(name="John Doe", email="johndoe@example.com", roll_number="12345", sport="Basketball")
qr_data = json.dumps({
    "name": "Nandhini",
    "email": "nandhinimanikandan001@gmail.com",
    "roll_number": "12345",
    "sport": "Basketball"
})
validation_result = validate_qrcode(qr_data)
print(validation_result)
