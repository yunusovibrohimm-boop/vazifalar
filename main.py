def tanlovni_tekshir(matn, max_raqam):
    matn = matn.strip()

    if not matn.isdigit():
        return None

    n = int(matn)

    if 0 <= n <= max_raqam:
        return n

    return None


def ha_yoq(matn):
    return matn.strip().lower() in ("h", "ha")
