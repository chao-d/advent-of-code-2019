from termcolor import colored


WIDTH, HEIGHT = 25, 6
SIZE = WIDTH * HEIGHT


def decode_image(nums):
    image = []
    for i in range(0, len(nums), SIZE):
        if i == 0:
            image.extend(nums[i: i + SIZE])
        else:
            for j in range(i, i + SIZE):
                image[j % SIZE] = decode_pixel(image[j % SIZE], nums[j])
    s = "".join([str(k) for k in image])
    for i in range(0, SIZE, WIDTH):
        for j in s[i: i + WIDTH]:
            if j == "0":
                print(colored("#", "grey"), end="")
            else:
                print(colored("#", "white"), end="")
        print()


def decode_pixel(first, sec):
    if first != 2:
        return first
    else:
        return sec


if __name__ == "__main__":
    with open("./day8input") as f:
        for line in f:
            nums = [int(num) for num in str(line).rstrip()]
    decode_image(nums)
