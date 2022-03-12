import os
import shutil
import time
from simple_chalk import chalk
from tqdm import tqdm


def backup(path) -> str:
    # * Main
    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    # specify the days
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present in path or not
    if os.path.exists(path):

        if listFilesCount(path)[1] == 0:
            for i in tqdm(range(7), desc="Scanning", ncols=74):
                time.sleep(0.1)
        else:
            for i in tqdm(range(listFilesCount(path)[1]), desc="Scanning", ncols=74):
                time.sleep(0.1)

        # iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):

            # comparing the days
            if seconds >= get_file_or_folder_age(root_folder):

                # removing the folder
                removeFolder(root_folder)
                deleted_folders_count += 1  # incrementing count

                # breaking after removing the root_folder
                break

            else:

                # checking folder from the root_folder
                for folder in folders:

                    # folder path
                    folder_path = os.path.join(root_folder, folder)

                    # comparing with the days
                    if seconds >= get_file_or_folder_age(folder_path):

                        # invoking the removeFolder function
                        removeFolder(folder_path)
                        deleted_folders_count += 1  # incrementing count

                # checking the current directory files
                for file in files:

                    # file path
                    file_path = os.path.join(root_folder, file)

                    # comparing the days
                    if seconds >= get_file_or_folder_age(file_path):

                        # invoking the removeFile function
                        removeFile(file_path)
                        deleted_files_count += 1  # incrementing count

        else:

            # if the path is not a directory
            # comparing with the days
            if seconds >= get_file_or_folder_age(path):

                # invoking the file
                removeFile(path)
                deleted_files_count += 1  # incrementing count

    else:

        # file/folder is not found
        print("\n" + chalk.red("Folder Not Found"), ":", path, "\n")
        deleted_files_count += 1  # incrementing count
        os._exit(1)

    if deleted_files_count > 0:
        print("\nTotal folders deleted :", deleted_folders_count)
        print("Total files deleted :", deleted_files_count)
    elif deleted_folders_count > 0:
        print("\nTotal folders deleted :", deleted_folders_count)
        print("Total files deleted :", deleted_files_count)
    else:
        print("\nTotal Folders Found :", listFilesCount(path)[3])
        print("Total Files Found :", listFilesCount(path)[1])
        print(
            "Total Files and Folders Found :",
            listFilesCount(path)[1] + listFilesCount(path)[3],
        )
        print(
            "\n" + chalk.green("Scanned :"),
            listFilesCount(path)[1] + listFilesCount(path)[3],
            "of",
            listFilesCount(path)[1] + listFilesCount(path)[3],
        )
        print(chalk.bold.yellow("No Old File/Folder Found !"))


def clear() -> None:
    # for windows
    if os.name == "nt":
        os.system("cls")

    # for mac and linux(if, os.name is 'posix')
    else:
        os.system("clear")


def error(code) -> int:
    if code == 1:
        print("\n" + chalk.yellow("User exited!"))
        os._exit(0)
    elif code == 2:
        print("\n" + chalk.red("SomeThing Went Wrong?"))
        os._exit(1)


def copyRight() -> None:
    app = "Backup Files"
    copyRight = app + " Copyright © " + str(time.localtime().tm_year) + " Junaid"

    # Giving a line for Credits
    print("\n")
    # Credits
    print("This tool is made by Junaid.")
    print(chalk.bgWhite.black(copyRight))


def removeFolder(path):
    print("\n"+chalk.yellow("We found an old folder."))

    # removing the folder
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print(chalk.red("Unable to delete the folder :"), path)
    else:
        print(chalk.red("Folder deleted :"), path)


def removeFile(path):
    print("\n"+chalk.yellow("We found an old file."))

    # removing the file
    try:
        os.remove(path)
    except FileNotFoundError:
        print(chalk.red("Unable to delete the file :"), path)
    else:
        print(chalk.red("file deleted :"), path)


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


def listFilesCount(path):
    listOfFiles = list()
    listOfDirs = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        listOfDirs += [os.path.join(dirpath, dirs) for dirs in dirnames]
    countOfFiles = listOfFiles.__len__()
    countOfDirs = listOfDirs.__len__()
    return [listOfFiles, countOfFiles, listOfDirs, countOfDirs]
