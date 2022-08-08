rth6 = canvas.create_polygon(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, fill="#213b52",tags=("bg_polygen_dash6"),smooth=True,)
                    

                    canvas.create_line(0, 0, 0, 0,fill="gray", tag=("sales_hr") )
                    
                    if exp_totl_inv[2]==None or exp_totl_inv[2]=='':
                        dates_start=date.today()
                    else:
                        dates_start=exp_totl_inv[2] 
                    

                    sql_pro="select sum(grandtotal) from app1_invoice where cid_id=%s and invoicedate between %s and %s "
                    sql_pro_val=(dtl_cmp_pro[0],dates_start,date.today(),)
                    fbcursor.execute(sql_pro,sql_pro_val,)
                    sal_totl_inv=fbcursor.fetchone()

                    sql_pros="select sum(grandtotal) from app1_invoice where cid_id=%s and invoicedate=%s "
                    sql_pros_val=(dtl_cmp_pro[0],dates_start,)
                    fbcursor.execute(sql_pros,sql_pros_val,)
                    sal_totl_invs=fbcursor.fetchone()
                    

                    if sal_totl_inv[0]==None or sal_totl_inv[0]=='':
                        tot_sal=0.0
                    else:
                        tot_sal=sal_totl_inv[0]

                    if sal_totl_invs[0]==None or sal_totl_invs[0]=='':
                        tot_sal_start=0.0
                    else:
                        tot_sal_start=sal_totl_invs[0]

                    sales_lb=Label(canvas, text="SALES ₹"+str(tot_sal),bg="#213b52", fg="White", anchor="nw",font=('Calibri 16 bold'))
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=sales_lb, tag=("sales_lb"))

                    
                    figlast = plt.figure(figsize=(8, 4), dpi=50)
                    x = [1, 2, ]
                    y = [tot_sal_start,tot_sal]
                    labels = [dates_start, date.today()]

                    plt.plot(x, y)
                    # You can specify a rotation for the tick labels in degrees or with keywords.
                    plt.xticks(x, labels, rotation='horizontal')
                    # Pad margins so that markers don't get clipped by the axes
                    plt.margins(0.2)
                    # Tweak spacing to prevent clipping of tick-labels
                    plt.subplots_adjust(bottom=0.15)
                    figlast.set_facecolor("#213b52")
                    

                    canvasbar = FigureCanvasTkAgg(figlast, master=canvas)
                    canvasbar
                    canvasbar.draw()
                    canvasbar.get_tk_widget()
                    win_inv1 = canvas.create_window(0, 0, anchor="nw", window=canvasbar.get_tk_widget(), tag=("grapg_6"))