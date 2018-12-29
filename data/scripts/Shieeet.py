import npyscreen

class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets

    F = npyscreen.Form(name = "Welcome To AlbertCat",)
    t = F.add(npyscreen.TitlePasswordGenerator, name = "[ 1. ] Password Generator :",)
    fn = F.add(npyscreen.TitleLogin, name = "[ 2. ] Login: ")

    ms = F.addd(npyscreen.TitleSelectOne, max_height= 5, value = [1,], name="Pick One",
                values = ["Password Generator", "Login",} scroll_exit=True)

    F.edit()

    print(ms.get_select_objects())

if __name__ == "__main__":
    App = App()
    App.run()