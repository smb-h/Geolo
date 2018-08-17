
def get_ip(request):

    fl = open('TEST', 'a')


    loc = request.META.get('ar-real-country')
    if not loc:
        loc = request.META.get('ar_real_country')

    if not loc:
        x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded != None:
            ip = x_forwarded.split(',')[0]
        else :
            ip = request.META.get('REMOTE_ADDR')
        # return ip
        if ip :
	        string = '\n' + str(ip)
	        fl.write(string)
        fl.close
        return

    # return loc
    if loc:
	    string = '\n' + str(loc)
	    fl.write(string)
    fl.close()
    return


