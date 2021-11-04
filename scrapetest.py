import base64

with open("exampleimage.jpg", "rb") as exampleimage:
    examplebytes = base64.b64encode(exampleimage.read())


with open("compareimage.png", "rb") as compareimage:
    comparebytes = base64.b64encode(compareimage.read())


if comparebytes == examplebytes:
    print("Det fungerade!")

else:
    print("Det fungerade inte.")