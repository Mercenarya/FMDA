import flet as ft
from flet import View
def main(page: ft.Page):
   #Login Page
   
   
#Functionality Design and Logical
   Errors_spot =ft.Text(color="red")
   Errors_spot_Recovery = ft.Text(color="red")
   def Accept_Denied(e):
        with open("D:/Password/FMDAUSername.txt","r") as f:
            checking_usr = f.read().strip()
            if LOGIN_USERNAME.value.strip() == checking_usr:
                with open("D:/Password/FMDAPassword.txt","r") as f2:
                    checking_pasw = f2.read().strip()
                    if LOGIN_PASSWORD.value.strip() == checking_pasw:
                        page.go("/Menu")
                    else: 
                        Errors_spot.value = f"Password or Username are wrong"
            else:
                Errors_spot.value = f"Password or Username are wrong"
        page.update()
   def Recovering(e):
        
            if RESET_LOGIN_PASSWORD.value == "" or RESET_LOGIN_USERNAME.value == "" :
                Errors_spot_Recovery.value = f"None or Wrong Filled Information"
            elif PHONENUMBER_KEY.value != "0766709535" and SECURITY_KEY.value != "17102004":
                Errors_spot_Recovery.value = f"None or Wrong Filled Information"
            else:
                try:
                    with open("D:/Password/FMDAUSername.txt","w") as f:
                        f.write(RESET_LOGIN_USERNAME.value)
                        with open("D:/Password/FMDAPassword.txt","w") as f1:
                            f1.write(RESET_LOGIN_PASSWORD.value)
                    page.snack_bar = ft.SnackBar(ft.Text("Recovery have been Completed !!!"))
                    page.snack_bar.open = True
                    page.go("/Login") 
                    
                except:
                    print("Errors")
            page.update()
            
            
   #Theme Settings 
   
   def Change_theme(e):
    #    ft.ThemeMode.DARK,
       page.theme_mode = (
           ft.ThemeMode.DARK
           if page.theme_mode == ft.ThemeMode.LIGHT
           else ft.ThemeMode.LIGHT
       )
       page.update()
   #Page's Navigating with a functional Variables
   
   def Selected_page(e):
       for index, page_nav in enumerate(pages_stack):
           page_nav.visible = True if index == MENU_RAIL.selected_index else False
       page.update()
           

   #Custom Function's Information Display
   IMG_AVT = ft.Image(src="C:/SIUU/user_1177568.png",height=100,width=100)
   LOGIN_USERNAME = ft.TextField(label="Username", width=400,data="Usr")
   LOGIN_PASSWORD = ft.TextField(label="Password",width=400, password=True, can_reveal_password=True)
   LOGIN_BUTTON = ft.ElevatedButton(text="Login",icon=ft.icons.LOGIN_OUTLINED, on_click=Accept_Denied, width=400, color="white", bgcolor="Black")
   QUE_BUTTON = ft.TextButton('Forgot Password ? Click here', icon=ft.icons.PASSWORD, on_click= lambda _: page.go('/Recovery'))
   
   
   
   #Custom Reset Password Interface
   RESET_LOGIN_USERNAME = ft.TextField(label="Enter new Username", width=400,data="Usr")
   RESET_LOGIN_PASSWORD = ft.TextField(label="Enter New Password",width=400, password=True, can_reveal_password=True)
   PHONENUMBER_KEY = ft.TextField(label="Enter Phone number", width=400,data="Usr")
   SECURITY_KEY = ft.TextField(label="Secret key", width=400,data="Usr")
   RESET_BUTTON = ft.ElevatedButton(text='Confirm',width=400, bgcolor= "blue", color="White", on_click=Recovering)
   
   #Custom Homepage Login Interface
   
   
   
   
   
   #Custom Page's loop
   Banner_view_1 = ft.Row(
         
         controls=[
            ft.Row(
                [
                    
                    ft.Container(

                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text("     For your Financial\n     Wellness", size=50, weight="bold", color="white"),
                                        ft.Text("                  It's Starts when knowing your where you stand\n                  Enjoy and be Comfortable with your Side", color="white"),
                                        
                                    ],
                                    
                                ),
                            
                                ft.Row(
                                    [
                                        ft.Text(" "*20),
                                        
                                        ft.Icon(name=ft.icons.PRICE_CHECK_SHARP, size=150, color="Green"),
                                        
                                    ],
                                    
                                )
                        
                            ],
                        ),
                        bgcolor=ft.colors.LIGHT_BLUE,
                        height=250,
                        width=800,
                    ),
                ],
                
            )
            
        ],
     
     )
     
     
   Banner_view_2 = ft.Row(
         
         controls=[
            ft.Row(
                [
                    
                    ft.Container(

                        ft.Row(
                            [
                                ft.Column(
                                    [
                                       ft.Text("     Planning - Save - Analytics\n     Stand with user's Quality", size=50, weight="bold", color="white"),
                                       ft.Text("                  Perfectly, Clearly and Critical Feartures with all Available Options \n                  with Guides, Suggestion and more", color="white"),
                                        
                                        
                                    ],
                                    
                                ),
                            
                                ft.Row(
                                    [
                                        ft.Text(" "),
                                        
                                        ft.Icon(name=ft.icons.DONE_ALL, size=150, color="blue"),
                                        
                                    ],
                                    
                                ),
                        
                            ],
                        ),
                        bgcolor=ft.colors.OUTLINE_VARIANT,
                        height=250,
                        width=960,
                    ),
                ],
                
            )
            
        ],
     
     )
   Banner_view_3 = ft.Row(
         
         controls=[
            ft.Row(
                [
                    
                    ft.Container(

                        ft.Row(
                            [
                                ft.Column(
                                    [
                                       ft.Text("     Suitable for many types of users\n     And their Needs", size=50, weight="bold", color="white"),
                                       ft.Text("                  All People can Applied this App to many Purposes \n                  with our Option", color="white"),
                                        
                                        
                                    ],
                                    
                                ),
                            
                                ft.Row(
                                    [
                                        ft.Text(" "),
                                        
                                        ft.Icon(name=ft.icons.ATTRACTIONS_ROUNDED, size=150, color="yellow"),
                                        
                                    ],
                                    
                                )
                        
                            ],
                        ),
                        bgcolor=ft.colors.PURPLE,
                        height=250,
                        width=1050,
                    ),
                ],
                
            )
            
        ],
     
     )
   Settings = ft.Column(
       controls=[
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           )
           ,
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           )
           ,
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           ),
           ft.Container(
               ft.Text("Page Theme Settings",weight="bold"),
               
               visible= True
           ),
           ft.Container(
               ft.Switch(label="",on_change=Change_theme),
               
               visible=True
           )
       ],
       scroll=True
   )
   
   normal_radius = 50
   hover_radius = 0
   normal_title_style = ft.TextStyle(
        size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
   chart = ft.PieChart(
        sections=[
            ft.PieChartSection(
                40,
                title="40%",
                title_style=normal_title_style,
                color=ft.colors.BLUE,
                radius=normal_radius,
            ),
            ft.PieChartSection(
                30,
                title="30%",
                title_style=normal_title_style,
                color=ft.colors.RED,
                radius=normal_radius,
            ),
            
            
        ],
        sections_space=0,
        center_space_radius=40,
        expand=True,
        visible=True,
    )
   Balance_spotting = ft.Row(
       controls=[
           ft.Container(
                ft.Column(
                [
                    ft.Text("Current Balance",size=30,weight="bold"),
                    ft.Text("  450.000 VND", size=30, color="#FFCC33"),  
                ],
            ),
                padding=35,
                bgcolor=ft.colors.GREEN,
                width= 300,
                
           ),
       ],
   )
   Percent_spotting = ft.Row(
       controls=[
           ft.Container(
                ft.Column(
                [
                    ft.Text("Saving percents",size=30,weight="bold"),
                    ft.Text("   70% - 100%", size=30, color="blue"),  
                ],
            ),
                padding=35,
                bgcolor=ft.colors.ORANGE,
                width= 300,
                
           ),
       ],
   )
   Chart_spotting = ft.Row(
       controls=[
           ft.Container(
                content=chart,
                padding=35,
                bgcolor=ft.colors.YELLOW_ACCENT,
                width= 300,
                
           ),
       ],
   )
   Status_spotting = ft.Row(
       controls=[
           ft.Container(
                ft.Column(
                [
                    ft.Text("Status Updated",size=30,weight="bold"),
                    ft.Text("   GOOD", size=50, color="white"),  
                ],
            ),
            padding=35,
            bgcolor=ft.colors.GREY_500,
            width= 300,
           ),
       ],
   )
   
   
   
   
   

   
   #Container Scrolling
   page_1 = ft.Column(
       controls=[
           ft.Container(
               ft.Row(
                   [
                       Banner_view_1,
                       Banner_view_2,
                       Banner_view_3
                   ],
                   scroll="AUTO"
               ),
               
               visible=True
           ),
           ft.Container(
               ft.Row(
                   [
                       Balance_spotting,
                       Percent_spotting,
                       Chart_spotting,
                       Status_spotting,
                   ],
                   scroll="AUTO"
                ),
               
               height=300,
               width=3000,
           ),
           ft.Container(
               ft.Row(
                  
                ),
               bgcolor="Grey",
               height=100,
               width=3000,
           ),
           
       ],
       auto_scroll=True,
       alignment=ft.MainAxisAlignment.CENTER,
       
   )
   page_2 = ft.Column(
       controls=[
           ft.Container(chart),
           
       ],
       auto_scroll=True,
   )
   page_3 = ft.Column(
       controls=[
           ft.Container(Settings)
       ],
       auto_scroll=True,
   )
   
   
   
   pages_stack =  [
       ft.Container(page_1,visible=True),
       ft.Container(page_2,visible=False),
       ft.Container(page_3,visible=False),
   ]
   
   #Custom Menu Function's Information Display
   MENU_RAIL = ft.NavigationRail(
       
       selected_index=0,
       label_type=ft.NavigationRailLabelType.ALL,
       min_width=100,
       min_extended_width=400,
       leading=ft.FloatingActionButton(text="Add",on_click=None),
       group_alignment=-0.9,
       destinations=[
           ft.NavigationRailDestination(
               icon=ft.icons.HOME, label= "Home",
           ),
           ft.NavigationRailDestination(
               icon=ft.icons.LINE_AXIS, label= "Reports",
           ),
           ft.NavigationRailDestination(
               icon=ft.icons.HELP, label= "Helps", 
           ),
           ft.NavigationRailDestination(
               icon=ft.icons.SETTINGS, label= "Settings",
           ),
           ft.NavigationRailDestination(
               icon=ft.icons.ACCOUNT_BOX_ROUNDED, label= "Account", 
           ),
           ft.NavigationRailDestination(
               icon=ft.icons.ACCOUNT_BALANCE, label= "Balance",
           ),
       ],
       on_change=Selected_page
   )
  
   
   
   #Custom Layout for Login Screen Display
   Login = ft.Row(
       controls=[
           ft.Container(
               ft.Column(
               [
                   ft.Row(
                       [
                           ft.Text(" "*35),
                           IMG_AVT,
                           
                           ],
                       alignment= ft.MainAxisAlignment.CENTER
                    ),
                   ft.Text(" "),
                   #Fixing method: using text space
                   LOGIN_USERNAME,
                   LOGIN_PASSWORD,
                   LOGIN_BUTTON,
                   QUE_BUTTON,
                   Errors_spot    
               ],
           ),
               margin=220,
               
           ),
          
       ],
       alignment=ft.MainAxisAlignment.CENTER ,
   )
   #Custom Layout for Recovery
   
   Recover = ft.Row(
       controls=[
           ft.Container(
               ft.Column([
                   ft.Text("Recovery",size=40,weight="bold"),
                   RESET_LOGIN_USERNAME,
                   RESET_LOGIN_PASSWORD,
                   PHONENUMBER_KEY,
                   SECURITY_KEY,
                   Errors_spot_Recovery,
                   ft.Row(
                       [
                       RESET_BUTTON,
                   ],
                       
                alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.ElevatedButton("Back to Login",width=400, color= "white",bgcolor="red",on_click=lambda _:page.go("/Login"))
               ],             
            ),
               margin=100,
           ),
       ],
       alignment=ft.MainAxisAlignment.CENTER,
   )
   
   #ROUTE CHANGE EVENT
   #Route Changing method page.route
   def route_change(e):
        page.views.clear
        page.views.append(
            View(
               "/Login",
                [
                   Login
                ]
            )
        )
        if page.route == "/Menu":
            page.views.append(
                ft.View(
                    "/Menu",
                    [
                        ft.Row(
                            [
                                MENU_RAIL,
                                ft.VerticalDivider(width=1),          
                                ft.Column(pages_stack, expand=True),
                                
                            ],
                            expand=True
                        )
                    ]
                )
            )
        elif page.route == "/Recovery":
            page.views.append(
                ft.View(
                    "/Recovery",
                    [
                        ft.Column(
                            [
                               Recover
                            ]
                        )
                    ]
                )
            )
      
        page.update()
   def view_pop(View):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
   page.on_route_change = route_change
   page.on_view_pop = view_pop
   page.go(page.route)
       
       
   
   #Mangage Route changing, Theme, Source controlling 
   page.theme_mode = ft.ThemeMode.LIGHT
   page.vertical_alignment = ft.MainAxisAlignment.CENTER
   page.update()
ft.app(target=main)