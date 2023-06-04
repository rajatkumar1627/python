x = "global"


def outer():
    x = "outer local"

    def inner():
        x = "inner local"

        def func():
            x = "func local"
            print(x)

        func()

    inner()


outer()  # "func local"
