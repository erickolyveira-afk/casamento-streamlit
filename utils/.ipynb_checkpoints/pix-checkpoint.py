import qrcode
from io import BytesIO

# ---------------- CRC16 ----------------
def crc16_ccitt(data: str):
    crc = 0xFFFF
    for byte in data.encode("utf-8"):
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return format(crc, "04X")

# ---------------- PIX PAYLOAD ----------------
def gerar_pix_payload(chave, nome, cidade, valor):
    gui = "BR.GOV.BCB.PIX"

    mai = (
        "00" + f"{len(gui):02}" + gui +
        "01" + f"{len(chave):02}" + chave
    )

    valor_str = f"{float(valor):.2f}"

    campo54 = "54" + f"{len(valor_str):02}" + valor_str

    payload_sem_crc = (
        "000201"
        "010212"
        "26" + f"{len(mai):02}" + mai +
        "52040000"
        "5303986"
        + campo54 +
        "5802BR"
        "59" + f"{len(nome):02}" + nome +
        "60" + f"{len(cidade):02}" + cidade +
        "62070503***"
        "6304"
    )

    checksum = crc16_ccitt(payload_sem_crc)
    return payload_sem_crc + checksum

# ---------------- QR CODE ----------------
def gerar_qr(payload):
    qr = qrcode.make(payload)
    buf = BytesIO()
    qr.save(buf, format="PNG")
    return buf.getvalue()