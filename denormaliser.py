import urllib.parse
import readline

class Denormaliser:

    def __init__(self):
        self.target_chars = {
                #LFI
                "..":"\u2025",
                "/":"\uff0f",
                #SQLi
                "'":"\uff07",
                '"':"\uff02",
                "-":"\ufe63",
                #Open Redirect
#                ".":"\u3002",
                #XSS
                "<":"\uff1c",
                #SSTi
                "{{":"\ufe5b",
                "[[":"\uff3b",
                #Command injection
                "&":"\uff06",
                "|":"\uff5c",
                #File upload
                "php":"\uff50\u02b0\uff50"
                };


    def denormalise_to_unicode(self,text):
        for old, new in self.target_chars.items():
            text = text.replace(old,urllib.parse.quote(new));

        return text

if __name__ == "__main__":
    denormer = Denormaliser();
    while True:
        try:
            t = input("$> ");
        except:
            print("Bye then :(");
            exit();
        a = denormer.denormalise_to_unicode(t);
        print(a);
