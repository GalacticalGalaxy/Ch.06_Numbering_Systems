import arcade
SW = 600
SH = 400

arcade.open_window(SW, SH, "Star Wars Art", True)
arcade.set_background_color((63,271,65))

arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,400, 300,200, arcade.color.AFRICAN_VIOLET)
arcade.draw_rectangle_filled(300,200,50,50, (255, 0, 0, 20),45)
arcade.draw_point(300,300,(0,0,0),5)
arcade.draw_line(20,30,100,200,(arcade.color.BLUE), 3)
arcade.draw_circle_filled(400,100,20,arcade.color.GREEN)
arcade.draw_text("May the force be with you!",300,300,arcade.color.BLACK,40,600,"center","Papyrus",True,True,"center")



for i in range(0,SW+1,20):
    arcade.draw_rectangle_filled(i,20,10,30, arcade.color.WHITE)
arcade.draw_line(0,14,SW,14,arcade.color.WHITE, 5)
arcade.draw_line(0,25,SW,25,arcade.color.WHITE, 5)





arcade.finish_render()
arcade.run()




