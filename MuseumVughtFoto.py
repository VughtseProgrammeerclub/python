# Maak een foto via de WEBCAM
# DETECTS FACES
# Foto's samenvoegen
# QR code maken

from PIL import Image, ImageFilter
import face_recognition, os, cv2, pygame, time
from matplotlib import pyplot as plt

datasets = 'c:\\FaceHerken' 
sub_data = 'Monique'    
path = os.path.join(datasets, sub_data)
#print(path)

def Maak_foto():
    webcam = cv2.VideoCapture(1)
    while True:
        try:
            check, frame = webcam.read()
            #print(check) #prints true as long as the webcam is running
            #print(frame) #prints matrix values of each framecd 
            cv2.imshow("Vughts Museum Foto", frame)
            cv2.moveWindow("Vughts Museum Foto", 1000, 200)
            key = cv2.waitKey(1)
            if key == ord(' '): 
                cv2.imwrite(filename='Museum_img.jpg', img=frame)
                #webcam.release()
                #print("Processing image...")
                #img_ = cv2.imread('Museum_img.jpg', cv2.IMREAD_ANYCOLOR)
                #print("Image saved!")
                webcam.release()
                cv2.destroyAllWindows()
                break
        
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
    
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break


def DetectFace():
    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("Museum_img.jpg")
    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    #if face_locations = 0:
    #    break
    print(face_locations)
    
    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        groot = int((bottom - top) /8)
        print("groot=:",groot)
        top = int(top - groot)
        right = int(right + groot)
        left = int(left - groot)
        bottom = int(bottom + groot)
        print("A newface is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        #pil_image.show()
        #pil_image.save("Museum_Gezicht.jpg")
        pil_image.save("Mus_Gezicht.png")
        img = Image.open("Mus_Gezicht.png")
        img = img.resize((100,100))
        img.save("Museum_Gezicht100.png")
        img = Image.open("Mus_Gezicht.png")
        img = img.resize((80,80))
        img.save("Museum_Gezicht80.png")
        # Size of the image in pixels (size of original image)
        #print ("Museum_gezicht size: ", img.size)
        print("kleine foto opgeslagen")


def FotoSamenvoegen():
    # Blur cirkelvorm    
    mask_im_blur100 = Image.open("mask_circle100.jpg")
    #mask_im_blur100 = mask_im.filter(ImageFilter.GaussianBlur(1))
    mask_im_blur80 = Image.open("mask_circle80.jpg")
    #mask_im_blur80 = mask_im.filter(ImageFilter.GaussianBlur(1))
      
    # Pak burgemeester samenvoegen
    im1 = Image.open("Burgemeester.jpg")
    im1P = Image.open("Burgemeester+.jpg")
    im2 = Image.open('Museum_Gezicht100.png')
    Image.Image.paste(im1, im2, (154, 179), mask_im_blur100)
    im1.save('c:/FaceHerken/Samen1.jpg', quality=99)
    Image.Image.paste(im1P, im2, (154, 179), mask_im_blur100)
    im1P.save('c:/FaceHerken/Samen1+.jpg', quality=99)
    # Pak dame samenvoegen
    im3 = Image.open("Dame.jpg")
    im3P = Image.open("Dame+.jpg")
    im4 = Image.open('Museum_Gezicht100.png')
    Image.Image.paste(im3, im4, (158, 65), mask_im_blur100)
    im3.save('c:/FaceHerken/Samen2.jpg', quality=99)
    Image.Image.paste(im3P, im4, (158, 65), mask_im_blur100)
    im3P.save('c:/FaceHerken/Samen2+.jpg', quality=99)
    # Pak politie samenvoegen
    im5 = Image.open("Politie.jpg")
    im5P = Image.open("Politie+.jpg")
    im6 = Image.open('Museum_Gezicht80.png')
    Image.Image.paste(im5, im6, (157, 160), mask_im_blur80)
    im5.save('c:/FaceHerken/Samen3.jpg', quality=99)
    Image.Image.paste(im5P, im6, (157, 160), mask_im_blur80)
    im5P.save('c:/FaceHerken/Samen3+.jpg', quality=99)
    # Pak brandweer samenvoegen
    im7 = Image.open("Brandweer.jpg")
    im7P = Image.open("Brandweer+.jpg")
    im8 = Image.open('Museum_Gezicht80.png')
    Image.Image.paste(im7, im8, (156, 117), mask_im_blur80)
    im7.save('c:/FaceHerken/Samen4.jpg', quality=99)
    Image.Image.paste(im7P, im8, (156, 117), mask_im_blur80)
    im7P.save('c:/FaceHerken/Samen4+.jpg', quality=99)
    

def Toon_drie_fotos():
    # importing required library
    import pygame

    #Inner function
    def teken_drie_plaatjes(plaatje1, plaatje2, plaatje3):
        #plaatje2 = pygame.transform.scale(plaatje2, (665,850))
        plaatje2 = pygame.transform.scale(plaatje2, (508,763))
        #plaatje3 = pygame.transform.scale(plaatje3, (400,400))
        # Using blit to copy content from one surface to other
        scrn.blit(plaatje1.convert(), (100, 150))
        scrn.blit(plaatje2.convert(), (706, 100))
        scrn.blit(plaatje3.convert(), (1429,150))
        # paint screen one time
        pygame.display.flip()
        
    # activate the pygame library .
    #pygame.init()

    # create the display surface object
    # of specific dimension..e(X, Y).
    size = pygame.display.list_modes()[0]
    scrn = pygame.display.set_mode(size, pygame.FULLSCREEN)
    print(size)
    # set the pygame window name
    #pygame.display.set_caption('Maak je keuze door op Spatiebalk te Klikken')
   
    # create a surface object, image is drawn on it.
    imp = pygame.image.load("Samen1+.jpg")
    imp2 = pygame.image.load("Samen2+.jpg")
    imp3 = pygame.image.load("Samen3+.jpg")
    imp4 = pygame.image.load("Samen4+.jpg")
    plaatjes = [imp, imp2, imp3, imp4]

    #Schrijf tekst
    #font = pygame.font.Font('freesansbold.ttf', 32)
    #green=(0, 255, 255)
    #white=(255,255,255)
    #text = font.render('DRUK OP SPATIEBALK ALS DIT JE KEUZE IS', True, green)
    #textRect = text.get_rect()
    #textRect.center = (500, 10)
    #scrn.blit(text, textRect)

    plt1 = pygame.image.load("KeuzeschermDef.png").convert()
    scrn.blit(plt1, (0, 0))
    pygame.display.update
    plt2 = pygame.image.load("c:/FaceHerken/KnoppenTekst.png").convert()
    scrn.blit(plt2, (150,800 ))
    pygame.display.update


    middelstePlaatje = 1
    teken_drie_plaatjes(plaatjes[0], plaatjes[1], plaatjes[2])

    status = True
    duur = 0
    tijd1 = time.perf_counter()
    while (status):
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
        tijd2 = time.perf_counter()
        duur = tijd2 - tijd1
        if int(duur) > 30:
            status = False
        for i in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    middelstePlaatje = (middelstePlaatje + 1) if (middelstePlaatje != len(plaatjes) - 1) else 0
                    rechts = (middelstePlaatje + 1) if (middelstePlaatje != len(plaatjes) - 1) else 0
                    links = (middelstePlaatje - 1) if (middelstePlaatje != 0) else (len(plaatjes) - 1)
                    teken_drie_plaatjes(plaatjes[links], plaatjes[middelstePlaatje], plaatjes[rechts])
                if i.key == pygame.K_RIGHT:
                    middelstePlaatje = (middelstePlaatje - 1) if (middelstePlaatje != 0) else (len(plaatjes) - 1)
                    links = (middelstePlaatje - 1) if (middelstePlaatje != 0) else (len(plaatjes) - 1)
                    rechts = (middelstePlaatje + 1) if (middelstePlaatje != len(plaatjes) - 1) else 0
                    teken_drie_plaatjes(plaatjes[links], plaatjes[middelstePlaatje], plaatjes[rechts])
                    #scrn.blit(text, textRect)
                if i.key == pygame.K_SPACE:
                    print("mijn keuze is: ", middelstePlaatje)
                    status = False
                if i.key == pygame.K_q:
                    status = False
    # deactivates the pygame library
    #pygame.quit()
    return middelstePlaatje


def Maak_kaart(Keuze):
    if (Keuze == 0):
        im1 = Image.open("Samen1.jpg")
        im2 = Image.open('Kaartversie1.jpg')
        # im2 = Image.open('Kaart1.jpg')
    elif (Keuze == 1):
        im1 = Image.open("Samen2.jpg")
        im2 = Image.open('Kaartversie2.jpg')
    elif (Keuze == 2):
        im1 = Image.open("Samen3.jpg")
        im2 = Image.open('Kaartversie3.jpg')
    elif (Keuze == 3):
        im1 = Image.open("Samen4.jpg")
        im2 = Image.open('Kaartversie4.jpg')
    else: 
        im1 = Image.open("Samen5.jpg")
        im2 = Image.open('Kaart5.jpg')
    Image.Image.paste(im2, im1, (604, 9))
    im2.save('c:/FaceHerken/SamenEind.jpg', quality=95)
    scrn = pygame.display.set_mode((X, Y))
     # set the pygame window name
    pygame.display.set_caption('image')
     # create a surface object, image is drawn on it.
    plt3 = pygame.image.load("AchtergrondDef.png").convert()
    scrn.blit(plt3, (0, 0))
    
    imp = pygame.image.load('c:/FaceHerken/SamenEind.jpg').convert()
     # Using blit to copy content from one surface to other
    scrn.blit(imp, (10, 250))
    
    pygame.display.update
     # paint screen one time
    Maak_QR("SamenEind.jpg",pygame,scrn)
    pygame.display.flip()
    print ("hier wachten")
    
    wacht = True
    duur = 0
    tijd1 = time.perf_counter()
    while (wacht):
    # Toon kaart tot knop wordt ingedrukt
        tijd2 = time.perf_counter()
        duur = tijd2 - tijd1
        #print (tijd1, tijd2, int(duur))
        if int(duur) > 30:
            wacht = False
        for i in pygame.event.get():
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        #print ("in loop pygame_event_get")
            if i.type == pygame.QUIT:
                done = False
                wacht = False
                pygame.quit()
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT or i.key == pygame.K_SPACE:
                    done = True
                    wacht = False
                    print ("rood of pijl ingedrukt")
                if i.key == pygame.K_ESCAPE:
                    done = False
                    wacht = False
       
    

def Maak_QR(A,pygame,scrn):
    #use: app.py <arg>
    #<arg> = naam van het bestand
    #pip install imagekitio  <-- niet vergeten
    #pip install qrcode  <-- niet vergeten

    import base64
    import os
    import sys
    import qrcode
    import qrcode.image.svg
    from imagekitio import ImageKit
    from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

    imagekit = ImageKit(
        private_key='private_twLxHvZgRYgDRiY8iu40RvYK56Y=',
        public_key='public_R6MmeaGuAreIruNRFYvOJopaZ0s=',
        url_endpoint='https://ik.imagekit.io/073Museum'
    )

    #argument filename foto
    print (A, sys.argv)
    n= len(sys.argv)
    if (n> 1):
        filename = sys.argv[1]
    else:
        filename = 'dc.jpg'

    #Bestandsnaam hardcoded in de source ipv argument achter app.py
    filename = "SamenEind.jpg"

    with open(filename, 'rb') as f:
        image_data = f.read()
        encoded_image = base64.b64encode(image_data)
        encoded_image

    options = UploadFileRequestOptions(
        use_unique_file_name=False,
        #tags=['abc', 'def'],
        folder='/testing/',
        is_private_file=False,
        custom_coordinates='10,10,20,20',
        overwrite_file=True,
        overwrite_ai_tags=False,
        overwrite_tags=False,
        )
    upload = imagekit.upload(
            encoded_image,
	        file_name="Vughts_Museum.jpg",
	        options=UploadFileRequestOptions(
	    	tags = ["Het Vughts Museum", "Vught"]
	        ) 
    )
    #print(upload.response_metadata.raw)
    finalURL= upload.url
    print(finalURL)
    img = qrcode.make(finalURL)
    type(img)  
    img.save(upload.name+".png")
    #pygame.display.set_caption('image')
     # create a surface object, image is drawn on it.
    #scrn = pygame.display.set_mode((X, Y))
    imp = pygame.image.load(upload.name+".png").convert()
     # Using blit to copy content from one surface to other
    scrn.blit(imp, (1200, 350))
     # paint screen one time
    pygame.display.update()
    #img.show()

   
if __name__ == '__main__':
    # importing required library
    import pygame
       # activate the pygame library .
    pygame.init()
    X = 1920
    Y = 1080
     # create the display surface object
    # of specific dimension..e(X, Y).
    done = True
    while done:
        scrn = pygame.display.set_mode((X, Y))
         # set the pygame window name
        pygame.display.set_caption('image')
         # create a surface object, image is drawn on it.
        imp = pygame.image.load("StartschermDef.png").convert()
         # Using blit to copy content from one surface to other
        scrn.blit(imp, (0, 0))
         # paint screen one time
        pygame.display.flip()
        print("begin maak foto")
        Maak_foto()
        print("begin DetectFace")
        DetectFace()
        print("Begin FotoSamenvoegen")
        FotoSamenvoegen()
        Choise = Toon_drie_fotos()
        print ("Keuze terug = ", Choise)
        Maak_kaart(Choise)
        print ("einde Maak_kaart")
        
    
    webcam.release()
    cv2.destroyAllWindows()
    pygame.quit
        
       
                