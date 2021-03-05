def banner_text(text):
    screen_width = 10
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))
    
    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width-4))
        print(output_string)


banner_text("*")
banner_text("test")
banner_text(" ")
banner_text("testtesttesttesttest")
banner_text("*")