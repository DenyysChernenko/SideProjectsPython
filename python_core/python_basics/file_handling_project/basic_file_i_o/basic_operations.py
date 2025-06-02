import textwrap

content = textwrap.dedent(
    """\
        some_content 1
        some_content 2
        some_content 3
        """
)

content2 = textwrap.dedent(
    """\
    new_content 1 
    new_content 2
    new_content 3
    """
)

with open("example.txt", "r") as f:
    info = f.read()
    print(info + "\n")

with open("example.txt", "r") as f:
    for line in f:
        print(line)


with open("output.txt", "w") as f:
    f.write(content)

with open("output.txt", "a") as f:
    f.write(content2)


# try:
#     file = open("output2.txt", 'r')
# except FileNotFoundError:
#     print("File wasn't found, sorry!")
# finally:
#     print("finally message")


with open("binary.bin", "wb") as f:
    f.write(b"\x00\xff\x00")

with open("binary.bin", "rb") as f:
    content_binary: bytes = f.read()
    print(content_binary)

with open("binary.bin", "r") as f:
    content = f.read()
    print(content)

with open("large_text_source.txt", "r") as f_source, open(
    "large_text_destination.txt", "a"
) as f_dest:
    while True:
        data = f_source.read(1024)
        if not data:
            break
        f_dest.write(data)
