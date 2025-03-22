import bcrypt

class EncryptionManager:
    def create_hash(self, text):
        salt =bcrypt.gensalt()
        return bcrypt.hashpw(text.encode("utf-8"), salt).decode("utf-8")#tipo de codificacion que tenemos. Se la pasamos por que el python esta pendejo y no sabe
    

    def compare_hashes(self, text, hashpw):
        return bcrypt.checkpw(text.encode("utf-8"), hashpw.encode("utf-8"))