class LikeLion :
    def __init__ (self,name,lion_num,lion_sex):
        self.name = name
        self.n = lion_num
        self.lion_sex = lion_sex

list_a = []
while True :
    name = input ("이름을 입력하세요 : ")
    if name == "그만":
       
        for i in list_a:
          print("이름은" + i.name +"," + "전화번호는" + i.n + "," + "성별은" + i.lion_sex + "입니다.")
        break
      
    lion_num = input ("전화번호를 입력하세요 : ")
    lion_sex = input ("성별을 입력하세요 (male이나 female로 작성해주세요) : ")
    if lion_sex != "male" and lion_sex != "female":
        lion_sex = "unknown"

    ahyeon_book = LikeLion (name,lion_num,lion_sex)
    list_a.append(ahyeon_book)
    for i in list_a:
        print("이름은" + i.name +"," + "전화번호는" + i.n + "," + "성별은" + i.lion_sex + "입니다.")