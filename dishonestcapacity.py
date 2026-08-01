# arvutus et leida kui palju tegelikult sa mahtu saad kui ostad endale mälupulga vs kui palju reklaamitakse:
#esiteks küsin mis mahuühiku kasutaja ostis ja arvutan selle mahutavuse kao kordaja
#teiseks küsin palju mahtu osteti?

print("Kas ostsite TB ühikut mahtu või GB ühikut mahtu")
ühik = input(">")

if ühik == "GB":
    Mahutavuse_kadu = 1000000000/1073741824
elif ühik == "gb":
    Mahutavuse_kadu = 1000000000/1073741824
elif ühik == "TB":
    Mahutavuse_kadu = 1000000000000/1099511627776
elif ühik == "tb":
    Mahutavuse_kadu = 1000000000000/1099511627776

print("Kui palju mahtu te ostsite?")
ostetud_maht = input(">")
ostetud_maht = float(ostetud_maht)

päris_maht = str(round(ostetud_maht * Mahutavuse_kadu, 2))

print("Sulle reklaamiti " + str(ostetud_maht) + ühik + " mahtu, tegelikult said " + päris_maht + ühik)