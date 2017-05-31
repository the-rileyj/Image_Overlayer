from PIL import Image
import sys
## Check for primitive image string arguments ##
if len(sys.argv) > 1:
    try:
        ## Check for overlay image string ##
        try:
            if len(sys.argv) > 2:
                logo = sys.argv[2]
            else:
                print("Sorry buddy, overlay photo string needed")
        except:
            print("Sorry, error in getting overlay photo string")
        ## Check for margin argument ##
        try:
            if len(sys.argv) > 3:
                margin = int(sys.argv[3])
            else:
                raise
        except:
            margin = 5
            hswap = False
            vswap = False
        ## Check for x-flip argument ##
        try:
            if len(sys.argv) > 4:
                los = sys.argv[4].lower()
                hswap = los[0] == "y" or "yes" in los
            else:
                raise
        except:
            hswap = False
            vswap = False
        ## Check for y-flip argument ##
        try:
            if len(sys.argv) > 5:
                los = sys.argv[5].lower()
                vswap = los[0] == "y" or "yes" in los
            else:
                raise
        except:
            vswap = False
        ## Check for renaming argument ##
        try:
            if len(sys.argv) > 6:
                rename = sys.argv[6]
            else:
                raise
        except:
            rename = 'new' + sys.argv[1]
        img = Image.open(sys.argv[1], 'r')
        overlay = Image.open(logo, 'r')
        origsix, origsiy = img.size
        overlaysix, overlaysiy = overlay.size
        img.paste(overlay, ((origsix - overlaysix - margin) if not hswap else (margin), (origsiy - overlaysiy - margin) if not vswap else (margin)))
        img.save(rename)
        ## Check for y/n string argument for whether or not to show image in default image viewer ##
        if len(sys.argv) > 7:
            img.show()
    except Exception as e:
        print("Error in Arguments\n{0}".format(e))
else:
    print("No Arguments Given")
