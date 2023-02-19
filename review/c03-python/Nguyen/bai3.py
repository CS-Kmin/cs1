GIO_NGU = [9, 50, 10]
GIO_THUC = [5, 20, 10]
if GIO_NGU[2] - GIO_THUC[2] < 0: #giay nho
    if GIO_NGU[1] - GIO_THUC[1] < 0: #phut nho
        if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
            b = - GIO_NGU[1] + GIO_THUC[1]
            a = - GIO_NGU[0] + GIO_THUC[0]
        else:
            if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                b = - GIO_NGU[1] + GIO_THUC[1]
                a = 0
            else: #gio lơn
                b = - GIO_NGU[1] + GIO_THUC[1]
                a = 24 - GIO_NGU[0] + GIO_THUC[0]
    else:
        if GIO_NGU[1] - GIO_THUC[1] == 0: #phut bang
            if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                b = 0
                a = - GIO_NGU[0] + GIO_THUC[0]
            else:
                if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                    b = 0
                    a = 0
                else: #gio lơn
                    b = 0
                    a = 24 - GIO_NGU[0] + GIO_THUC[0] 
        else: # phut lơn
            if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                b = 60 - GIO_NGU[1] + GIO_THUC[1]
                a = - GIO_NGU[0] + GIO_THUC[0] - 1
            else:
                if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                    b = 60 - GIO_NGU[1] + GIO_THUC[1]
                    a = 23
                else: #gio lơn
                    b = 60 - GIO_NGU[1] + GIO_THUC[1]
                    a = 24 - GIO_NGU[0] + GIO_THUC[0] - 1
else:
    if GIO_NGU[2] - GIO_THUC[2] > 0: #giay lon
        if GIO_NGU[1] - GIO_THUC[1] < 0: #phut nho
            if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                b = - GIO_NGU[1] + GIO_THUC[1] - 1
                a = - GIO_NGU[0] + GIO_THUC[0]
            else:
                if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                    b = - GIO_NGU[1] + GIO_THUC[1] - 1
                    a = 0
                else: #gio lơn
                    b = - GIO_NGU[1] + GIO_THUC[1] - 1
                    a = 24 - GIO_NGU[0] + GIO_THUC[0] - 1
        else:
            if GIO_NGU[1] - GIO_THUC[1] == 0: #phut bang
                if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                    b = 59
                    a = - GIO_NGU[0] + GIO_THUC[0] - 1
                else:
                    if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                        b = 59
                        a = 23
                    else: #gio lơn
                        b = 59
                        a = 24 - GIO_NGU[0] + GIO_THUC[0] - 1
            else: #phut lơn
                if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                    b = 60 - GIO_NGU[1] + GIO_THUC[1] - 1
                    a = - GIO_NGU[0] + GIO_THUC[0] - 1
                else: 
                    if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                        b = 60 - GIO_NGU[1] + GIO_THUC[1] - 1
                        a = 23
                    else: #gio lơn
                        b = 60 - GIO_NGU[1] + GIO_THUC[1] - 1
                        a = 24 - GIO_NGU[0] + GIO_THUC[0] - 1
    else: # giay bang
        if GIO_NGU[1] - GIO_THUC[1] < 0: #phut nho
            if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                b = - GIO_NGU[1] + GIO_THUC[1]
                a = - GIO_NGU[0] + GIO_THUC[0]
            else: 
                if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                    b = - GIO_NGU[1] + GIO_THUC[1]
                    a = 0
                else: #gio lơn
                    b = - GIO_NGU[1] + GIO_THUC[1]
                    a = 24 - GIO_NGU[0] + GIO_THUC[0]
        else:
            if GIO_NGU[1] - GIO_THUC[1] == 0: #phut bang
                if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                    b = 0
                    a = - GIO_NGU[0] + GIO_THUC[0]
                else:
                    if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                        b = 0
                        a = 0
                    else: #gio lơn
                        b = 0
                        a = 24 - GIO_NGU[0] + GIO_THUC[0]
            else: #phut lơn
                if GIO_NGU[0] - GIO_THUC[0] < 0: #gio nho
                    b = 60 - GIO_NGU[1] + GIO_THUC[1]
                    a = - GIO_NGU[0] + GIO_THUC[0] - 1
                else:
                    if GIO_NGU[0] - GIO_THUC[0] == 0: #gio bang
                        b = 60 - GIO_NGU[1] + GIO_THUC[1]
                        a = 23
                    else: #gio lơn
                        b = 60 - GIO_NGU[1] + GIO_THUC[1] 
                        a = 24 - GIO_NGU[0] + GIO_THUC[0] - 1
print("Thời gian ngủ : "+ str(a)+" giờ "+str(b)+ " phút")

        
