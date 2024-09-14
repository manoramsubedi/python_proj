import json


def load_data():
    try:
        with open('yt.txt', 'r') as file:
            return json.load(file)
            #print(test)
            #return test
    except FileNotFoundError:
        return []

def save_data(video):
    with open('yt.txt', 'w') as file:
        json.dump(video, file) # Write data

def add_video(video):
    name = input("Enter Video Title:")
    url = input("Enter Video URL:")

    video.append(
        {'name':name, 'url': url}
    )
    save_data(video)


def list_all(video):
    print('*'*90)
    print("\n")
    for index, vid in enumerate(video, start=1):
        print(f"{index}. Title: {vid['name']} |  Link: {vid['url']}")

    print("\n")
    print('*'*90)


def update_video(video):
    list_all(video)
    index = int(input("Enter the video number to update:"))

    if 1 <= index <= len(video):
        new_name=input("Enter video name: ")
        new_url=input("Enter video url: ")

        video[index-1]={'name':new_name, 'url': new_url}
        save_data(video)

    else:
        print("Invalid index selected.")


def delete_video(video):
    list_all(video)
    index = int(input("Enter video you want to delete: "))

    if 1 <= index <= len(video):
        del video[index-1]
        save_data(video)

    else:
        print("Invalid index selected.")


def main():
    video=load_data()
    print(video)
    while True:
        print("\n")
        print("Welcome to Youtube Manager")
        print("1. Add Video")
        print("2. List all the video detials.")
        print("3. Update video detials.")
        print("4. Delete Video.")
        print("5. Exit")

        choice = input("Enter your choice:")

        match choice:
            case '1':
                add_video(video)

            case '2':
                list_all(video)

            case '3':
                update_video(video)

            case '4':
                delete_video(video)

            case '5':
                exit()

            case _:
                print("Invalid Choice.")


if __name__ == "__main__":
    main()

