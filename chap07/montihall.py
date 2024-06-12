import random

NGames=10000
UnchangeGame=[]
ChangeGame=[]

for i in range(0, NGames):
    # 자동차는 랜덤하게 숨겨진다. 
    CarDoor=random.choice(["Door1", "Door2", "Door3"])

    # 사용자가 첫 번째 선택을 한다. 
    UserDoor=random.choice(["Door1", "Door2", "Door3"])
    
    # 호스트가 자동차가 있지 않은 문을 연다. 
    OpenDoor=list(set(["Door1", "Door2", "Door3"])-set([UserDoor, CarDoor]))[0]
    
    # 남아 있는 문을 결정한다. 
    OtherDoor=list(set(["Door1", "Door2", "Door3"])-set([UserDoor, OpenDoor]))[0]
    
    # 사용자가 선택을 바꾸지 않아서 성공하면 True를 리스트에 추가한다. True는 정수 1이다.
    UnchangeGame.append(UserDoor==CarDoor)
    
    # 사용자가 선택을 바꾸어서 성공하면 True를 리스트에 추가한다.  True는 정수 1이다.
    ChangeGame.append(OtherDoor==CarDoor)

# 각 리스트에서 정수 1의 개수를 센다.     
print(f"{NGames} 개의 게임 중에서 바꾸지 않았을 때의 승률: {sum(UnchangeGame)/NGames} \n\
      바꾸었을 때의 승률: {sum(ChangeGame)/NGames}")
