import os
import dropbox

dbx = dropbox.Dropbox(os.getenv("dropbox"))


def downloading_file(file_from):
    with open(file_from, "wb") as f:
        metadata, res = dbx.files_download(path="/"+file_from)
        f.write(res.content)


def upload_file(file_from):
    deleting_file(file_from)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), "/"+file_from)


def deleting_file(file_from):
    dbx.files_delete("/"+file_from)


def checking_exist(file_from):
    try:
        dbx.files_get_metadata(file_from)
        return True
    except Exception:
        return False

