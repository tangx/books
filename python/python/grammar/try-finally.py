def divide(n1: int, n2: int) -> float | Exception:
    try:
        n = n1 / n2

    # 多一个 excpet 语句块，用于捕获除了 ZeroDivisionError 之外的异常
    except (ZeroDivisionError, OSError):
        return Exception("Division by zero")
    except TypeError:
        return Exception("Invalid type")
    else:
        # 当 try 语句块没有抛出异常时执行
        print("This will execute if no exception is raised")
        return n
    finally:
        print("This will always execute")


import httpx

c2 = httpx.Client()  # 创建客户端
MOVIES = "https://ghibliapi.herokuapp.com/films"
try:
    r2 = c2.get(MOVIES)
    print(r2.status_code)
    movies = r2.json()
    for movie in movies:
        print(movie["title"])
finally:
    c2.close()  # 关闭
