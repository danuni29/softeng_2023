import random

from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg


webpage = requests.get(
    "https://sobi.chonbuk.ac.kr/menu/week_menu.php")
soup = BeautifulSoup(webpage.content, "html.parser")
restaurants = soup.find_all('h5', {'class': 'title'})
# print(restaurants)


all_menu_items = []
menu_by_day = {'월': [], '화': [], '수': [], '목': [], '금': []}

for restaurant in restaurants:
    restaurant_name = restaurant.text.strip()

    # 원하는 식당이면 해당 식당의 식단을 출력
    if '후생관' in restaurant_name:
        menu = restaurant.find_next('tbody')
        if menu:
            print(f"식당: {restaurant_name}")
            for row in menu.find_all('tr'):
                # 조식인 경우 건너뛰기
                if '조식' in row.text:
                    continue
                if '도시락' in row.text:
                    continue
                # 각 행의 정보를 출력
                menu_items = [td.text.strip() for td in row.find_all('td')]
                all_menu_items.append(menu_items)

# print(all_menu_items)


# 요일마다 달라지는 메뉴...처리...
# 리스트 안의 값이 5개인 것은 차례대로 월화수목금에 넣어줌
# 나머지는 고정메뉴니까 월화수목금 다 넣어줌
for menu_item in all_menu_items:
    # print(menu_item)
    # Check the length of menu_item and process accordingly
    if len(menu_item) == 5:
        for i, day in enumerate(['월', '화', '수', '목', '금']):
            menu_by_day[day].append(menu_item[i])
    else:
        # Add the entire menu_item to all days
        for day in ['월', '화', '수', '목', '금']:
            menu_by_day[day].append(menu_item)
                # for menu_item in menu_items:



# 위에서 만든 요일별 메뉴에서.. 운영없음은 제거하고, '/'로 묶어있는 메뉴 정리, 리스트 안 리스트 값 정리..



for day, menu_items in menu_by_day.items():
    cleaned_menu_items = []

    for menu_item in menu_items:
        # '운영없음'이 있으면 제거
        if '운영없음' in menu_item:
            continue

        if isinstance(menu_item, list):
            cleaned_menu_items.extend(menu_item)
        else:
            # '/'로 구분된 문자열을 나누어 개별 아이템으로 만듦
            sub_items = [item.strip() for item in menu_item.split('/')]
            cleaned_menu_items.extend(sub_items)

    # 각 요일에 대한 처리가 끝나면 딕셔너리 업데이트
    menu_by_day[day] = cleaned_menu_items



# 결과 출력
print(menu_by_day['월'])
print(random.choice(menu_by_day['월']))




