class Chef:
    def make_chicken(self):
        print("chef makes chicken")
    def make_pasta(self):
        print("chef makes pasta")
    def make_salad(self):
        print("chef makes salad")
class KoreanChef(Chef):
    def korean_bbq(self):
        print("chef makes korean bbq")
korean=KoreanChef()
korean.make_chicken()
korean.make_pasta()
korean.make_salad()
korean.korean_bbq()