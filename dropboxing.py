import os
import dropbox

DBX = dropbox.Dropbox(os.getenv("dropbox"))


def downloading_file(file_from):
    """
    downloading file
    """
    with open(file_from, "wb") as file:
        metadata, res = DBX.files_download(path="/"+file_from)
        file.write(res.content)


def upload_file(file_from):
    """
    uploading new file
    """
    deleting_file(file_from)
    file = open(file_from, 'rb')
    DBX.files_upload(file.read(), "/"+file_from)


def deleting_file(file_from):
    """
    delete file
    """
    DBX.files_delete("/"+file_from)


def checking_exist(file_from):
    """
    checking if file exist
    """
    try:
        DBX.files_get_metadata("/"+file_from)
        return True
    except Exception:
        return False
