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


def menyu():
    print("""
=== 📝 VAZIFALAR ===
1. Ro'yxat
2. Qo'shish
3. Bajarildi deb belgilash
4. O'chirish
5. Bajarilmaganlar
0. Chiqish
""")


def main():
    from xizmat import Royxat

    r = Royxat.yukla()

    while True:
        menyu()
        tanlov = tanlovni_tekshir(input("Tanlang: "), 5)

        try:
            if tanlov is None:
                print("❌ 0 dan 5 gacha son kiriting")

            elif tanlov == 1:
                if not r.vazifalar:
                    print("  (ro'yxat bo'sh)")
                else:
                    for i, v in enumerate(r.vazifalar):
                        print(f"  #{i} {v}")

            elif tanlov == 2:
                matn = input("Vazifa: ")
                muhim = ha_yoq(input("Muhimmi? (h/y): "))
                idx = r.qosh(matn, muhim)
                print(f"✅ #{idx} qo'shildi: {r.vazifalar[idx]}")

            elif tanlov == 3:
                idx = int(input("Vazifa raqami: "))
                if r.bajar(idx):
                    print(f"✔️ #{idx} bajarildi")
                else:
                    print("❌ Allaqachon bajarilgan")

            elif tanlov == 4:
                idx = int(input("Vazifa raqami: "))
                r.ochir(idx)
                print(f"🗑 #{idx} o'chirildi")

            elif tanlov == 5:
                qolgan = r.bajarilmaganlar()
                print(f"⏳ Bajarilmagan: {len(qolgan)} ta")
                for v in qolgan:
                    print(f"  {v}")

            elif tanlov == 0:
                r.saqla()
                print("💾 Saqlandi. 👋 Xayr!")
                break

        except ValueError as e:
            print(
                "❌ Son kiriting!"
                if "invalid literal" in str(e)
                else f"❌ Xato: {e}"
            )
        except IndexError:
            print("❌ Bunday vazifa yo'q")


if __name__ == "__main__":
    main()

