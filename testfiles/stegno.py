from stegano import lsb
secret = lsb.hide("t2.png", "WzU1MDkgMzE4MSwJCjcwMjggODA5NywKNjQwNCAyODU2LAkKMTMyMyA4NjY0XQ==")
secret.save("t4.png")

clear_message = lsb.reveal("t4.png")
print(clear_message)

