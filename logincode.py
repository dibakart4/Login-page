#Log-in page

#importing the necessary packages
import ipywidgets as widgets             #to get the widgets
from IPython.display import display      #to display the created widgets

#to direct our widgets
e_add=widgets.Text(description="E-mail")                                #to allow the user to type the e-mail
e_pass=widgets.Password(description="Password")                          #to allow the user to type the password(it is in dots)
c=widgets.Button(description="Log in", button_style="info")         #to prompt the user to log-in
val=widgets.Text(description=e_pass.value, disabled=True)                #to show the password entered by the user(disabling it so that he cannot make changes to it)
mylink=widgets.jslink((e_pass,'value'),(val,'value'))                    #to link the password entered with 'val'
display(e_add,e_pass,val,c)                                                  #to display all the values

#to define a function which checks for the entered values
def on_button_clicked(b):                                                   #defining a function to check for the credentials
        if(a.value==''):                                                    #in case the e-mail box is left empty
            print("There must be some address. It cannot be empty")         #giving a suitable message
            c.button_style='danger'                                         #changing the button colour to red(indicating wrong)
        else:                                                               #else if the value isn't empty
            if(val.value=="pass@123" and e_add.value=="someone@email.com"):     #it checks the entered values with the values here
                print("Access Granted")                                     #print suitable message
                print("---Welcome---")                                      #greet the user
            else:                                                           #if the entered values do not match
                print("The entered password or e-mail is wrong")            #tell him that the entered e-mail or password is wrong
                c.button_style='danger'                                     #turn the button to red colour

c.on_click(on_button_clicked)                   #call the function by using the attribue of c 'on_click' and passing the name of the function
