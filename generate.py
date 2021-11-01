from PIL import Image

number_of_bg=x
number_of_hat=x
number_of_eyes=x
number_of_mouth=x
number_of_body=x
number_of_feet=x

for a in range(1,number_of_bg+1):
    for b in range(1,number_of_hat+1):
        for c in range(1,number_of_eyes+1):
            for d in range(1,number_of_mouth+1):
                for e in range(1,number_of_body+1):
                    for f in range(1,mumber_of_feet+1):
                        bg = Image.open("backgrounds/bg{}.png".format(a))).convert("RGBA")
                        hat = Image.open("hats/hat{}.png".format(b))).convert("RGBA")
                        eyes = Image.open("eyes/eyes{}.png".format(c))).convert("RGBA")
                        mouth = Image.open("mouthes/mouth{}.png".format(d))).convert("RGBA")
                        body = Image.open("bodies/body{}.png".format(e))).convert("RGBA")
                        feet = Image.open("feet/feet{}.png".format(f))).convert("RGBA")

                        bg.paste(hat,(0,0),hat)
                        bg.paste(eyes,(0,0),eyes)
                        bg.paste(mouth,(0,0),mouth)
                        bg.paste(body,(0,0),body)
                        bg.paste(feet,(0,0),feet)

                        bg.save("output/xxx_{}_{}_{}_{}_{}_{}.png".format(a,b,c,d,e,f))
